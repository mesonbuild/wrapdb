#!/usr/bin/env python3

import re, sys

for path in sys.argv[1:]:
    with open(path, encoding='utf-8') as f:
        for line in f:
            if line.startswith('DEFINE_TEST'):
                print(line, end='')
