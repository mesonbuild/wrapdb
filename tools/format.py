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
import json
from pathlib import Path
import subprocess

from utils import format_meson, read_wrap

FORMAT_FILES = {'meson.build', 'meson_options.txt', 'meson.options'}

def main() -> None:
    with open('releases.json', 'r', encoding='utf-8') as f:
        releases = json.load(f)

    tags = set(subprocess.check_output(['git', 'tag', '--merged'], text=True).splitlines())

    files = []
    for name, info in releases.items():
        if f'{name}_{info["versions"][0]}' not in tags:
            config = read_wrap(name)
            patch_dir_name = config['wrap-file'].get('patch_directory')
            if patch_dir_name:
                patch_dir = Path('subprojects', 'packagefiles', patch_dir_name)
                files += [f for f in patch_dir.rglob('*') if f.name in FORMAT_FILES]

    format_meson(files)


if __name__ == '__main__':
    main()
