project(
  'lvgl',
  'c',
  'cpp',
  default_options: ['default_library=static'],
  license: 'MIT',
  meson_version: '>= 0.52.0',
  version: '9.3.0',
)

subdir('src')
if not get_option('LV_CONF_BUILD_DISABLE_DEMOS')
  subdir('demos')
endif
if not get_option('LV_CONF_BUILD_DISABLE_EXAMPLES')
  subdir('examples')
endif
