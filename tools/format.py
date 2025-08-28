#!/usr/bin/env python3

# Copyright 2021 Xavier Claessens <xclaesse@gmail.com>

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import annotations
from configparser import ConfigParser
import json
import os
from pathlib import Path
import platform
import subprocess
import time
import venv

FORMAT_FILES = {'meson.build', 'meson_options.txt', 'meson.options'}

def meson_path() -> Path:
    env_dir = Path(__file__).parent / 'mesonenv'
    if platform.system() == 'Windows':
        meson = env_dir / 'Scripts/meson.exe'
    else:
        meson = env_dir / 'bin/meson'

    try:
        if meson.stat().st_mtime + 86400 >= time.time():
            return meson
    except FileNotFoundError:
        pass

    if not env_dir.exists():
        venv.create(env_dir, with_pip=True)
    subprocess.run([
        meson.with_stem('pip'), 'install', '--disable-pip-version-check',
        '-qU', '--pre', 'meson'
    ], check=True)
    os.utime(meson)
    return meson


def main() -> None:
    with open('releases.json', 'r', encoding='utf-8') as f:
        releases = json.load(f)

    tags = set(subprocess.check_output(['git', 'tag', '--merged'], text=True).splitlines())

    files = []
    for name, info in releases.items():
        if f'{name}_{info["versions"][0]}' not in tags:
            config = ConfigParser(interpolation=None)
            config.read(f'subprojects/{name}.wrap', encoding='utf-8')
            patch_dir_name = config['wrap-file'].get('patch_directory')
            if patch_dir_name:
                patch_dir = Path('subprojects', 'packagefiles', patch_dir_name)
                files += [f for f in patch_dir.rglob('*') if f.name in FORMAT_FILES]

    if files:
        cmd: list[Path | str] = [meson_path(), 'format', '--configuration', './meson.format', '--inplace']
        args = cmd + files
        subprocess.run(args, check=True)


if __name__ == '__main__':
    main()
