#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2025 L. E. Segovia <amy@centricular.com>
# SPDX-License-Ref: BSD-3-Clause

from argparse import ArgumentParser
import pathlib


def output(platform, symbols):
    if platform == 'win':
        print('EXPORTS')
        print(*[f'    {symbol}' for symbol in sorted(set(symbols))], sep='\n')
    elif platform == 'darwin':
        print(*[f'{symbol}' for symbol in sorted(set(symbols))], sep='\n')
    else:
        print('{')
        print('    global:')
        print(
            *[f'        {symbol};' for symbol in sorted(set(symbols))], sep='\n')
        print('    local:')
        print('        *;')
        print('};')


if __name__ == '__main__':
    parser = ArgumentParser(description='Convert Windows .def file to a GNU version script or Mach-O exported symbols list.')
    parser.add_argument('--prefix', metavar='PREFIX',
                            help='Prefix for extern symbols')
    parser.add_argument('--os', type=str, choices=('win', 'linux', 'darwin'),
                            default='linux', required=True,
                            help='Target operating system for the exports file (win = MSVC module definition file, linux = version script, darwin = exported symbols list)')
    parser.add_argument('input', metavar='FILE', type=pathlib.Path, help='Module definition file to parse')

    args = parser.parse_args()

    lines = args.input.open('r', encoding='utf-8').readlines()

    symbols = []
    found_exports = False
    for line in lines:
        stripped = line.strip()
        if not found_exports:
            if stripped.upper().startswith('EXPORTS'):
                found_exports = True
            continue
        # After EXPORTS – ignore blanks or comment lines
        if stripped == '' or stripped.startswith(';'):
            continue
        # Strip inline comments
        symbol = stripped.split(';', 1)[0].strip()
        if symbol:
            symbols.append(symbol)

    if not symbols:
        raise RuntimeError('Error: No symbols found after EXPORTS')

    if args.prefix:
        symbols = [f'_{s}' for s in symbols]

    output(args.os, symbols)
