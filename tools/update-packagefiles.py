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

import configparser
import tarfile
import zipfile
import shutil
from pathlib import Path

def read_wrap(filename: Path):
    wrap = configparser.ConfigParser(interpolation=None)
    wrap.read(filename)
    return wrap[wrap.sections()[0]]

def read_archive_files(path: Path, base_path: Path):
    if path.suffix == '.zip':
        with zipfile.ZipFile(path, 'r') as archive:
            archive_files = set(base_path / i for i in archive.namelist())
    else:
        with tarfile.open(archive_path) as archive:
            archive_files = set(base_path / i.name for i in archive)
    return archive_files

if __name__ == '__main__':
    for f in Path('subprojects').glob('*.wrap'):
        wrap_section = read_wrap(f)
        patch_directory = wrap_section.get('patch_directory')
        if not patch_directory:
            continue
        directory = Path('subprojects', wrap_section['directory'])
        if not directory.is_dir():
            continue
        archive_path = Path('subprojects', 'packagecache', wrap_section['source_filename'])
        if not archive_path.exists():
            continue
        lead_directory_missing = bool(wrap_section.get('lead_directory_missing', False)) # type: ignore
        base_path = directory if lead_directory_missing else Path('subprojects')
        archive_files = read_archive_files(archive_path, base_path)
        directory_files = set(directory.glob('**/*'))
        new_files = directory_files - archive_files
        packagefiles = Path('subprojects', 'packagefiles', patch_directory)
        print(f'Updating {directory}')
        shutil.rmtree(packagefiles)
        for src_path in new_files:
            if not src_path.is_file():
                continue
            rel_path = src_path.relative_to(directory)
            dst_path = packagefiles / rel_path
            print(f'Copy {rel_path}')
            dst_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(src_path, dst_path)
