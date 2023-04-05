#!/usr/bin/env python3

"""
This import is to open the files.
"""
import sys

with open(sys.argv[1], 'rb') as bs:
    with open(sys.argv[2], 'w', encoding='utf-8') as of:
        for b in bs.read():
            hex_value = hex(b)
            of.write(f'    {hex_value},\n')
