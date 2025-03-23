project(
  'tree-sitter',
  'c',
  version: '0.22.5',
)

src = files(
  'lib/src/alloc.c',
  'lib/src/get_changed_ranges.c',
  'lib/src/language.c',
  'lib/src/lexer.c',
  'lib/src/node.c',
  'lib/src/parser.c',
  'lib/src/query.c',
  'lib/src/stack.c',
  'lib/src/subtree.c',
  'lib/src/tree.c',
  'lib/src/tree_cursor.c',
  'lib/src/wasm_store.c',
)

include_dir = include_directories('lib/include', 'lib/src')

tree_sitter = library(
  'tree-sitter',
  src,
  include_directories: [include_dir],
  install: not meson.is_subproject(),
)

tree_sitter_dep = declare_dependency(
  include_directories: include_dir,
  link_with: tree_sitter,
)

pkg_mod = import('pkgconfig')

pkg_mod.generate(
  tree_sitter,
  name: 'tree-sitter',
  description: 'An incremental parsing system for programming tools',
  libraries: tree_sitter,
  version: meson.project_version(),
)

