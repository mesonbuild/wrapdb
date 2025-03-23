gumbo_lib = library(
  'gumbo',
  [
    'attribute.c',
    'char_ref.c',
    'error.c',
    'parser.c',
    'string_buffer.c',
    'string_piece.c',
    'tag.c',
    'tokenizer.c',
    'utf8.c',
    'util.c',
    'vector.c',
  ],
  include_directories: (host_machine.system() == 'windows' and not cc.has_header(
    'strings.h',
  ) ? include_directories(
    '../visualc/include',
  ) : []),
  install: true,
  version: '2.0.0',
  vs_module_defs: 'gumbo.def',
)

gumbo_dep = declare_dependency(
  include_directories: include_directories('.'),
  link_with: gumbo_lib,
)
meson.override_dependency('gumbo', gumbo_dep)

pkg = import('pkgconfig')
pkg.generate(
  gumbo_lib,
  description: 'A fully-compliant HTML5 parser.',
)

install_headers('gumbo.h', 'tag_enum.h')
