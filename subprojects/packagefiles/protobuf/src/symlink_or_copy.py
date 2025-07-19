#!/usr/bin/env python3

"""
Helper-script, a replacement to unix
`ln -s [source] [destination] || cp -r [source] [destination]` command
should work everywhere where meson does
"""

import argparse
import os
import platform
import shutil
import sys
from pathlib import Path


def main() -> int:
    """Your script main entry point"""

    parser = argparse.ArgumentParser()
    parser.add_argument("source")
    parser.add_argument("destination")
    args = parser.parse_args()

    source = Path(args.source)
    destination = Path(args.destination)
    destination_parent = destination.absolute().parent

    if not source.exists():
        print("Source not found at:", source.absolute())
        return -2
    if not destination_parent.exists():
        print("Destination directory not found at:", destination_parent)
        return -3

    relative_target = Path(os.path.relpath(source.absolute(), destination_parent))
    print(f"creating symlink {destination} -> {relative_target}")
    if destination.is_symlink():
        destination.unlink()
    elif destination.is_dir():
        shutil.rmtree(destination)
    try:
        destination.symlink_to(relative_target, target_is_directory=source.is_dir())
    except OSError as exc:
        # 1314: A required privilege is not held by the client.
        # Windows raises these errors when the script doesn't have
        # sufficient (administrator) priviledges and Developer mode
        # is not enabled (which enables regular users to create
        # symlinks).
        if platform.system() == "Windows" and exc.winerror == 1314:
            try:
                shutil.copytree(source, destination)
            except (FileNotFoundError, NotADirectoryError, PermissionError) as exc:
                print(exc, file=sys.stderr)
                return -4
        else:
            print(exc, file=sys.stderr)
            return -4
    except (FileNotFoundError, PermissionError) as exc:
        print(exc, file=sys.stderr)
        return -4

    return 0


if __name__ == "__main__":
    sys.exit(main())
