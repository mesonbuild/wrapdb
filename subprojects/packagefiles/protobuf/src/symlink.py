#!/usr/bin/env python3

"""
Helper-script, a replacement to unix `ln -s [target] [alias]` command
should work everywhere where meson does
"""

import os
import sys
from pathlib import Path


def main(argv: [str]) -> int:
    """Your script main entry point"""

    if len(sys.argv) != 3:
        print(f"Usage: {argv[0]} [target] [alias]")
        return -1

    target = Path(sys.argv[1])
    alias = Path(sys.argv[2])
    alias_dir = alias.absolute().parent

    if not target.exists():
        print("Target not found at:", target.absolute())
        return -2
    if not alias_dir.exists():
        print("Alias directory not found at:", alias_dir)
        return -3

    rtarget = Path(os.path.relpath(target.absolute(), alias_dir))
    print(f"creating symlink {alias} -> {rtarget}")
    if alias.is_symlink():
        alias.unlink()
    alias.symlink_to(rtarget, target_is_directory=target.is_dir())

    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
