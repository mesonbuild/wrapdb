#!/usr/bin/env python3
'''
Python script which chdirs to specified directory and executes program.

See https://github.com/mesonbuild/meson/discussions/10390
'''

import sys
import os

if len(sys.argv) < 2:
    print('Directory to cd to must be specified as first argument!', file=sys.stderr)
    sys.exit(1)
if len(sys.argv) == 2:
    print('No command to execute specified!', file=sys.stderr)
    sys.exit(1)

try:
    os.chdir(sys.argv[1])
except OSError as exc:
    print(f'Couldn\'t chdir into \'{sys.argv[1]}\': {exc}', file=sys.stderr)
    sys.exit(1)

try:
    os.execvp(sys.argv[2], sys.argv[2:])
except OSError as exc:
    print(exc, file=sys.stderr)
    sys.exit(1)
