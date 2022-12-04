#!/usr/bin/env python3

from argparse import ArgumentParser
from pathlib import Path
from subprocess import run
from sys import stdout, stderr
from tempfile import TemporaryDirectory

if __name__ == '__main__':
    parser = ArgumentParser(description='Tests for installed TeX packages')
    parser.add_argument('--pdflatex', type=Path)
    parser.add_argument('package')
    args = parser.parse_args()

    with TemporaryDirectory() as tmp:
        test = Path(f'{tmp}/test.tex')

        with test.open(mode='w', encoding='utf-8') as f:
            f.write('\\documentclass{book}\n')
            f.write('\\usepackage{%s}\n' % args.package)
            f.write('\\begin{document}\n')
            f.write('Hello World.\n')
            f.write('\\end{document}\n')
            f.close()

        run([args.pdflatex, '-interaction', 'batchmode', '-halt-on-error',
            test.absolute()], check=True, stdout=stdout, stderr=stderr, cwd=tmp)
