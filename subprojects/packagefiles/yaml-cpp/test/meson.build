# Latest gmock version only works with c++17, but library default standard is c++11
# So use local copy of gmock
if host_machine.system() == 'windows' and get_option('default_library') != 'static'
  dllexp = '-DGTEST_CREATE_SHARED_LIBRARY=1'
  dllimp = '-DGTEST_LINKED_AS_SHARED_LIBRARY=1'
else
  dllexp = []
  dllimp = []
endif
gtest_inc = include_directories(
  'gtest-1.11.0/googletest/include',
  'gtest-1.11.0/googletest',
)
gtest_lib = library(
  'gtest-all',
  sources: files('gtest-1.11.0/googletest/src/gtest-all.cc'),
  gnu_symbol_visibility: 'hidden',
  cpp_args: dllexp,
  dependencies: dependency('threads'),
  include_directories: gtest_inc,
)
gmock_inc = include_directories(
  'gtest-1.11.0/googlemock/include',
  'gtest-1.11.0/googlemock',
  'gtest-1.11.0/googletest/include',
)
gmock_lib = library(
  'gmock-all',
  files('gtest-1.11.0/googlemock/src/gmock-all.cc'),
  dependencies: dependency('threads'),
  include_directories: gmock_inc,
  link_with: gtest_lib,
)
gmock_dep = declare_dependency(
  include_directories: gmock_inc,
  link_with: [gmock_lib, gtest_lib],
)

# Library tests
tests_src = files(
  'binary_test.cpp',
  'integration/emitter_test.cpp',
  'integration/encoding_test.cpp',
  'integration/error_messages_test.cpp',
  'integration/gen_emitter_test.cpp',
  'integration/handler_spec_test.cpp',
  'integration/handler_test.cpp',
  'integration/load_node_test.cpp',
  'integration/node_spec_test.cpp',
  'main.cpp',
  'node/node_test.cpp',
  'ostream_wrapper_test.cpp',
  'parser_test.cpp',
  'regex_test.cpp',
)

test_exe = executable(
  'yaml-cpp-tests',
  tests_src,
  cpp_args: cc.get_supported_arguments(
    '-Wno-variadic-macros',
    '-Wno-sign-compare',
    '-Wno-c99-extensions',
  ),
  link_with: yaml_cpp_lib,
  include_directories: yaml_cpp_private_inc,
  dependencies: [gmock_dep],
)
test('tests', test_exe)
