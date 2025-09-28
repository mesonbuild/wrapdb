#!/usr/bin/env python3

import os, pty, sys

os.environ['TERM'] = 'xterm-256color'
status = pty.spawn(sys.argv[1:])
if sys.version_info >= (3, 9):
    sys.exit(os.waitstatus_to_exitcode(status))
else:
    # just check for success or failure
    sys.exit(0 if os.WIFEXITED(status) and not os.WEXITSTATUS(status) else 1)
