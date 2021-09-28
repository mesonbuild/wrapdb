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

import sys
import configparser
import shutil
import hashlib
import requests
import tempfile
import typing as T
import subprocess
import json

from pathlib import Path

class CreateRelease:
    def __init__(self, repo: T.Optional[str], token: T.Optional[str], tag: str):
        print('Preparing release for:', tag)
        self.tag = tag
        self.name, self.version = self.tag.rsplit('_', 1)
        self.repo = repo
        self.token = token

        with tempfile.TemporaryDirectory() as self.tempdir:
            self.read_wrap()
            self.find_upload_url()
            self.create_patch_zip()
            self.create_wrap_file()

    def read_wrap(self):
        filename = Path('subprojects', self.name + '.wrap')
        self.wrap = configparser.ConfigParser(interpolation=None)
        self.wrap.read(filename)
        self.wrap_section = self.wrap[self.wrap.sections()[0]]

    def create_patch_zip(self):
        patch_directory = self.wrap_section.get('patch_directory')
        if patch_directory is None:
            return

        directory = self.wrap_section.get('directory', self.name)
        srcdir = Path('subprojects', 'packagefiles', patch_directory)
        destdir = Path(self.tempdir, directory)

        generator = Path(srcdir, 'generator.sh')
        if generator.exists():
            subprocess.check_call([generator])

        # If no specific license is specified, copy wrapdb's
        license_file = srcdir / 'LICENSE.build'
        if not license_file.exists():
            shutil.copyfile('COPYING', license_file)

        shutil.copytree(srcdir, destdir)
        base_name = Path(self.tempdir, f'{self.tag}_patch')
        shutil.make_archive(base_name.as_posix(), 'zip', root_dir=self.tempdir, base_dir=directory)

        patch_filename = base_name.with_name(base_name.name + '.zip')
        self.upload(patch_filename, 'application/zip')

        h = hashlib.sha256()
        h.update(patch_filename.read_bytes())
        patch_hash = h.hexdigest()

        del self.wrap_section['patch_directory']
        self.wrap_section['patch_filename'] = patch_filename.name
        self.wrap_section['patch_url'] = f'https://wrapdb.mesonbuild.com/v2/{self.tag}/get_patch'
        self.wrap_section['patch_hash'] = patch_hash

    def create_wrap_file(self):
        filename = Path(self.tempdir, self.name + '.wrap')
        with open(filename, 'w') as f:
            self.wrap.write(f)

        print('Generated wrap file:')
        print(filename.read_text())
        self.upload(filename, 'text/plain')

    def find_upload_url(self):
        if not self.repo or not self.token:
            return
        api = f'https://api.github.com/repos/{self.repo}/releases'
        headers = { 'Authorization': f'token {self.token}' }
        response = requests.get(api, headers=headers)
        response.raise_for_status()
        for r in response.json():
            if r['tag_name'] == self.tag:
                self.upload_url = r['upload_url'].replace(u'{?name,label}','')
                print('Found release:', self.upload_url)
                return

        content = {
            'tag_name': self.tag,
            'name': self.tag,
        }
        response = requests.post(api, headers=headers, json=content)
        response.raise_for_status()
        self.upload_url = response.json()['upload_url'].replace(u'{?name,label}','')
        print('Created release:', self.upload_url)

    def upload(self, path: Path, mimetype: str):
        if not self.repo or not self.token:
            # Write files locally when not run on CI
            with Path('subprojects', 'packagecache', path.name).open('wb') as f:
                f.write(path.read_bytes())
            return
        headers = {
            'Authorization': f'token {self.token}',
            'Content-Type': mimetype,
        }
        params = { 'name': path.name }
        response = requests.post(self.upload_url, headers=headers, params=params, data=path.read_bytes())
        response.raise_for_status()

def run(repo: T.Optional[str], token: T.Optional[str]):
    with open('releases.json', 'r') as f:
        releases = json.load(f)
    stdout = subprocess.check_output(['git', 'tag'])
    tags = [t.strip() for t in stdout.decode().splitlines()]
    for name, info in releases.items():
        versions = info['versions']
        latest_tag = f'{name}_{versions[0]}'
        if latest_tag not in tags:
            CreateRelease(repo, token, latest_tag)

if __name__ == '__main__':
    # Support local testing when passing no arguments
    repo = token = None
    if len(sys.argv) > 1:
        repo, token = sys.argv[1:]
    run(repo, token)
