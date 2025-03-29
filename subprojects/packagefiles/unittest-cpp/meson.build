project(
  'UnitTest++',
  'cpp',
  version: '2.0.0',
  license: 'MIT',
)

unittest_cpp_src = []

if meson.get_compiler('cpp').get_argument_syntax() == 'msvc'
  add_project_arguments(
    '-D_CRT_SECURE_NO_WARNINGS',
    language: 'cpp',
  )
endif

subdir('UnitTest++')

unittest_cpp_lib = static_library(
  'unittest-cpp',
  unittest_cpp_src,
  include_directories: '.',
)

unittest_cpp_dep = declare_dependency(
  version: meson.project_version(),
  link_with: unittest_cpp_lib,
  include_directories: '.',
)

subdir('tests')
