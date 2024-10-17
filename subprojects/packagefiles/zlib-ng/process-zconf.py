#!/usr/bin/python3

import argparse
import re
import sys

parser = argparse.ArgumentParser()
parser.add_argument('--have-unistd', action='store_true')
parser.add_argument('--ptrdiff-type')
parser.add_argument(
    'file', type=argparse.FileType('r'), nargs='?', default=sys.stdin
)
args = parser.parse_args()

unistd = f'#if {int(bool(args.have_unistd))}  /* set by Meson */'
unistd_regex = re.compile('^#ifdef HAVE_UNISTD_H.*')
ptrdiff_regex = re.compile('^#ifdef NEED_PTRDIFF_T.*')

for line in args.file:
    line = unistd_regex.sub(unistd, line)
    if args.ptrdiff_type:
        line = ptrdiff_regex.sub('#if 1  /* set by Meson */', line)
        line = line.replace(
            'typedef PTRDIFF_TYPE', f'typedef {args.ptrdiff_type}'
        )
    print(line, end='')
