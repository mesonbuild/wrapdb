#!/usr/bin/python3

import argparse
import os
from pathlib import Path
import re

parser = argparse.ArgumentParser()
parser.add_argument('type', choices=['zlib', 'zlib-ng'])
args = parser.parse_args()

if args.type == 'zlib':
    regex = re.compile('#define ZLIB_VERSION "([0-9.]+)\\.zlib-ng"$')
else:
    regex = re.compile('#define ZLIBNG_VERSION "([0-9.]+)"$')

zlib_h_in = (
    Path(os.environ['MESON_SOURCE_ROOT']) /
    os.environ['MESON_SUBDIR'] /
    'zlib.h.in'
)
for line in zlib_h_in.open():
    match = regex.match(line)
    if match:
        print(match.group(1))
        break
else:
    raise Exception('Specified version not found in ' + zlib_h_in.as_posix())
