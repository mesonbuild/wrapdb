project(
  'libxv',
  'c',
  version: '1.0.11',
)

incdirs = include_directories('include')

x11_dep = dependency('x11')
xext_dep = dependency('xext')

xv = library(
  'Xv',
  'src/Xv.c',
  dependencies: [x11_dep, xext_dep],
  include_directories: incdirs,
  install: true,
)

xv_dep = declare_dependency(
  dependencies: [x11_dep, xext_dep],
  include_directories: incdirs,
  link_with: xv,
)
