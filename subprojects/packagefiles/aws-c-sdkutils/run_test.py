#!/usr/bin/env python3

import sys
import os

# Usage: run_test.py <test exe> [args...]
if __name__ == '__main__':
    test_exe = sys.argv[1]
    test_args = sys.argv[2:]
    import subprocess
    result = subprocess.run([test_exe] + test_args, cwd = os.getcwd())
    if result.returncode == 103:
        result.returncode = 77  # Skip code for meson
    sys.exit(result.returncode)
