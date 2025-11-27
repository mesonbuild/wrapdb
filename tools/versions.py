#!/usr/bin/env python3

# Copyright 2024-2025 Benjamin Gilbert <bgilbert@backtick.net>

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
from argparse import ArgumentParser, Namespace
from functools import cache
from hashlib import sha256
from itertools import count
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import time
import typing as T

import requests

from utils import Releases, read_wrap, wrap_path

WRAP_URL_TEMPLATE = (
    'https://github.com/mesonbuild/wrapdb/blob/master/subprojects/{0}.wrap'
)


class AnityaPackageList(T.TypedDict):
    items: list[AnityaPackage]
    items_per_page: int
    page: int
    total_items: int


class AnityaPackage(T.TypedDict):
    distribution: str
    ecosystem: str
    name: str
    project: str
    stable_version: str
    version: str


@cache
def get_upstream_versions() -> dict[str, str]:
    '''Query Anitya and return a dict: wrap_name -> upstream_version.'''

    items_per_page = 250
    versions = {}
    for i in count(1):
        for attempt in range(3):
            if attempt > 0:
                time.sleep(5)
            resp = requests.get(
                f'https://release-monitoring.org/api/v2/packages/'
                f'?distribution=Meson%20WrapDB'
                f'&items_per_page={items_per_page}'
                f'&page={i}'
            )
            # retry a few times on gateway timeout
            if resp.status_code != 504:
                resp.raise_for_status()
                break
        else:
            raise Exception('Repeated gateway timeouts querying Anitya')
        packages: AnityaPackageList = resp.json()
        versions.update({
            package['name']: package['stable_version']
            for package in packages['items']
        })
        if len(packages['items']) < items_per_page:
            break

    def sub(name: str, old: str, new: str) -> None:
        if name in versions:
            versions[name] = re.sub(old, new, versions[name])
    sub('icu', '-', '.')
    sub('inih', '^', 'r')
    sub('mt32emu', '_', '.')
    sub('re2', '-', '')
    return versions


@cache
def get_commit_releases(commit: str) -> Releases:
    '''Parse and return releases.json for the specified commit.'''
    data = subprocess.check_output(
        ['git', 'cat-file', 'blob', f'{commit}:releases.json'], text=True
    )
    return Releases(json.loads(data))


def get_wrap_versions() -> dict[str, str]:
    '''Return a dict: wrap_name -> wrapdb_version.'''
    return {
        name: info['versions'][0].split('-')[0]
        for name, info in Releases.load().items()
        if 'deprecated' not in info
    }


def get_port_wraps() -> set[str]:
    '''Return the names of wraps that have a patch directory.'''
    ports = set()
    for name, info in Releases.load().items():
        wrap = read_wrap(name)
        if wrap.has_option('wrap-file', 'patch_directory'):
            ports.add(name)
    return ports


def update_wrap(name: str, old_ver: str, new_ver: str) -> None:
    '''Try to update the specified wrap file from old_ver to new_ver.'''

    # read wrap file
    path = wrap_path(name)
    with path.open(encoding='utf-8') as f:
        lines = f.readlines()

    # update versions
    # rewrite wrap manually to preserve comments and spacing
    replacements = [
        (old_ver, new_ver),
        (old_ver.replace('.', '-'), new_ver.replace('.', '-')),
        (old_ver.replace('.', '_'), new_ver.replace('.', '_')),
    ]
    if old_ver.count('.') == 2 and new_ver.count('.') == 2:
        # some projects use URLs like .../projname/2.60/projname-2.60.3.tar.gz
        # this substitution must be done last
        replacements.append(
            ('.'.join(old_ver.split('.')[:2]), '.'.join(new_ver.split('.')[:2]))
        )
    for i, line in enumerate(lines):
        for old, new in replacements:
            line = line.replace(old, new)
        if '=' in line:
            k, v = line.split('=', 1)
            if k.strip() == 'source_url':
                source_url = v.strip()
        lines[i] = line

    # update source hash
    resp = requests.get(source_url, stream=True, headers={
        'User-Agent': 'wrapdb/0',
    })
    resp.raise_for_status()
    hash = sha256()
    while True:
        buf = resp.raw.read(1 << 20)
        if not buf:
            break
        hash.update(buf)
    for i, line in enumerate(lines):
        if '=' in line:
            k, v = line.split('=', 1)
            if k.strip() == 'source_hash':
                lines[i] = f'source_hash = {hash.hexdigest()}\n'
                break

    # write
    with path.open('w', encoding='utf-8') as f:
        f.write(''.join(lines))


