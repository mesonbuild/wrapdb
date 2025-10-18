catch2_dep = dependency(
  'catch2-with-main',
  required: get_option('tests'),
)
if not catch2_dep.found()
  subdir_done()
endif

test_srcs = [
  'unittest.cpp',
  'query_string_tests.cpp',
  'unit_tests/test_http_response.cpp',
  'unit_tests/test_json.cpp',
  'unit_tests/test_mustache.cpp',
  'unit_tests/test_utility.cpp',
  'unit_tests/test_websocket.cpp',
]

unittest = executable(
  'unittest',
  test_srcs,
  dependencies: [crow_dep, catch2_dep],
  override_options: crow_private_options,
  cpp_args: crow_private_args,
)
test(
  'crow_test',
  unittest,
  timeout: 60,
)

subdir('template')
subdir('multi_file')
subdir('external_definition')
subdir('ssl')
subdir('img')
