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

import os
import sys
import subprocess
import configparser
import requests
import json
import io
import typing as T

from utils import Version

upload_repo = 'mesonbuild/wrapdb'

def get_wrap_list():
    stdout = subprocess.check_output(['meson', 'wrap', 'list'])
    return stdout.decode().splitlines()

def get_wrap_info(wrap: str) -> T.List[T.Tuple[str, str]]:
    versions: T.List[T.Tuple[str, str]] = []
    try:
        stdout = subprocess.check_output(['meson', 'wrap', 'info', wrap])
        for line in stdout.decode().splitlines()[1:]:
            line = line.strip()
            version, revision = line.split()
            versions.append((version, revision))
    except subprocess.CalledProcessError:
       pass
    return versions

def rewrite_wrap(wrap: str):
    # Add 'patch_directory' key info wrap file
    filename = f'subprojects/{wrap}.wrap'
    config = configparser.ConfigParser(interpolation=None)
    config.read(filename)
    wrap_section = config[config.sections()[0]]
    wrap_section['patch_directory'] = wrap
    with open(filename, 'w') as f:
        config.write(f)

def fetch_git(wrap: str, branch: str):
    # Fetch history from legacy repository and move files to new location
    os.makedirs(f'subprojects/packagefiles/{wrap}', exist_ok=True)
    subprocess.check_call(['git', 'fetch', f'https://github.com/mesonbuild/{wrap}', branch])
    subprocess.check_call(['git', 'merge', 'FETCH_HEAD', '--allow-unrelated-histories', '--no-edit'])
    subprocess.check_call(['git', 'mv', 'upstream.wrap', f'subprojects/{wrap}.wrap'])
    subprocess.check_call(['git', 'rm', 'readme.txt'])
    all_files = set(os.listdir('.'))
    packagefiles = all_files - {'subprojects', 'tools', '.git'}
    if wrap == 'openh264':
        os.makedirs(f'subprojects/packagefiles/{wrap}/subprojects/')
        subprocess.check_call(['git', 'mv', 'subprojects/gtest.wrap', f'subprojects/packagefiles/{wrap}/subprojects/'])
    if packagefiles != {'LICENSE.build'}:
        for i in packagefiles:
            subprocess.check_call(['git', 'mv', i, f'subprojects/packagefiles/{wrap}/'])
        rewrite_wrap(wrap)
        subprocess.check_call(['git', 'add', f'subprojects/{wrap}.wrap'])
    else:
        subprocess.check_call(['git', 'rm', 'LICENSE.build'])
    subprocess.check_call(['git', 'commit', '-m', f'Move {wrap} files'])

def create_release(tag: str, token: str):
    api = f'https://api.github.com/repos/{upload_repo}/releases'
    headers = { 'Authorization': f'token {token}' }
    json: T.Dict[str, str] = {
        'tag_name': tag,
        'name': tag,
    }
    response = requests.post(api, headers=headers, json=json)
    if response.status_code == 422:
        # This release has already been uploaded by previous run of the script
        return None
    response.raise_for_status()
    return response.json()['upload_url'].replace(u'{?name,label}','')

def upload(upload_url: str, content: T.AnyStr, mimetype: str, name: str, token: str):
    headers = {
        'Authorization': f'token {token}',
        'Content-Type': mimetype,
    }
    params = { 'name': name }
    response = requests.post(upload_url, headers=headers, params=params, data=content)
    response.raise_for_status()

def import_release(wrap: str, version: str, revision: str, token: str):
    # Create a release and copy files from the old repository
    tag = f'{wrap}_{version}-{revision}'
    upload_url = create_release(tag, token)
    if not upload_url:
        return

    # Rewrite the patch URL
    response = requests.get(f'https://github.com/mesonbuild/{wrap}/releases/download/{version}-{revision}/{wrap}.wrap')
    response.raise_for_status()
    config = configparser.ConfigParser()
    config.read_string(response.content.decode())
    wrap_section = config[config.sections()[0]]
    wrap_section['patch_url'] = f'https://wrapdb.mesonbuild.com/v2/{tag}/get_patch'
    with io.StringIO() as f:
        config.write(f)
        f.seek(0)
        wrap_content = f.read()
    upload(upload_url, wrap_content, 'text/plain', f'{wrap}.wrap', token)

    # Upload patch zip as-is
    response = requests.get(f'https://github.com/mesonbuild/{wrap}/releases/download/{version}-{revision}/{wrap}.zip')
    response.raise_for_status()
    upload(upload_url, response.content, 'application/zip', f'{tag}_patch.zip', token)

def get_provide(wrap: str):
    progs = []
    deps = []
    config = configparser.ConfigParser()
    config.read(f'subprojects/{wrap}.wrap')
    if 'provide' in config.sections():
        provide = config['provide']
        progs = [i.strip() for i in provide.get('program_names', '').split(',')]
        deps = [i.strip() for i in provide.get('dependency_names', '').split(',')]
        for k in provide:
            if k not in {'dependency_names', 'program_names'}:
                deps.append(k.strip())
    progs = [i for i in progs if i]
    deps = [i for i in deps if i]
    return progs, deps

def add_to_db(wrap: str, versions: T.List[T.Tuple[str, str]], releases: T.Dict[str, T.Dict[str, T.List[str]]]):
    releases.setdefault(wrap, {})
    releases[wrap].setdefault('versions', [])
    releases[wrap].setdefault('dependency_names', [])
    releases[wrap].setdefault('program_names', [])
    versions: T.List[Version] = [Version(f'{version}-{revision}') for version, revision in versions]
    versions = sorted(versions, reverse=True)
    versions: T.List[str] = [v._s for v in versions]
    progs, deps = get_provide(wrap)
    releases[wrap]['versions'] = versions
    releases[wrap]['program_names'] = progs
    releases[wrap]['dependency_names'] = deps

if __name__ == '__main__':
    token = sys.argv[1]
    releases: T.Dict[str, T.Dict[str, T.List[str]]] = {}
    # - Don't import sqlite, it has been replaced by sqlite3.
    # - Don't import libjpeg, it has been replaced by libjpeg-turbo.
    # - openh264 is special because it contains "subprojects/gtest.wrap" that
    #   conflicts with gtest from wrapdb.
    all_wraps = get_wrap_list()
    all_wraps.remove('sqlite')
    all_wraps.remove('libjpeg')
    all_wraps.remove('openh264')
    all_wraps.insert(0, 'openh264')
    for wrap in all_wraps:
        versions = get_wrap_info(wrap)
        if not versions:
            continue
        latest_branch, _ = versions[0]
        fetch_git(wrap, latest_branch)
        for version, revision in versions:
            import_release(wrap, version, revision, token)
        add_to_db(wrap, versions, releases)

    with open('releases.json', 'w') as f:
        json.dump(releases, f, indent=2, sort_keys=True)
