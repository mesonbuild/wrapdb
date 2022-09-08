project('sqlite3', 'c', license: 'pd', version: '3.39.3', meson_version: '>=0.46.0')

cc = meson.get_compiler('c')
if meson.version().version_compare('>= 0.62.0')
  libdl = dependency('dl', required: false)
else
  libdl = cc.find_library('dl', required: false)
endif
libm = cc.find_library('m', required: false)

sqlite_args = []
# On Windows/MinGW, we need to define -DSQLITE_API=__declspec(dllexport)
# If not the .lib will not be generated
if host_machine.system() == 'windows' and 'static' != get_option('default_library')
    sqlite_args += ['-DSQLITE_API=__declspec(dllexport)']
endif

libsqlite3 = library(
    'sqlite3',
    'sqlite3.c',
    c_args: sqlite_args,
    dependencies: [libdl, libm, dependency('threads')],
    install: true,
    # ABI compatibility with autotools/libtool
    version: '0.8.6',
)

install_headers('sqlite3.h')

sqlite3_dep = declare_dependency(
    include_directories: include_directories('.'),
    link_with: libsqlite3,
)

pkgconfig = import('pkgconfig')
pkgconfig.generate(
    libsqlite3,
    description: 'An embedded SQL database engine',
    version: meson.project_version(),
)
