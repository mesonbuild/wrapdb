gmock_dep = dependency(
  'gmock',
  required: get_option('tests'),
)

if not gmock_dep.found()
  subdir_done()
endif

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

test_args = meson.get_compiler('cpp').get_supported_arguments(
  '-Wno-narrowing',
  '-Wno-c++11-narrowing',
)

yaml_cpp_tests_exe = executable(
  'yaml-cpp-tests',
  tests_src,
  include_directories: private_inc,
  dependencies: [yaml_cpp_dep, gmock_dep],
  cpp_args: test_args,
  override_options: ['cpp_std=c++17'],
  build_by_default: false,
)
test('yaml-cpp-tests', yaml_cpp_tests_exe)
