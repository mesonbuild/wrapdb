project(
  'cwalk',
  'c',
  license: 'MIT',
  version: '1.2.9',
  meson_version: '>= 0.60.0',
)

cwalk_inc = include_directories('include')
default_library = get_option('default_library')

# CWK_SHARED is part of the public interface of the shared library: it makes
# cwalk.h use dllexport/dllimport and default symbol visibility.
if default_library != 'static'
  cwalk_shared_lib = shared_library(
    'cwalk',
    'src/cwalk.c',
    c_args: ['-DCWK_SHARED', '-DCWK_EXPORTS'],
    include_directories: cwalk_inc,
    gnu_symbol_visibility: 'hidden',
    install: true,
  )
  cwalk_dep = declare_dependency(
    compile_args: '-DCWK_SHARED',
    include_directories: cwalk_inc,
    link_with: cwalk_shared_lib,
  )
  meson.override_dependency(
    'cwalk',
    cwalk_dep,
    static: false,
  )
endif

if default_library != 'shared'
  cwalk_static_lib = static_library(
    'cwalk',
    'src/cwalk.c',
    include_directories: cwalk_inc,
    install: true,
  )
  cwalk_static_dep = declare_dependency(
    include_directories: cwalk_inc,
    link_with: cwalk_static_lib,
  )
  meson.override_dependency(
    'cwalk',
    cwalk_static_dep,
    static: true,
  )
  if default_library == 'static'
    cwalk_dep = cwalk_static_dep
  endif
endif

install_headers('include/cwalk.h')

# pkg-config can't select CWK_SHARED per variant, so only set it when the
# shared library is the only one installed
pkg = import('pkgconfig')
pkg.generate(
  default_library == 'static' ? cwalk_static_lib : cwalk_shared_lib,
  extra_cflags: default_library == 'shared' ? ['-DCWK_SHARED'] : [],
)

if get_option('ENABLE_TESTS')
  subdir('test')
endif
