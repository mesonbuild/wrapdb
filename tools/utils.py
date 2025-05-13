# Copyright 2012-2021 The Meson development team

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from contextlib import contextmanager
import operator
import re
import os
import sys
import typing as T
import platform

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
