webpmux_lib = library(
  'webpmux',
  ['anim_encode.c', 'muxedit.c', 'muxinternal.c', 'muxread.c'],
  dependencies: [build_libwebpmux, common_deps, webp_dep],
  gnu_symbol_visibility: 'hidden',
  install: true,
  version: '3.1.2',
)

webpmux_dep = declare_dependency(
  dependencies: webp_dep,
  include_directories: include_directories('.'),
  link_with: webpmux_lib,
)

meson.override_dependency('libwebpmux', webpmux_dep)

pkg.generate(
  webpmux_lib,
  description: 'Library for manipulating the WebP graphics format container',
  name: 'libwebpmux',
)
