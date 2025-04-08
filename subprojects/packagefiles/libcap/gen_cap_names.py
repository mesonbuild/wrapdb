#!/usr/bin/env python3

import sys
import re

with open(sys.argv[1], 'r') as infile, open(sys.argv[2], 'w') as outfile:
    for line in infile:
        match = re.match(r'^#define\s+(CAP_[A-Z0-9_]+)\s+([0-9]+)\s*$', line)
        if match:
            cap_name = match.group(1).lower()
            cap_value = match.group(2)
            outfile.write(f'{{"{cap_name}", {cap_value}}},\n')
