# original CMakeLists.txt excludes MSVC only here
# but upstream does not test mingw and it seems to fail on mingw too.
if host_machine.system() == 'windows' or not openssl_dep.found() or not find_program(
  'openssl',
  required: false,
).found()
  summary(
    'ssltest',
    false,
    bool_yn: true,
  )
  subdir_done()
endif
summary(
  'ssltest',
  true,
  bool_yn: true,
)

ssltest = executable(
  'ssltest',
  'ssltest.cpp',
  dependencies: [crow_dep, catch2_dep],
  override_options: crow_private_options,
  cpp_args: crow_private_args,
)

test('ssl_test', ssltest)
