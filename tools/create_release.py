#!/usr/bin/env python3

# Copyright 2021 Xavier Claessens <xclaesse@gmail.com>

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
import io
import sys
import shutil
import hashlib
import requests
import tempfile
import typing as T
import subprocess
import json

from pathlib import Path
from utils import CIConfig, Releases, is_ci, is_debianlike, read_wrap, write_wrap

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
            self.create_source_fallback()
            self.create_patch_zip()
            self.create_wrap_file()
            self.finalize()

    def warn(self, message: str) -> None:
        if is_ci():
            print(f'::warning file=subprojects/{self.name}.wrap,line=1,title={self.name}::{message}')
        else:
            print(message)

    def read_wrap(self) -> None:
        self.wrap = read_wrap(self.name)
        self.wrap_section = self.wrap[self.wrap.sections()[0]]

    def create_patch_zip(self) -> None:
        patch_directory = self.wrap_section.get('patch_directory')
        if patch_directory is None:
            return

        directory = self.wrap_section.get('directory', self.name)
        srcdir = Path('subprojects', 'packagefiles', patch_directory)
        destdir = Path(self.tempdir, directory)

        generator = Path(srcdir, 'generator.sh')
        if generator.exists():
            try:
                ci = CIConfig.load()
            except json.decoder.JSONDecodeError as ex:
                raise RuntimeError(f'CI config is malformed') from ex

            debian_packages = ci.get(self.name, {}).get('debian_packages', [])
            if debian_packages and is_debianlike():
                if is_ci():
                    subprocess.check_call(['sudo', 'apt-get', 'update'])
                    subprocess.check_call(['sudo', 'apt-get', '-y', 'install'] + debian_packages)
                else:
                    s = ', '.join(debian_packages)
                    print(f'The following packages could be required: {s}')

            subprocess.check_call([generator])

        shutil.copytree(srcdir, destdir)
        # If no specific license is specified, copy wrapdb's
        license_file = destdir / 'LICENSE.build'
        if not license_file.exists():
            shutil.copyfile('COPYING', license_file)

        base_name = Path(self.tempdir, f'{self.tag}_patch')
        shutil.make_archive(base_name.as_posix(), 'zip', root_dir=self.tempdir, base_dir=directory)

        patch_filename = base_name.with_name(f'{base_name.name}.zip')
        self.upload(patch_filename, 'application/zip')

        h = hashlib.sha256()
        h.update(patch_filename.read_bytes())
        patch_hash = h.hexdigest()

        del self.wrap_section['patch_directory']
        self.wrap_section['patch_filename'] = patch_filename.name
        self.wrap_section['patch_url'] = f'https://wrapdb.mesonbuild.com/v2/{self.tag}/get_patch'
        self.wrap_section['patch_fallback_url'] = f'https://github.com/mesonbuild/wrapdb/releases/download/{self.tag}/{patch_filename.name}'
        self.wrap_section['patch_hash'] = patch_hash

    def create_wrap_file(self) -> None:
        self.wrap_section['wrapdb_version'] = self.version

        filename = Path(self.tempdir, f'{self.name}.wrap')
        write_wrap(filename, self.wrap)

        print('Generated wrap file:')
        print(filename.read_text())
        self.upload(filename, 'text/plain')

    def find_upload_url(self) -> None:
        if not self.repo or not self.token:
            return
        api = f'https://api.github.com/repos/{self.repo}/releases'
        headers = { 'Authorization': f'token {self.token}' }
        response = requests.get(api, headers=headers)
        response.raise_for_status()
        for r in response.json():
            if r['tag_name'] == self.tag:
                if r['draft']:
                    delete_api = f'https://api.github.com/repos/{self.repo}/releases/{r["id"]}'
                    response = requests.delete(delete_api, headers=headers)
                    response.raise_for_status()
                    print('Deleted stale release draft:', r['id'])
                else:
                    raise Exception('Refusing to recreate existing release')

        cmd = ['git', 'rev-parse', 'HEAD']
        commit = subprocess.check_output(cmd, text=True).strip()
        content = {
            'tag_name': self.tag,
            'name': self.tag,
            'target_commitish': commit,
            'draft': True,
        }
        response = requests.post(api, headers=headers, json=content)
        response.raise_for_status()
        r = response.json()
        self.release_id = r['id']
        self.upload_url = r['upload_url'].replace('{?name,label}','')
        print('Created release:', self.upload_url)

    def upload(self, path: Path, mimetype: str) -> None:
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

    def create_source_fallback(self) -> None:
        for url in (self.wrap_section['source_url'],
                    self.wrap_section.get('source_fallback_url')):
            if url is None:
                continue
            try:
                response = requests.get(url, headers={'User-Agent': 'wrapdb/0'})
                response.raise_for_status()
                digest = hashlib.sha256(response.content).hexdigest()
                if digest != self.wrap_section['source_hash']:
                    raise Exception(f'Hash mismatch for {url} ({len(response.content)} bytes): expected {self.wrap_section["source_hash"]}, found {digest}')
                # we don't rewrite the wrap's source_url, even if we had to
                # use the source_fallback_url instead
                break
            except Exception as ex:
                self.warn(str(ex))
        else:
            self.warn("Couldn't download source archive; skipping creation of source fallback")
            return

        filename = Path(self.tempdir, self.wrap_section['source_filename'])
        filename.write_bytes(response.content)
        self.upload(filename, 'application/zip')
        self.wrap_section['source_fallback_url'] = f'https://github.com/mesonbuild/wrapdb/releases/download/{self.tag}/{filename.name}'

    def finalize(self) -> None:
        if not self.repo or not self.token:
            return
        api = f'https://api.github.com/repos/{self.repo}/releases/{self.release_id}'
        headers = { 'Authorization': f'token {self.token}' }
        content = { 'draft': False }
        response = requests.patch(api, headers=headers, json=content)
        response.raise_for_status()
        print('Published release:', self.upload_url)

def run(repo: T.Optional[str], token: T.Optional[str]) -> None:
    releases = Releases.load()
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
