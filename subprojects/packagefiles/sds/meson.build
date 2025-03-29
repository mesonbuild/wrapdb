project(
  'sds',
  'c',
  version: '2.0.0',
  meson_version: '>=0.49.0',
  license: 'BSD-2-Clause',
)

cc = meson.get_compiler('c')
if cc.get_argument_syntax() == 'msvc'
  error('MSVC is unsupported. sds uses __attribute__ syntax.')
endif

sds_inc = include_directories('.')

sds_lib = library('sds', 'sds.c')

sds_dep = declare_dependency(
  link_with: sds_lib,
  include_directories: sds_inc,
)

if get_option('tests')
  sds_test_exe = executable(
    'hts_endian',
    'sds.c',
    c_args: '-DSDS_TEST_MAIN',
  )

  test('sds_test', sds_test_exe)
endif
