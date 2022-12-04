#!/usr/bin/env python3

from argparse import ArgumentParser
from pathlib import Path
from subprocess import run

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('latexmk', type=Path)
    parser.add_argument('src_file', type=Path)
    args = parser.parse_args()

    latexmk = args.latexmk
    src = args.src_file

    run([latexmk, '-pdf', src.name],
        capture_output=True, cwd=src.parent, check=True)
