#!/usr/bin/env python3

import re, sys

tests = []
for path in sys.argv[1:]:
    with open(path, encoding='utf-8') as f:
        for line in f:
            if line.startswith('DEFINE_TEST('):
                tests.append(line)
print(''.join(sorted(tests)), end='')
