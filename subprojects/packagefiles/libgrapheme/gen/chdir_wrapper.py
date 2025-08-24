import os, sys, subprocess

os.chdir(os.environ['PROJECT_SOURCE_ROOT'])
subprocess.check_call(sys.argv[1:])
