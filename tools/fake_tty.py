#!/usr/bin/env python3

import os, pty, sys

os.environ['TERM'] = 'xterm-256color'
sys.exit(os.waitstatus_to_exitcode(pty.spawn(sys.argv[1:])))
