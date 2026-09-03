project(
  'picohttpparser',
  'c',
  meson_version: '>=0.56.0',
  version: '1.2',
  license: 'MIT OR Artistic-1.0-Perl OR GPL-1.0-or-later',
)

lib_pico = library(
  'picohttpparser',
  'picohttpparser.c',
  vs_module_defs: 'picohttpparser.def',
  install: true,
)

dep_pico = declare_dependency(
  include_directories: include_directories('.'),
  link_with: lib_pico,
)

meson.override_dependency('picohttpparser', dep_pico)
