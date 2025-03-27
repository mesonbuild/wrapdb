project(
  'dlfcn-win32',
  'c',
  version: '1.4.2',
  meson_version: '>=0.49.0',
)

if host_machine.system() != 'windows'
  error('dlfcn-win32 is only for Windows. All else is unsupported.')
endif

cargs = []
if get_option('default_library') != 'static'
  cargs += '-DDLFCN_WIN32_SHARED'
endif

incdirs = include_directories('src')

dlfcn = library(
  'dl',
  'src/dlfcn.c',
  include_directories: incdirs,
  c_args: cargs,
)

dlfcn_win32_dep = declare_dependency(
  include_directories: incdirs,
  link_with: dlfcn,
)
