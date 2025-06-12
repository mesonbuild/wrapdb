project(
  'gtest',
  'cpp',
  version: '1.17.0',
  default_options: [
    meson.version().version_compare('>=1.3.0') ? 'cpp_std=gnu++17,c++17' : 'cpp_std=gnu++17',
  ],
  license: 'BSD-3-Clause',
)

subdir('googletest')

subdir('googlemock')
