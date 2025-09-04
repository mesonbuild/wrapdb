project(
  'obfuscate',
  'cpp',
  version: '1.0.0',
  license: 'Unlicense',
  meson_version: '>=0.59.0',
  default_options: ['cpp_std=c++14'],
)

obfuscate_dep = declare_dependency(
  include_directories: include_directories('.'),
)

gtest_dep = dependency(
  'gtest_main',
  version: '>=1.10.0',
  required: get_option('tests'),
)

if gtest_dep.found()
  test(
    'test_unit',
    executable(
      'test_unit',
      ['test_unit.cpp'],
      dependencies: [gtest_dep, obfuscate_dep],
    ),
  )
endif

meson.override_dependency('Obfuscate', obfuscate_dep)
