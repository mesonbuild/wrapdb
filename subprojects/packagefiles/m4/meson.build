project(
  'm4',
  'c',
  version: '1.4.19',
  license: 'GPL-3.0-or-later',
  meson_version: '>= 0.56.0',
)

override_opts = ['c_std=c11']

subdir('lib')
subdir('src')
if get_option('enable_tests')
  subdir('checks')
endif
