project(
  'miniz',
  'c',
  license: 'mit',
  version: '3.0.1',
  meson_version: '>=0.48.0',
)

install_headers('miniz.h')

if host_machine.system() == 'windows'
  api = get_option('default_library' ) != 'static' ? '-DMINIZ_EXPORT=__declspec(dllexport)' : []
else
  api = '-DMINIZ_EXPORT=__attribute__((visibility("default")))'
endif

miniz_lib = library(
  'miniz',
  'miniz.c',
  c_args: api,
  gnu_symbol_visibility: 'hidden',
  install: true,
)

miniz_inc = include_directories('.')
miniz_dep = declare_dependency(
  include_directories: miniz_inc,
  link_with: miniz_lib,
)

pkg = import('pkgconfig')
pkg.generate(
  miniz_lib,
  name: 'miniz',
  description: 'Single C source file zlib-replacement library',
)

foreach n : ['1', '2', '3', '4', '5']
  executable('example@0@'.format(n), 'examples/example@0@.c'.format(n), dependencies: miniz_dep)
endforeach

cc = meson.get_compiler('c')
m_dep = cc.find_library('m', required: false)
executable('example6', 'examples/example6.c', dependencies: [miniz_dep, m_dep])
