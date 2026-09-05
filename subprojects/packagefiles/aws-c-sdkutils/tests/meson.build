test_src = files(
  'aws_profile_parser_tests.c',
  'aws_profile_tests.c',
  'endpoints_regex_tests.c',
  'endpoints_rule_engine_tests.c',
  'endpoints_util_tests.c',
  'resource_name_tests.c',
  'sdkutils_test.c',
)

libtestcases = static_library(
  'aws_c_sdkutils_testcases',
  test_src,
  dependencies: [aws_c_sdkutils_dep],
  c_args: ['-DAWS_UNSTABLE_TESTING_API=1'],
  include_directories: inc,
  build_by_default: false,
)

test_harness = executable(
  'aws-c-sdkutils-tests',
  test_harness_src,
  dependencies: [aws_c_sdkutils_dep],
  link_with: [libtestcases],
  c_args: ['-DAWS_UNSTABLE_TESTING_API=1'],
  include_directories: inc,
  build_by_default: false,
)

# aws-c-commons test harness has some very unfortunate behaviour on windows
# where it changes the working directory to the test executable's directory before running the test,
# so we need to copy all the test resources to the build directory or the tests cant find them.
# see https://github.com/awslabs/aws-c-common/blob/main/include/aws/testing/aws_test_harness.h#L407-L416
copied = []

subdir('resources/malformed-rules')
subdir('resources/test-cases')
subdir('resources/valid-rules')
subdir('resources')

foreach name : names
  test(
    name,
    run_test,
    args: [test_harness.full_path(), name],
    workdir: meson.current_build_dir() / 'resources',
    timeout: 600,
    depends: [test_harness, copied],
  )
endforeach
