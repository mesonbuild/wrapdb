project(
  'box2d',
  'cpp',
  version: '2.4.1',
  license: 'zlib',
  meson_version: '>=0.49.0',
)

incdir = include_directories('include')
box2d_compile_args = []
if get_option('buildtype') != 'static'
  box2d_compile_args += '-DB2_SHARED'
  box2d_compile_args += '-Dbox2d_EXPORTS'
endif

subdir('src')

box2d_dep = declare_dependency(
  link_with: box2d_lib,
  include_directories: incdir,
  version: meson.project_version(),
)

doctest_dep = dependency(
  'doctest',
  required: false,
)
if doctest_dep.found()
  subdir('unit-test')
endif
