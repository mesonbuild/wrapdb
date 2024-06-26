project('cwalk', 'c',
  license: 'MIT',
  version: '1.2.9',
  meson_version: '>= 1.3.0'
)

cwalk_inc = include_directories('include')

cwalk = library('cwalk', 'src/cwalk.c',
  install: true,
  include_directories: cwalk_inc,
  gnu_symbol_visibility: 'hidden',
  c_args: '-DCWK_EXPORTS',
  c_shared_args: '-DCWK_SHARED'
)

pkg = import('pkgconfig')
pkg.generate(cwalk)

install_headers('include/cwalk.h')

cwalk_dep = declare_dependency(
  include_directories: 'include',
  link_with: cwalk
)

if get_option('ENABLE_TESTS')
  subdir('test')
endif

