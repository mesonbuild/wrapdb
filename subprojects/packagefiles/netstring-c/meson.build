project(
  'netstring-c',
  'c',
  version: '0.0.0',
  license: 'Unlicense',
  meson_version: '>= 0.40',
)

# libm (glibc)
cc = meson.get_compiler('c')
libm_dep = cc.find_library(
  'm',
  required: false,
)

netstring_c_lib = library(
  'netstring-c',
  vs_module_defs: 'netstring-c.def',
  dependencies: libm_dep,
  sources: 'netstring.c',
)

netstring_c_dep = declare_dependency(
  dependencies: libm_dep,
  include_directories: '.',
  link_with: netstring_c_lib,
)

netstring_c_test = executable(
  'netstring-c-testsuite',
  build_by_default: false,
  dependencies: netstring_c_dep,
  sources: 'testsuite.c',
)

test('netstring-c-testsuite', netstring_c_test)
