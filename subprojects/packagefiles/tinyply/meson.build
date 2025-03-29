project(
  'tinyply',
  'cpp',
  version: '2.3.4',
  default_options: ['cpp_std=c++11'],
  meson_version: '>=0.46.0',
)
pkg = import('pkgconfig')

i = include_directories('source')
tinyply_lib = library(
  'tinyply',
  'source/tinyply.cpp',
  include_directories: i,
  install: true,
)
install_headers('source/tinyply.h')
tinyply_dep = declare_dependency(
  include_directories: i,
  link_with: tinyply_lib,
)

pkg.generate(
  name: 'tinyply',
  description: 'C++11 ply 3d mesh format importer & exporter',
  libraries: tinyply_lib,
)
