if not openssl_dep.found() or meson.get_compiler('cpp').get_id() == 'msvc'
  subdir_done()
endif

ssltest = executable(
  'ssltest',
  'ssltest.cpp',
  dependencies: [crow_dep, catch2_dep],
  override_options: crow_private_options,
  cpp_args: crow_private_args,
)

test('ssl_test', ssltest)
