project(
  'libxrandr',
  'c',
  version: '1.5.5',
  default_options: ['warning_level=3'],
  license: 'HPND-sell-variant',
  meson_version: '>= 1.1.0',
)

incdirs = include_directories('include', 'include/X11/extensions')

xext_dep = dependency('xext')
xrender_dep = dependency('xrender')

xrandr = library(
  'Xrandr',
  'src/Xrandr.c',
  'src/XrrConfig.c',
  'src/XrrCrtc.c',
  'src/XrrMode.c',
  'src/XrrMonitor.c',
  'src/XrrOutput.c',
  'src/XrrProperty.c',
  'src/XrrProvider.c',
  'src/XrrProviderProperty.c',
  'src/XrrScreen.c',
  dependencies: [xext_dep, xrender_dep],
  include_directories: incdirs,
  install: true,
)

xrandr_dep = declare_dependency(
  include_directories: incdirs,
  link_with: xrandr,
)
meson.override_dependency('xrandr', xrandr_dep)
