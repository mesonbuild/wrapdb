build_tests_opt = get_option('build_tests')

glfw3_dep = dependency(
  'glfw3',
  required: build_tests_opt,
  disabler: true,
)
gtest_dep = dependency(
  'gtest',
  required: build_tests_opt,
  disabler: true,
)
gmock_dep = dependency(
  'gmock',
  required: build_tests_opt,
  disabler: true,
)

# Commented out tests are broken and unused upstream - see https://github.com/cginternals/glbinding/pull/345
glbinding_test_sources = files(
  'glbinding-test/AllVersions_test.cpp',
  'glbinding-test/Boolean_compilation_test.cpp',
  #'glbinding-test/MultiContext_test.cpp',
  #'glbinding-test/MultiThreading_test.cpp',
  'glbinding-test/Regression_test_185.cpp',
  'glbinding-test/Regression_test_198.cpp',
  'glbinding-test/Regression_test_82.cpp',
  'glbinding-test/RingBuffer_test.cpp',
  'glbinding-test/SharedBitfield_test.cpp',
  'glbinding-test/main.cpp',
)

glbinding_test_exe = executable(
  'glbinding-test',
  glbinding_test_sources,
  cpp_args: [system_name_arg],
  override_options: ['cpp_std=c++14'],
  dependencies: [
    glbinding_dep,
    glbinding_aux_dep,
    glfw3_dep,
    gtest_dep,
    gmock_dep,
  ],
)

if get_option('run_tests')
  test(
    'glbinding test suite',
    glbinding_test_exe,
    protocol: 'gtest',
  )
endif
