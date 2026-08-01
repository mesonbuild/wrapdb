project(
  'miniz',
  'c',
  license: 'MIT',
  version: '3.1.2',
  meson_version: '>=0.56.0',
)

install_headers('miniz.h')

cc = meson.get_compiler('c')
if host_machine.system() == 'windows'
  add_project_arguments(
    '-D_CRT_SECURE_NO_WARNINGS',
    cc.get_supported_arguments('-Wno-deprecated-declarations'),
    language: 'c',
  )
  api = get_option('default_library') != 'static' ? '-DMINIZ_EXPORT=__declspec(dllexport)' : []
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
meson.override_dependency('miniz', miniz_dep)

pkg = import('pkgconfig')
pkg.generate(
  miniz_lib,
  name: 'miniz',
  description: 'Single C source file zlib-replacement library',
)

if get_option('examples')
  foreach n : ['1', '2', '3', '4', '5']
    executable(
      'example@0@'.format(n),
      'examples/example@0@.c'.format(n),
      dependencies: miniz_dep,
    )
  endforeach

  if cc.links(
    '#include <math.h>\nint main(){log(0);}',
    name: 'log()',
  )
    m_dep = declare_dependency()
  else
    m_dep = cc.find_library('m')
  endif
  executable(
    'example6',
    'examples/example6.c',
    dependencies: [miniz_dep, m_dep],
  )
endif
