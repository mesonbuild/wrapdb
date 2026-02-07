project(
  'libXext',
  'c',
  version: '1.3.7',
  default_options: ['warning_level=3'],
  # also a Digital Equipment Corporation MIT-like license that doesn't
  # seem to exactly match anything in SPDX
  license: 'HPND-doc AND HPND-doc-sell AND HPND-sell-variant AND ISC AND MIT AND MIT-open-group AND NTP AND SMLNJ AND X11',
  meson_version: '>= 0.56.0',
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
  include_directories: incdirs,
  link_with: xext,
)
meson.override_dependency('xext', xext_dep)
