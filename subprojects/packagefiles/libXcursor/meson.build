project(
  'libXcursor',
  'c',
  version: '1.2.3',
  default_options: ['warning_level=3'],
)

subdir('include/X11/Xcursor')

incdirs = include_directories('.', 'include', 'include/X11/Xcursor')

cfile = configure_file(
  output: 'config.h',
  configuration: {},
)

xrender_dep = dependency('xrender')

xcursor = library(
  'Xcursor',
  'src/cursor.c',
  'src/display.c',
  'src/file.c',
  'src/library.c',
  'src/xlib.c',
  dependencies: xrender_dep,
  include_directories: incdirs,
  install: true,
)

xcursor_dep = declare_dependency(
  dependencies: xrender_dep,
  include_directories: incdirs,
  link_with: xcursor,
)
