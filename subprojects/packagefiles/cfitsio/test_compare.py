#!/usr/bin/env python3

"""
cfitsio instructs the user build test executeables, run them, and then compare
the output to provided reference files. This python file does that in a
portable way integrated into meson's test framework
"""

import sys
from pathlib import Path
import subprocess

test_exe = Path(sys.argv[1])
src_dir = Path(sys.argv[2])
name = test_exe.name.split('.')[0]

input_name = src_dir / (name + ".tpt")
output_ref = src_dir / (name + ".out")
fits_ref = src_dir / (name + ".std")

print(f"input file: {input_name} found : {input_name.is_file()}")
print(f"output reference: {output_ref} found : {output_ref.is_file()}")
print(f"fits reference: {fits_ref} found : {fits_ref.is_file()}")

r = subprocess.run(test_exe.absolute(), cwd=src_dir, capture_output=True)
if r.returncode:
    print(r"test returned non zero: {r.returncode}")
    exit(r.returncode)

out_are_same = r.stdout.splitlines() == open(output_ref, "rb").read().splitlines()
print(f"Outputs are the same: {out_are_same}")
fits_are_same = (
    open(fits_ref, "rb").read() == open(src_dir / (name + ".std"), "rb").read()
)
print(f"Fits are the same: {fits_are_same}")

exit(int(not fits_are_same) * 2 + int(not out_are_same))
