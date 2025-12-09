#!/usr/bin/env python3
import sys
import subprocess

# Get executables from arguments
mtest, mtest_opponent = sys.argv[1:3]

# Get iteration count from command line (default 1000)
iterations = sys.argv[3] if len(sys.argv) > 3 else '1000'

# Run mtest and pipe its output to mtest_opponent
mtest_proc = subprocess.Popen([mtest, iterations], stdout=subprocess.PIPE)
mtest_opponent_proc = subprocess.Popen([mtest_opponent], stdin=mtest_proc.stdout)

# Close mtest stdout in parent to allow proper SIGPIPE handling
mtest_proc.stdout.close()

# Wait for both processes to complete
mtest_opponent_proc.wait()
mtest_proc.wait()

# Exit with mtest_opponent's exit code (standard pipe behavior)
sys.exit(mtest_opponent_proc.returncode)
