#!/usr/bin/env python3

from argparse import ArgumentParser
from pathlib import Path

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('doxyfile_in', type=Path)
    parser.add_argument('doxyfile_out', type=Path)
    parser.add_argument('output_directory', type=Path)
    args = parser.parse_args()

    doxyfile_in: Path = args.doxyfile_in
    src_contents = doxyfile_in \
        .read_text(encoding='utf-8') \
        .replace('OUTPUT_DIRECTORY       = libtheora',
                 f'OUTPUT_DIRECTORY       = {args.output_directory}')

    doxyfile_out: Path = args.doxyfile_out
    doxyfile_out.write_text(src_contents, encoding='utf-8')
