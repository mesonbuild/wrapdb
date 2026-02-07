project(
  'libXxf86vm',
  'c',
  version: '1.1.7',
  license: 'X11',
  meson_version: '>= 1.1.0',
)

if host_machine.system() == 'windows'
  error('Windows is unsupported. libXxf86vm requires POSIX')
endif

incdirs = include_directories('include')

x11_dep = dependency('x11')
xext_dep = dependency('xext')

xxf86vm = library(
  'Xxf86vm',
  'src/XF86VMode.c',
  dependencies: [x11_dep, xext_dep],
  include_directories: incdirs,
  install: true,
)

xxf86vm_dep = declare_dependency(
  include_directories: incdirs,
  link_with: xxf86vm,
)
meson.override_dependency('xxf86vm', xxf86vm_dep)
