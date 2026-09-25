project(
  'bearssl',
  'c',
  version: '0.6',
  meson_version: '>=0.56.0',
  license: 'MIT',
  default_options: [
    'warning_level=1',
    'c_std=gnu99,c99',
  ],
)

cc = meson.get_compiler('c')
m_dep = cc.find_library(
  'm',
  required: false,
)

inc = include_directories('inc', 'src')
inc_export = include_directories('inc')

subdir('src')
if get_option('tools')
  subdir('tools')
endif

if get_option('tests')

  t_crypto = executable(
    'testcrypto',
    'test/test_crypto.c',
    include_directories: inc,
    link_with: bearssl_lib,
    dependencies: m_dep,
    build_by_default: false,
  )

  t_speed = executable(
    'testspeed',
    'test/test_speed.c',
    include_directories: inc,
    link_with: bearssl_lib,
    dependencies: m_dep,
    build_by_default: false,
  )

  t_x509 = executable(
    'testx509',
    'test/test_x509.c',
    c_args: ['-DSRCDIRNAME=".."'],
    include_directories: inc,
    link_with: bearssl_lib,
    dependencies: m_dep,
    build_by_default: false,
  )

  test('testcrypto', t_crypto)
  test('testspeed', t_speed)
  test('testx509', t_x509)
endif
