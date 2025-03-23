project(
  'libxrender',
  'c',
  version: '0.9.10',
  default_options: ['warning_level=3'],
)

incdirs = include_directories('.', 'include', 'include/X11/extensions/')

config_h = configure_file(
  output: 'config.h',
  configuration: {},
)

x11_dep = dependency('x11')

xrender = library(
  'xrender',
  'src/AddTrap.c',
  'src/Color.c',
  'src/Composite.c',
  'src/Cursor.c',
  'src/FillRect.c',
  'src/FillRects.c',
  'src/Filter.c',
  'src/Glyph.c',
  'src/Picture.c',
  'src/Poly.c',
  'src/Trap.c',
  'src/Tri.c',
  'src/Xrender.c',
  dependencies: x11_dep,
  include_directories: incdirs,
  install: true,
)

xrender_dep = declare_dependency(
  dependencies: x11_dep,
  include_directories: incdirs,
  link_with: xrender,
)
