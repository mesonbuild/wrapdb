#!/usr/bin/env python3

from argparse import ArgumentParser
from pathlib import Path

if __name__ == '__main__':
    parser = ArgumentParser(
        description='Patches the BLOCK "0x040904B0" instruction in .rc files to be Windows compliant')
    parser.add_argument('src_rc', type=Path, help='Source file')
    parser.add_argument('all_rc', type=Path, help='"All" metadata file')
    parser.add_argument('dst_rc', type=Path, help='Destination file')
    parser.add_argument(
        'version', help='Version string in the format major.minor.patch')

    args = parser.parse_args()

    source = args.src_rc.read_text(encoding='utf-8')
    all = args.all_rc.read_text(encoding='utf-8')

    version = f"{','.join(args.version.split('.')[0:2])},0"

    all = all.replace('"0x040904B0"', '"040904B0"') \
        .replace('TH_VERSION_FIELD', version) \
        .replace('TH_VERSION_STRING', f'"{version}"')

    source = source.replace(f'#include "{args.all_rc.name}"', all)

    dest = args.dst_rc
    dest.parent.mkdir(exist_ok=True, parents=True)
    dest.write_text(source, encoding='utf-8')
