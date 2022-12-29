#!/usr/bin/env python3

"""Module providing file I/O"""
import sys

with open(sys.argv[1], 'r', encoding="utf-8") as inputfile:
    bs = inputfile.read()

with open(sys.argv[2], 'w', encoding="utf-8") as of:
    of.write('EXPORTS\n;\n')
    of.write(bs)
