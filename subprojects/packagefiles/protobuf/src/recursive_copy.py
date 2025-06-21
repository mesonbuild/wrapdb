#!/usr/bin/env python3

"""
Helper-script, a replacement to unix `cp -r [source] [destination]` command
should work everywhere where meson does
"""

# This script used to symlink source to destination, but
# creating symlinks in Windows may require administrator
# priviledges or Developer mode enabled.

import sys
import argparse
import shutil


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('source')
    parser.add_argument('destination')
    args = parser.parse_args()

    try:
        shutil.copytree(args.source, args.destination)
    except (FileNotFoundError, NotADirectoryError, PermissionError) as exc:
        print(exc, file=sys.stderr)
        sys.exit(2)
