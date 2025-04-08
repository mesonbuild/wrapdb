#!/bin/sh

exec grep -E '^#define\s+CAP_[A-Z0-9_]+\s+[0-9]+\s*$' "$1" | \
    sed -e 's/^#define\s\+/{"/' \
        -e 's/\s*$/},/' \
        -e 's/\s\+/",/' \
        -e 'y/ABCDEFGHIJKLMNOPQRSTUVWXYZ/abcdefghijklmnopqrstuvwxyz/' \
    >> "$2"
