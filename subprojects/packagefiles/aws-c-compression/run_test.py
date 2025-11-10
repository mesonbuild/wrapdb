#!/usr/bin/env python3

import sys

# Usage: run_test.py <test exe> [args...]
if __name__ == '__main__':
    test_exe = sys.argv[1]
    test_args = sys.argv[2:]
    import subprocess
    result = subprocess.run([test_exe] + test_args)
    exitcode = result.returncode
    if exitcode == 103:
        exitcode = 77  # Skip code for meson
    sys.exit(exitcode)
