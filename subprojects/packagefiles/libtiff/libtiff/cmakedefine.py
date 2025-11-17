#!/usr/bin/env python3

import re, sys

with open(sys.argv[1], encoding='utf-8') as f:
    contents = f.read()
with open(sys.argv[2], 'w', encoding='utf-8') as f:
    f.write(re.sub('# +cmakedefine', '#cmakedefine', contents))