def update_revisions(args: Namespace) -> None:
    # run queries
    releases = Releases.load()
    cur_vers = get_wrap_versions()

    # decide what to update
    names: list[str] = args.names
    if names:
        for name in names:
            if name not in cur_vers:
                raise ValueError(f'{name} is not a valid wrap in releases.json')
    else:
        names = [name for name in cur_vers]

    # update
    for name in names:
        print(f'Updating {name} revision...')
        cur_rev = int(releases[name]['versions'][0].split('-')[1])
        releases[name]['versions'].insert(0, f'{cur_vers[name]}-{cur_rev + 1}')
    releases.save()


def do_autoupdate(args: Namespace) -> None:
    # --revision is distinct functionality; handle it separately
    if args.revision:
        return update_revisions(args)

    # run queries
    releases = Releases.load()
    cur_vers = get_wrap_versions()
    upstream_vers = get_upstream_versions()
    ports = get_port_wraps()

    # decide what to update
    names: list[str] = args.names
    if names:
        for name in names:
            if name not in upstream_vers:
                raise ValueError(f'{name} is not tracked in Anitya; upstream version is unknown')
            if name in ports and not args.port:
                raise ValueError(f'{name} upstream does not use Meson; cannot update automatically. Use -p/--port to update everything but the packagefiles.')
    else:
        names = [name for name in cur_vers if name in upstream_vers]
        if not args.port:
            names = [name for name in names if name not in ports]

    # update
    failures = 0
    for name in names:
        cur_ver, upstream_ver = cur_vers[name], upstream_vers[name]
        try:
            if cur_ver != upstream_ver:
                if name in ports:
                    # manual packagefiles changes will also be needed
                    print(f'Updating {name}.wrap and releases.json...')
                else:
                    print(f'Updating {name}...')
                update_wrap(name, cur_ver, upstream_ver)
                releases[name]['versions'].insert(0, f'{upstream_ver}-1')
                releases.save()
        except Exception as e:
            print(e, file=sys.stderr)
            failures += 1
    if failures:
        raise Exception(f"Couldn't update {failures} wraps")


def do_commit(args: Namespace) -> None:
    old_releases = get_commit_releases('HEAD')
    new_releases = Releases.load()

    # we don't validate any invariants checked by sanity_checks.py
    changed_wraps = [
        name for name in new_releases
        if old_releases.get(name) != new_releases[name]
    ]
    if not changed_wraps:
        raise ValueError('Found no changes to releases.json')
    if len(changed_wraps) != 1:
        raise ValueError(f'Can only commit one wrap at a time: {changed_wraps}')
    name = changed_wraps[0]

    if not args.message:
        new_ver = new_releases[name]['versions'][0]
        try:
            old_ver = old_releases[name]['versions'][0]
        except KeyError:
            old_ver = None
        if old_ver is None:
            args.message = 'add'
        elif old_ver != new_ver and new_ver.endswith('-1'):
            args.message = f'update from {old_ver.split("-")[0]} to {new_ver.split("-")[0]}'
        else:
            raise ValueError("Can't autogenerate commit message; specify -m")

    commit_files: list[str | Path] = [
        'ci_config.json', 'releases.json', wrap_path(name)
    ]
    patch_dir = read_wrap(name).get(
        'wrap-file', 'patch_directory', fallback=None
    )
    if patch_dir:
        commit_files.append(f'subprojects/packagefiles/{patch_dir}')

    # suppress Git summary output and recreate it ourselves so we can also
    # show the diffstat, to confirm we've committed the right files
    cmd: list[str | Path] = [
        'git', 'commit', '-m', f'{name}: {args.message}', '-q'
    ]
    subprocess.check_call(cmd + commit_files)
    subprocess.check_call(['git', 'log', '-1', '--format=[%h] %s'])
    subprocess.check_call(['git', 'diff', '--stat', 'HEAD^..HEAD'])


def do_libtool_ver(args: Namespace) -> None:
    components = args.info.split(':', 2)
    components += ['0'] * (3 - len(components))
    current, revision, age = (int(c) for c in components)
    print(f'{current - age}.{age}.{revision}')


