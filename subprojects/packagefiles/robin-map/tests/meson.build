boost_unit_test_framework_dep = dependency(
  'boost',
  modules: 'unit_test_framework',
  required: get_option('tests'),
)

if not boost_unit_test_framework_dep.found()
  subdir_done()
endif

tsl_robin_map_tests = executable(
  'tsl_robin_map_tests',
  sources: files(
    'custom_allocator_tests.cpp',
    'main.cpp',
    'policy_tests.cpp',
    'robin_map_tests.cpp',
    'robin_set_tests.cpp',
  ),
  dependencies: [robin_map_dep, boost_unit_test_framework_dep],
  override_options: 'cpp_std=c++17',
  build_by_default: false,
)
test('tsl_robin_map_tests', tsl_robin_map_tests)
