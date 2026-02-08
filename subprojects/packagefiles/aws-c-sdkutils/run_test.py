#!/usr/bin/env python3

import sys

# Usage: run_test.py <test exe> [args...]
if __name__ == '__main__':
    test_exe = sys.argv[1]
    test_args = sys.argv[2:]
    import subprocess
    result = subprocess.run([test_exe] + test_args)
    if result == 103:
        result = 77  # Skip code for meson
    sys.exit(result.returncode)