def do_list(args: Namespace) -> None:
    # set default flags
    if not any((args.official, args.port)):
        args.official = args.port = True
    if not any((args.current, args.update, args.untracked)):
        args.current = args.update = args.untracked = True

    # build list
    names = set(args.names)
    cur_vers = get_wrap_versions()
    upstream_vers = get_upstream_versions()
    ports = get_port_wraps()
    wraps = []
    for name in cur_vers:
        if names and name not in names:
            # user isn't interested in this wrap
            continue
        if name in ports:
            if not args.port:
                continue
        else:
            if not args.official:
                continue
        if name in upstream_vers:
            if cur_vers[name] == upstream_vers[name]:
                if not args.current:
                    continue
            else:
                if not args.update:
                    continue
        else:
            if not args.untracked:
                continue
        wraps.append(name)

    # report
    if args.github:
        print('matrix=', end='')
        json.dump(
            {
                "include": [
                    {
                        'wrap': name,
                        'old-version': cur_vers[name],
                        'new-version': upstream_vers.get(name),
                    } for name in wraps
                ]
            },
            sys.stdout,
        )
        print()
    elif args.json:
        json.dump(
            {
                name: {
                    'wrapdb': cur_vers[name],
                    'upstream': upstream_vers.get(name),
                    'port': name in ports,
                    'source': read_wrap(name).get(
                        'wrap-file', 'source_url'
                    )
                } for name in wraps
            }, sys.stdout, indent=2, sort_keys=True
        )
        print()
    elif args.markdown:
        print('| Type | Wrap | WrapDB Version | Upstream Version |')
        print('| --- | --- | --- | --- |')
        for name in wraps:
            typ = ':construction:' if name in ports else ':bank:'
            fname = f'[{name}]({WRAP_URL_TEMPLATE.format(name)})'
            if name not in upstream_vers:
                upstream_ver = '_unknown_'
            elif cur_vers[name] != upstream_vers[name]:
                upstream_ver = f'**{upstream_vers[name]}**'
            else:
                upstream_ver = upstream_vers[name]
            print(
                f'| {typ} | {fname} | {cur_vers[name]} | {upstream_ver} |'
            )
        if not wraps:
            print('| _none_ | | | |')
    else:
        for name in wraps:
            official = '*' if name not in ports else ' '
            line = f'{official} {name:25} {cur_vers[name]:>15}'
            if name not in upstream_vers:
                line += '  =>|'
            elif cur_vers[name] != upstream_vers[name]:
                line += f'  => {upstream_vers[name]:>15}'
            print(line)


def main() -> None:
    parser = ArgumentParser(
        prog='versions.py',
        description='Manage wrap versions.'
    )
    subparsers = parser.add_subparsers(metavar='subcommand', required=True)

    autoupdate = subparsers.add_parser(
        'autoupdate',
        aliases=['au'],
        help='automatically update wraps',
        description="Automatically update wraps that support Meson upstream, update metadata only (releases.json and *.wrap) for wraps that don't, or increment wrap revision in releases.json."
    )
    autoupdate.add_argument(
        'names', metavar='name', nargs='*', help='wrap to update'
    )
    autoupdate.add_argument(
        '-p', '--port', action='store_true',
        help='allow updating metadata for wraps without upstream Meson support',
    )
    autoupdate.add_argument(
        '-r', '--revision', action='store_true',
        help='increment wrap revision and do nothing else'
    )
    autoupdate.set_defaults(func=do_autoupdate)

    commit = subparsers.add_parser(
        'commit',
        aliases=['com'],
        help='commit a wrap update to Git',
        description='Commit a wrap update to Git.',
    )
    commit.add_argument(
        '-m', '--message', metavar='text',
        help='commit message, without wrap name prefix'
    )
    commit.set_defaults(func=do_commit)

    libtool_ver = subparsers.add_parser(
        'libtool-ver',
        aliases=['ltv'],
        help='calculate library version from libtool version-info',
        description='Calculate library version number from libtool version-info.',
    )
    libtool_ver.add_argument(
        'info', metavar='version-info', help='libtool current:revision:age'
    )
    libtool_ver.set_defaults(func=do_libtool_ver)

    list = subparsers.add_parser(
        'list',
        aliases=['ls'],
        help='list wraps and their versions',
        description='List wraps and their versions.',
    )
    list.add_argument(
        'names', metavar='name', nargs='*', help='wrap to check'
    )
    group = list.add_argument_group('filter on upstream Meson support')
    group.add_argument(
        '-o', '--official', action='store_true',
        help='only list wraps with Meson support upstream'
    )
    group.add_argument(
        '-p', '--port', action='store_true',
        help='only list wraps with Meson support added in wrapdb'
    )
    group = list.add_argument_group('filter on update status')
    group.add_argument(
        '-c', '--current', action='store_true',
        help='only list wraps without new upstream release'
    )
    group.add_argument(
        '-u', '--update', action='store_true',
        help='only list wraps with new upstream release'
    )
    group.add_argument(
        '-x', '--untracked', action='store_true',
        help='only list wraps whose upstream version is not tracked'
    )
    group = list.add_argument_group('output format')
    xgroup = group.add_mutually_exclusive_group()
    xgroup.add_argument(
        '-g', '--github', action='store_true',
        help='output GitHub Actions matrix'
    )
    xgroup.add_argument(
        '-j', '--json', action='store_true', help='output JSON'
    )
    xgroup.add_argument(
        '-m', '--markdown', action='store_true', help='output Markdown table'
    )
    list.set_defaults(func=do_list)

    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
