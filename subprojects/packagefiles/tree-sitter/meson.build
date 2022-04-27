project('tree-sitter', 'c',
  version: '0.15.7',
  license: 'MIT',
  meson_version: '>=0.46.0',
)

tree_sitter = library('tree-sitter', 'lib/src/lib.c',
  include_directories: [
    include_directories('lib/src'),
    include_directories('lib/include'),
    include_directories('lib/utf8proc')
  ],
  soname: '0.0',
  install:true,
)

install_headers('lib/include')

tree_sitter_dep = declare_dependency(
  link_with: tree_sitter,
  include_directories: include_directories('lib/include'),
)


pkg = import('pkgconfig')
pkg.generate(tree_sitter,
             version : '0.15.7',
             name : 'libtree-sitter',
             description : 'An incremental parsing system for programming tools.')
