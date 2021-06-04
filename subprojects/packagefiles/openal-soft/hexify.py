#!/usr/bin/env python3

import os, sys

ifile = sys.argv[1]
ofile = sys.argv[2]
varname = sys.argv[3]

bs = open(ifile, 'rb').read()
with open(ofile, 'w') as of:
    of.write(f'const unsigned char {varname}[] = {{\n')
    for b in bs:
        hex_value = hex(b)
        of.write(f'    {hex_value},\n')
    of.write('};')
