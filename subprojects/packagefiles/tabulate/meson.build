project(
  'tabulate',
  'cpp',
  version: '1.5',
  license: 'MIT',
)

includes = include_directories(['single_include', 'include'])

tabulate_dep = declare_dependency(
  include_directories: includes,
)

install_headers(
  [
    'include/tabulate/asciidoc_exporter.hpp',
    'include/tabulate/cell.hpp',
    'include/tabulate/color.hpp',
    'include/tabulate/column.hpp',
    'include/tabulate/column_format.hpp',
    'include/tabulate/exporter.hpp',
    'include/tabulate/font_align.hpp',
    'include/tabulate/font_style.hpp',
    'include/tabulate/format.hpp',
    'include/tabulate/latex_exporter.hpp',
    'include/tabulate/markdown_exporter.hpp',
    'include/tabulate/optional_lite.hpp',
    'include/tabulate/printer.hpp',
    'include/tabulate/row.hpp',
    'include/tabulate/string_view_lite.hpp',
    'include/tabulate/table.hpp',
    'include/tabulate/table_internal.hpp',
    'include/tabulate/termcolor.hpp',
    'include/tabulate/utf8.hpp',
    'include/tabulate/variant_lite.hpp',
    'single_include/tabulate/tabulate.hpp',
  ],
  subdir: 'tabulate',
)
