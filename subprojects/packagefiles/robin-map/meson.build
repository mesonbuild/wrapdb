project(
  'robin-map',
  'cpp',
  version: '1.4.1',
  license: 'MIT',
  meson_version: '>=0.56.0',
)

robin_map_inc = include_directories('include')

robin_map_dep = declare_dependency(
  include_directories: robin_map_inc,
)
meson.override_dependency('tsl-robin-map', robin_map_dep)

subdir('tests')
