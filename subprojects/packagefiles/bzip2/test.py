#!/usr/bin/env python3

import subprocess
import argparse
from pathlib import Path
import tempfile
import os
import shlex
import sys


def run_command(command, stdinfile):
    if "MESON_EXE_WRAPPER" in os.environ:
        command = shlex.split(os.environ["MESON_EXE_WRAPPER"]) + command
    with tempfile.TemporaryFile("w+b") as outf:
        with open(stdinfile, "rb") as inf:
            subprocess.run(command, stdin=inf, stdout=outf)
        outf.seek(0)
        return outf.read()


def compare(result, reffile):
    with open(reffile, "rb") as reff:
        return result == reff.read()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("reference", type=Path)
    parser.add_argument("command", nargs="+")
    args = parser.parse_args()

    if not compare(run_command(args.command, args.input), args.reference):
        print("Output did not match reference file!")
        sys.exit(1)
