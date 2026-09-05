#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2025 L. E. Segovia <amy@centricular.com>
# SPDX-License-Ref: BSD-3-Clause

from argparse import ArgumentParser
from pathlib import Path
import subprocess
import sys


def parse_key_value_file(path: Path):
    data = {}
    with path.open('r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or ':' not in line:
                continue
            key, value = line.split(':', 1)
            data[key.strip()] = value.strip()
    return data


if __name__ == '__main__':
    parser = ArgumentParser(
        description='Identity version control software version display, also read version files to present x265 version.')
    parser.add_argument('--git', required=False, type=Path)
    parser.add_argument('src_dir', type=Path)
    args = parser.parse_args()

    # Default Settings, for user to be vigilant about x265 version being reported during product build.
    x265_version = 'unknown'
    x265_latest_tag = '0.0'
    x265_tag_distance = '0'
    x265_revision_id = ''

    archive_file = Path(args.src_dir) / 'x265Version.txt'
    git_dir = Path(args.src_dir) / '.git'

    # FIXME UPSTREAM: the original cannot parse shallow clones --Amy
    can_describe_tags = False
    if git_dir.exists() and args.git:
        can_describe_tags = subprocess.run([args.git,
                                            'describe', '--abbrev=0',
                                            '--tags'],
                                           cwd=args.src_dir,
                                           encoding='utf-8',
                                           ).returncode == 0

    if can_describe_tags:
        x265_latest_tag = subprocess.check_output(
            [args.git, 'describe', '--abbrev=0', '--tags'],
            cwd=args.src_dir,
            encoding='utf-8',
        ).strip()
        # Convert “v1.8.0” → “1.8.0”
        if x265_latest_tag.startswith('v'):
            x265_latest_tag = x265_latest_tag[1:]

        x265_tag_distance = subprocess.check_output(
            [args.git, 'rev-list', f'{x265_latest_tag}..',
                '--count', '--first-parent'],
            cwd=args.src_dir,
            encoding='utf-8',
        ).strip()

        x265_revision_id = subprocess.check_output(
            [args.git, 'log', '--pretty=format:%h', '-n', '1'],
            cwd=args.src_dir,
            encoding='utf-8',
        ).strip()
        print("GIT LIVE REPO VERSION RETRIEVED", file=sys.stderr)
    elif archive_file.exists():
        print("SOURCE CODE IS FROM x265 GIT ARCHIVED ZIP OR TAR BALL", file=sys.stderr)
        # Read the lines of the archive summary file to extract the version
        git_meta = parse_key_value_file(archive_file)
        #   releasetag:     1.8.0
        #   releasetagdistance: 2
        #   repositorychangeset: abcdef123456...
        x265_latest_tag = git_meta.get('releasetag', x265_latest_tag)
        x265_tag_distance = git_meta.get(
            'releasetagdistance', x265_tag_distance)
        commit = git_meta.get('repositorychangeset', '')
        if commit:
            x265_revision_id = commit[:9]          # 9‑char abbreviated hash
        print("GIT ARCHIVAL INFORMATION PROCESSED", file=sys.stderr)

    # formatting based on distance from tag
    if x265_tag_distance == '0':
        x265_version = x265_latest_tag
    elif int(x265_tag_distance) > 0:
        x265_version = f'{x265_latest_tag}+{x265_tag_distance}-{x265_revision_id}'

    # will always be printed in its entirety based on version file configuration to avail revision monitoring by repo owners
    print(f'X265_VERSION={x265_version}')
    print(f'X265_LATEST_TAG={x265_latest_tag}')
    print(f'X265_TAG_DISTANCE={x265_tag_distance}')
    print(f"X265 RELEASE VERSION {x265_version}", file=sys.stderr)
