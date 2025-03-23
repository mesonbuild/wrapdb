project(
  'libXext',
  'c',
  version: '1.3.5',
  default_options: ['warning_level=3'],
)

incdirs = include_directories('.', 'include')

x11_dep = dependency('x11')

xext = library(
  'Xext',
  'src/DPMS.c',
  'src/MITMisc.c',
  'src/XAppgroup.c',
  'src/XLbx.c',
  'src/XEVI.c',
  'src/XMultibuf.c',
  'src/XSecurity.c',
  'src/XShape.c',
  'src/XShm.c',
  'src/XSync.c',
  'src/XTestExt1.c',
  'src/Xcup.c',
  'src/Xdbe.c',
  'src/Xge.c',
  'src/extutil.c',
  'src/globals.c',
  'src/reallocarray.c',
  dependencies: x11_dep,
  include_directories: incdirs,
  install: true,
)

xext_dep = declare_dependency(
  dependencies: x11_dep,
  include_directories: incdirs,
  link_with: xext,
)
