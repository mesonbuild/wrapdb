test_files = files(
  'compare.cpp',
  'increment.cpp',
  'prerelease.cpp',
  'serialization.cpp',
  'version.cpp',
)

catch2_dep = dependency('catch2-with-main')

tests_exe = executable(
  'cpp_semver_tests',
  test_files,
  dependencies: [cpp_semver_dep, catch2_dep],
)

test('cpp_semver_tests', tests_exe)



