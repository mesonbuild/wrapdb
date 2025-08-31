#!/usr/bin/env python3

# Copyright 2025 Benjamin Gilbert <bgilbert@backtick.net>

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
from argparse import ArgumentParser
from hashlib import sha256
import json
from pathlib import Path
import subprocess

from utils import read_wrap, write_wrap, wrap_path

class Internalizer:
    def __init__(self, all=False):
        with open('releases.json') as fh:
            releases = json.load(fh)
        tags = set(
            subprocess.check_output(['git', 'tag'], text=True).splitlines()
        )

        self.download = []
        self.rewrite = {}
        for name, info in releases.items():
            tag = f'{name}_{info["versions"][0]}'
            if all or tag not in tags:
                self.download.append(name)
            else:
                self.rewrite[name] = tag

    def get_cache_key(self) -> str:
        hash = sha256()
        for name in self.download:
            wrap = read_wrap(name)
            wf = wrap['wrap-file']
            parts = [
                name,
                wf['source_url'],
                wf.get('source_fallback_url', ''),
                wf['source_filename'],
                wf['source_hash'],
                '=====',
            ]
            for s in parts:
                hash.update(s.encode() + b'\0')
        return hash.hexdigest()[:16]

    def download_sources(self) -> None:
        if self.download:
            subprocess.check_call(
                ['meson', 'subprojects', 'download'] + self.download
            )
        else:
            Path('subprojects', 'packagecache').mkdir(exist_ok=True)

    def rewrite_wraps(self) -> None:
        for name, tag in self.rewrite.items():
            wrap = read_wrap(name)
            wf = wrap['wrap-file']
            wf['source_fallback_url'] = wf['source_url']
            wf['source_url'] = f'https://github.com/mesonbuild/wrapdb/releases/download/{tag}/{wf["source_filename"]}'
            write_wrap(wrap_path(name), wrap)
        print(f'Rewrote source_url for {len(self.rewrite)} projects.')


def main() -> None:
    common = ArgumentParser(add_help=False)
    common.add_argument(
        '-a', '--all', action='store_true', help='select all projects'
    )

    parser = ArgumentParser(
        prog='internalize_sources.py',
        description='CI tool for avoiding unnecessary downloads of upstream source archives.',
    )
    subparsers = parser.add_subparsers(metavar='subcommand', required=True)

    cache_key = subparsers.add_parser(
        'cache-key', parents=[common], help='generate cache key'
    )
    cache_key.set_defaults(op='cache-key')

    download = subparsers.add_parser(
        'download', parents=[common], help='download sources for modified wraps'
    )
    download.set_defaults(op='download')

    rewrite = subparsers.add_parser(
        'rewrite', parents=[common],
        help='redirect unmodified wraps to WrapDB GitHub releases'
    )
    rewrite.set_defaults(op='rewrite')

    args = parser.parse_args()
    intern = Internalizer(args.all)
    if args.op == 'cache-key':
        print(intern.get_cache_key())
    elif args.op == 'download':
        intern.download_sources()
    elif args.op == 'rewrite':
        intern.rewrite_wraps()


if __name__ == '__main__':
    main()
