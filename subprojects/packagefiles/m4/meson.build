project(
  'm4',
  'c',
  version: '1.4.19',
  license: 'GPLv3+',
  default_options: ['c_std=c11'],
  meson_version: '>= 0.59.0',  # required for executable(..., win_subsystem: ...)
)

message('updates to the directory work')
subdir('lib')
subdir('src')
if get_option('enable_tests')
  subdir('checks')
endif
