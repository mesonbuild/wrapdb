#!/usr/bin/env python3

import sys

# Usage: generate_tests.py <input test names file> <output C file>
if __name__ == '__main__':
    with open(sys.argv[1], 'r') as test_names:
        tests = [line.strip() for line in test_names if line.strip()]
        with open(sys.argv[2], 'w') as out:
            out.write('/* Auto-generated file, do not edit */\n\n#include <string.h>\n\n')
            for name in tests:
                out.write(f'extern int {name}(int argc, char **argv);\n')
            out.write('\n')
            out.write('int main(int argc, char **argv) {\n')
            for name in tests:
                out.write(f'    if (strcmp(argv[1], "{name}") == 0) return {name}(argc, argv);\n')
            out.write('    return 0;\n')
            out.write('}\n')
