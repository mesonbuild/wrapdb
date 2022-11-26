#!/usr/bin/env python3

import re

if __name__ == '__main__':
    with open('doc/spec/spec.tex', 'r') as f:
        packages = [x for x in re.findall(
            r'\\usepackage\{(.+)\}', f.read()) if x != "ltablex"]
        for x in packages:
            print(x)
