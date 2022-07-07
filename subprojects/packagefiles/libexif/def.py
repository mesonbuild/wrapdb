#!/usr/bin/env python3

import os, sys

ifile = sys.argv[1]
ofile = sys.argv[2]

bs = open(ifile, 'r').read()
with open(ofile, 'w') as of:
    of.write(f'EXPORTS\n;\n')
    of.write(bs)
