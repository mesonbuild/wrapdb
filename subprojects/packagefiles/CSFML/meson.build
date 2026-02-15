project(
  'csfml',
  ['c', 'cpp'],
  meson_version: '>= 0.63.0',
  version: '3.0.0',
  license: 'Zlib',
  default_options: [
    'warning_level=2',
    'cpp_std=c++17',
    'wrap_mode=forcefallback',
  ],
)

deps = [
  dependency('sfml'),
  dependency('gl'),
]
private_include = include_directories('src')
public_include = include_directories('include')

# Install C header
subdir('include/CSFML')
# Compile libs
csfml_libs = []
subdir('src/CSFML')

csfml_deps = declare_dependency(
  include_directories: [public_include, private_include],
  link_with: csfml_libs,
  dependencies: deps,
)

meson.override_dependency('csfml', csfml_deps)

