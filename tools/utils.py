# Copyright 2012-2021 The Meson development team

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     https://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import annotations
import abc
import configparser
from contextlib import contextmanager
import functools
import io
import json
import operator
import os
from pathlib import Path
import platform
import re
import subprocess
import sys
import time
import venv
import typing as T

# a helper class which implements the same version ordering as RPM
class Version:
    def __init__(self, s: str) -> None:
        self._s = s

        # split off revision and store it separately
        match = re.match('(.+)-([0-9]+)$', s)
        if not match:
            raise ValueError(f'Missing/invalid revision: {s}')
        v = match[1]
        self._r = int(match[2])

        # split version into numeric, alphabetic and non-alphanumeric sequences
        sequences1 = re.finditer(r'(\d+|[a-zA-Z]+|[^a-zA-Z\d]+)', v)

        # non-alphanumeric separators are discarded
        sequences2 = [m for m in sequences1 if not re.match(r'[^a-zA-Z\d]+', m.group(1))]

        # numeric sequences are converted from strings to ints
        sequences3 = [int(m.group(1)) if m.group(1).isdigit() else m.group(1) for m in sequences2]

        self._v = sequences3

    def __str__(self) -> str:
        return f'{self._s} (V={str(self._v)}, R={self._r})'

    def __repr__(self) -> str:
        return f'<Version: {self._s}>'

    def __lt__(self, other: object) -> bool:
        if isinstance(other, Version):
            return self.__cmp(other, operator.lt)
        return NotImplemented

    def __gt__(self, other: object) -> bool:
        if isinstance(other, Version):
            return self.__cmp(other, operator.gt)
        return NotImplemented

    def __le__(self, other: object) -> bool:
        if isinstance(other, Version):
            return self.__cmp(other, operator.le)
        return NotImplemented

    def __ge__(self, other: object) -> bool:
        if isinstance(other, Version):
            return self.__cmp(other, operator.ge)
        return NotImplemented

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Version):
            return self._v == other._v and self._r == other._r
        return NotImplemented

    def __ne__(self, other: object) -> bool:
        if isinstance(other, Version):
            return self._v != other._v or self._r != other._r
        return NotImplemented

    def __cmp(self, other: 'Version', comparator: T.Callable[[T.Any, T.Any], bool]) -> bool:
        # compare each sequence in order
        for ours, theirs in zip(self._v, other._v):
            # sort a non-digit sequence before a digit sequence
            ours_is_int = isinstance(ours, int)
            theirs_is_int = isinstance(theirs, int)
            if ours_is_int != theirs_is_int:
                return comparator(ours_is_int, theirs_is_int)

            if ours != theirs:
                return comparator(ours, theirs)

        # if one version has a suffix remaining, that version is greater
        if len(self._v) != len(other._v):
            return comparator(len(self._v), len(other._v))

        # versions are equal, so compare revisions
        return comparator(self._r, other._r)

class _JSONFile(abc.ABC):
    FILENAME: str

    def __init__(self, _: T.Any): ...

    @classmethod
    def load(cls) -> T.Self:
        with open(cls.FILENAME, encoding='utf-8') as f:
            return cls(json.load(f))

    def encode(self) -> str:
        return json.dumps(self, indent=2, sort_keys=True) + '\n'

    def save(self) -> None:
        with open(f'{self.FILENAME}.new', 'w', encoding='utf-8') as f:
            f.write(self.encode())
        os.rename(f'{self.FILENAME}.new', self.FILENAME)

    @classmethod
    def format(cls, *, check: bool = False) -> None:
        contents = Path(cls.FILENAME).read_text(encoding='utf-8')
        parsed = cls.load()
        if contents != parsed.encode():
            if check:
                raise FormattingError
            else:
                parsed.save()

class ProjectReleases(T.TypedDict):
    dependency_names: T.NotRequired[list[str]]
    program_names: T.NotRequired[list[str]]
    versions: list[str]
    deprecated: T.NotRequired[ProjectDeprecated]

class ProjectDeprecated(T.TypedDict):
    # for wraps with no replacement
    reason: T.NotRequired[str]
    # for wraps with an API-compatible replacement
    replacement: T.NotRequired[str]
    # for wraps with an API-incompatible replacement
    successor: T.NotRequired[str]

class Releases(T.Dict[str, ProjectReleases], _JSONFile):
    FILENAME = 'releases.json'

