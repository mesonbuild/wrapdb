test_src_files = files(
  'oatpp-openssl/FullAsyncClientTest.cpp',
  'oatpp-openssl/FullAsyncClientTest.hpp',
  'oatpp-openssl/FullAsyncTest.cpp',
  'oatpp-openssl/FullAsyncTest.hpp',
  'oatpp-openssl/FullTest.cpp',
  'oatpp-openssl/FullTest.hpp',
  'oatpp-openssl/app/AsyncController.hpp',
  'oatpp-openssl/app/Client.hpp',
  'oatpp-openssl/app/Controller.hpp',
  'oatpp-openssl/app/DTOs.hpp',
  'oatpp-openssl/tests.cpp',
)

test_deps = deps
test_deps += dependency(
  'oatpp-test',
  version: '1.3.0',
)
test_deps += oatpp_openssl_dep

test_inc_dirs = inc_dirs
test_inc_dirs += include_directories('.')

test_flags = [
  '-DCERT_PEM_PATH="' + (meson.project_source_root() / 'utility' / 'cert' / 'test_key.pem') + '"',
  '-DCERT_CRT_PATH="' + (meson.project_source_root() / 'utility' / 'cert' / 'test_cert.crt') + '"',
]

openssl_tests = executable(
  'oatpp_openssl_tests',
  test_src_files,
  include_directories: test_inc_dirs,
  cpp_args: test_flags,
  dependencies: test_deps,
)

test(
  'oatpp openssl module tests',
  openssl_tests,
  timeout: 60,
)
