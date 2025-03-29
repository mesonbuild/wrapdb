test_src_files = files(
  'oatpp-zlib/DeflateAsyncTest.cpp',
  'oatpp-zlib/DeflateAsyncTest.hpp',
  'oatpp-zlib/DeflateTest.cpp',
  'oatpp-zlib/DeflateTest.hpp',
  'oatpp-zlib/tests.cpp',
)

test_deps = deps
test_deps += dependency(
  'oatpp-test',
  version: '1.3.0',
)
test_deps += oatpp_zlib_dep

test_inc_dirs = inc_dirs
test_inc_dirs += include_directories('.')

test_flags = [
  '-DCERT_PEM_PATH="' + (meson.project_source_root() / 'utility' / 'cert' / 'test_key.pem') + '"',
  '-DCERT_CRT_PATH="' + (meson.project_source_root() / 'utility' / 'cert' / 'test_cert.crt') + '"',
]

zlib_tests = executable(
  'oatpp_zlib_tests',
  test_src_files,
  include_directories: test_inc_dirs,
  cpp_args: test_flags,
  dependencies: test_deps,
)

# tests may take longer
test(
  'oatpp zlib module tests',
  zlib_tests,
  timeout: 60,
)
