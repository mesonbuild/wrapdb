#!/usr/bin/env python3

import sys

with open(sys.argv[1], 'r') as f:
    # Skip first line, which is LIBRARY and has a MinGW name
    line = f.readline()
    assert(line.startswith('LIBRARY'))
    with open(sys.argv[2], 'w') as of:
        of.write(f.read())
