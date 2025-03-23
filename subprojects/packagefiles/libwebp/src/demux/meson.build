webpdemux_lib = library(
  'webpdemux',
  ['anim_decode.c', 'demux.c'],
  dependencies: [build_libwebpdemux, common_deps, webp_dec_dep],
  gnu_symbol_visibility: 'hidden',
  install: true,
  version: '2.0.14',
)

webpdemux_dep = declare_dependency(
  dependencies: webp_dec_dep,
  include_directories: include_directories('.'),
  link_with: webpdemux_lib,
)

meson.override_dependency('libwebpdemux', webpdemux_dep)

pkg.generate(
  webpdemux_lib,
  description: 'Library for parsing the WebP graphics format container',
  name: 'libwebpdemux',
)
