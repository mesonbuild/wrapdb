catch2_dep = dependency(
  'catch2-with-main',
  required: get_option('tests'),
  default_options: ['cpp_std=c++17'],
)
if not catch2_dep.found()
  summary(
    'tests',
    false,
    bool_yn: true,
  )
  subdir_done()
endif
summary(
  'tests',
  true,
  bool_yn: true,
)

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
subdir('template')
subdir('multi_file')
subdir('external_definition')
subdir('ssl')
subdir('img')

fs = import('fs')
test(
  'crow_test',
  unittest,
  timeout: 90,
  workdir: fs.parent(meson.current_build_dir()),
)
