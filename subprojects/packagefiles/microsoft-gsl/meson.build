project(
  'microsoft-gsl',
  'cpp',
  version: '4.2.1',
  license: 'MIT',
  meson_version: '>=0.63.0',
)

subdir('include')

microsoft_gsl_dep = declare_dependency(
  include_directories: gsl_inc,
)

meson.override_dependency('msft_gsl', microsoft_gsl_dep)

pkgconfig = import(
  'pkgconfig',
  required: false,
)

if pkgconfig.found()
  pkgconfig.generate(
    name: 'msft_gsl',
    description: 'Guidelines Support Library',
    url: 'https://github.com/microsoft/GSL',
    install_dir: get_option('datadir') / 'pkgconfig',
  )
endif
