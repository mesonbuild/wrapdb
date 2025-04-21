#!/usr/bin/env python3

import sys

with open(sys.argv[1], 'r') as f, open(sys.argv[2], 'w') as of:
    of.write('{ global:\n')
    for l in f.read().splitlines():
        of.write(f'{l};\n')
    of.write('local: *; };\n')
