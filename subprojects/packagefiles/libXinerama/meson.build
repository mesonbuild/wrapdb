project(
  'libxinerama',
  'c',
  version: '1.1.5',
  default_options: ['warning_level=3'],
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
  dependencies: [x11_dep, xext_dep],
  include_directories: incdirs,
  link_with: xinerama,
)
