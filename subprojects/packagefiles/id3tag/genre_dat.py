#!/usr/bin/env python3
# replicate upstream genre.dat.cmake logic

import re
import sys

with open(sys.argv[1], encoding='utf-8') as input:
    genre_li = [line.rstrip('\n') for line in input]

genre_li = [genre for genre in genre_li if re.match(r'^[a-zA-Z]', genre)]

def_strings = []
table_el = []
for genre in genre_li:
    genre_str_name = re.sub(r'[^a-zA-Z0-9]', '_', genre.upper())
    genre_chars = ''.join(f"'{ch}', " for ch in genre)
    def_strings.append(
        f'static id3_ucs4_t const genre_{genre_str_name}[] =\n'
        f'  {{ {genre_chars}0 }}'
    )
    table_el.append(f'  genre_{genre_str_name}')

joined_defs = ';\n'.join(def_strings)
joined_table = ',\n'.join(table_el)

content = (
    f'/* Automatically generated from {sys.argv[1]} */'
    + '\n'
    + '\n'
    + joined_defs
    + ';\n'
    + '\n'
    + 'static id3_ucs4_t const *const genre_table[] = {\n'
    + joined_table
    + '\n'
    + '};\n'
)

with open(sys.argv[2], 'w', encoding='utf-8') as output:
    output.write(content)
