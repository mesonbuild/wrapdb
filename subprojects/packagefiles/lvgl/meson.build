project(
  'lvgl',
  'c',
  'cpp',
  default_options: ['default_library=static'],
  license: 'MIT',
  meson_version: '>= 0.54.0',
  version: '9.4.0',
)

subdir('src')
if get_option('CONFIG_LV_BUILD_DEMOS')
  subdir('demos')
endif
if get_option('CONFIG_LV_BUILD_EXAMPLES')
  subdir('examples')
endif
