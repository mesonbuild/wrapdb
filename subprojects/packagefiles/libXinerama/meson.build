project(
  'libxinerama',
  'c',
  version: '1.1.6',
  default_options: ['warning_level=3'],
  license: 'MIT AND MIT-open-group AND X11',
  meson_version: '>= 1.1.0',
)

incdirs = include_directories('include')

x11_dep = dependency('x11')
xext_dep = dependency('xext')

xinerama = library(
  'Xinerama',
  'src/Xinerama.c',
  dependencies: [x11_dep, xext_dep],
  include_directories: incdirs,
  install: true,
)

xinerama_dep = declare_dependency(
  include_directories: incdirs,
  link_with: xinerama,
)
meson.override_dependency('xinerama', xinerama_dep)
