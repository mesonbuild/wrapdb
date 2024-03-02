#!/usr/bin/env python3

import binding_generator
import sys

binding_generator.generate_bindings(sys.argv[1], "True", "64", sys.argv[3], sys.argv[2])

