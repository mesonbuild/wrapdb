project(
  'sqlite3',
  'c',
  license: 'pd',
  version: '3.39.4',
  meson_version: '>=0.48.0',
)

cc = meson.get_compiler('c')
if meson.version().version_compare('>= 0.62.0')
  libdl = dependency('dl', required: false)
else
  libdl = cc.find_library('dl', required: false)
endif
libm = cc.find_library('m', required: false)

if host_machine.system() == 'windows'
  sqlite_args = '-DSQLITE_API=@0@'.format(get_option('default_library') != 'static' ? '__declspec(dllexport)' : '""')
else
  sqlite_args = '-DSQLITE_API=__attribute__((visibility("default")))'
endif

libsqlite3 = library(
  'sqlite3',
  'sqlite3.c',
  c_args: sqlite_args,
  dependencies: [libdl, libm, dependency('threads')],
  install: true,
  gnu_symbol_visibility: 'hidden',
  # ABI compatibility with autotools/libtool
  version: '0.8.6',
)

if host_machine.system() == 'windows'
  sqlite_args = '-DSQLITE_API=@0@'.format(get_option('default_library') != 'static' ? '__declspec(dllimport)' : '""')
else
  sqlite_args = '-DSQLITE_API=__attribute__((visibility("default")))'
endif

sqlite3_dep = declare_dependency(
  compile_args: sqlite_args,
  include_directories: '.',
  link_with: libsqlite3,
)

install_headers('sqlite3.h')

pkgconfig = import('pkgconfig')
pkgconfig.generate(
  libsqlite3,
  description: 'An embedded SQL database engine',
  version: meson.project_version(),
)