class ProjectCIConfig(T.TypedDict):
    build_on: T.NotRequired[dict[str, bool]]
    build_options: T.NotRequired[list[str]]
    fatal_warnings: T.NotRequired[bool]
    has_provides: T.NotRequired[bool]
    skip_dependency_check: T.NotRequired[list[str]]
    skip_program_check: T.NotRequired[list[str]]
    skip_tests: T.NotRequired[bool]
    test_options: T.NotRequired[list[str]]
    ignore_upstream_meson: T.NotRequired[str]

    alpine_packages: T.NotRequired[list[str]]
    brew_packages: T.NotRequired[list[str]]
    choco_packages: T.NotRequired[list[str]]
    debian_packages: T.NotRequired[list[str]]
    msys_packages: T.NotRequired[list[str]]
    python_packages: T.NotRequired[list[str]]

class CIConfig(T.Dict[str, ProjectCIConfig], _JSONFile):
    FILENAME = 'ci_config.json'

    @property
    def broken(self) -> list[str]:
        system = platform.system().lower()
        return T.cast('list[str]', self.get(f'broken_{system}', []))

    def get_option_arguments(self, name: str) -> list[str]:
        global_opts = T.cast('list[str]', self.get('global_build_options', []))
        opts = [o for o in global_opts if not o.startswith(f'{name}:')]
        opts += self.get(name, {}).get('build_options', [])
        return [f'-D{o}' for o in opts]

def wrap_path(name: str) -> Path:
    return Path('subprojects', f'{name}.wrap')

def read_wrap(name: str) -> configparser.ConfigParser:
    config = configparser.ConfigParser(interpolation=None)
    config.read(wrap_path(name), encoding='utf-8')
    return config

def write_wrap(path: Path, config: configparser.ConfigParser) -> None:
    # configparser write() adds multiple trailing newlines, collapse them
    buf = io.StringIO()
    config.write(buf)
    with path.open('w', encoding='utf-8') as f:
        f.write(buf.getvalue().rstrip('\n') + '\n')

@contextmanager
def ci_group(title):
    if is_ci() or sys.stdout.isatty():
        title = f'\33[34m{title}\33[0m'
    print(f'::group::{title}')
    try:
        yield
    finally:
        print('::endgroup::')

def is_ci() -> bool:
    return 'CI' in os.environ

def is_alpinelike() -> bool:
    return os.path.isfile('/etc/alpine-release')

def is_debianlike() -> bool:
    return os.path.isfile('/etc/debian_version')

def is_windows() -> bool:
    return platform.system().lower() == 'windows' and not "MSYSTEM" in os.environ

def is_msys() -> bool:
    return platform.system().lower() == 'windows' and "MSYSTEM" in os.environ

def is_macos():
    return any(platform.mac_ver()[0])

@functools.lru_cache
def venv_meson_path() -> Path:
    if is_ci():
        # assume CI already has a current Meson
        return Path('meson')

    env_dir = Path(__file__).parent / 'mesonenv'
    if not env_dir.exists():
        venv.create(env_dir, with_pip=True)

    if platform.system() == 'Windows':
        for subdir in 'Scripts', 'bin':
            if (env_dir / subdir).exists():
                meson = env_dir / subdir / 'meson.exe'
                break
        else:
            raise Exception("Couldn't find venv bin dir")
    else:
        meson = env_dir / 'bin/meson'

    try:
        if meson.stat().st_mtime + 86400 >= time.time():
            return meson
    except FileNotFoundError:
        pass

    subprocess.run([
        meson.with_name('pip' + meson.suffix),
        'install', '--disable-pip-version-check', '-qU', '--pre', 'meson'
    ], check=True)
    os.utime(meson)
    return meson

class FormattingError(Exception):
    pass

def format_meson(files: T.Iterable[Path], *, check: bool = False) -> None:
    if not files:
        return
    cmd: list[str | Path] = [venv_meson_path(), 'format', '--configuration', './meson.format']
    if check:
        cmd.append('--check-only')
    else:
        cmd.append('--inplace')
    cmd.extend(files)
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as ex:
        raise FormattingError from ex

def format_wrap(name: str, *, check: bool = False) -> None:
    '''Simple format cleanups:
       - Strip leading/trailing whitespace from lines
       - Fix line endings
       - Ensure key and value are separated by ' = '
       - Ensure file ends in a newline
       - Ensure sections are separated by blank lines and there are no other
         blank lines
       Does not understand continuation lines.
    '''
    path = wrap_path(name)
    old_contents = path.read_text(encoding='utf-8')
    new = []
    for line in old_contents.splitlines():
        line = line.strip()
        if not line:
            continue
        elif line[0] in {'#', ';'}:
            new.append(line)
        elif line[0] == '[':
            if new:
                new.append('')
            new.append(line)
        else:
            k, v = line.split('=', 1)
            new.append(f'{k.strip()} = {v.strip()}')
    new_contents = '\n'.join(new) + '\n'

    if old_contents != new_contents:
        if check:
            raise FormattingError
        else:
            with path.open('w', encoding='utf-8') as f:
                f.write(new_contents)
