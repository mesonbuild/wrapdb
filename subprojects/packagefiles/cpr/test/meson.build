gtest_dep = dependency(
  'gtest',
  required: get_option('tests'),
)
if not gtest_dep.found()
  subdir_done()
endif

#most of these cannot be built because upstream downloads extra stuff
tests = [
  #  'alternating',
  #  'async',
  #  'callback',
  #  'delete',
  #  'download',
  'encoded_auth',
  #  'error',
  #  'get',
  #  'head',
  #  'interceptor',
  #  'options',
  #  'patch',
  #  'post',
  #  'prepare',
  #  'proxy_auth',
  #  'proxy',
  #  'put',
  #  'raw_body',
  #  'session',
  'structures',
  'util',
  'version',
]

foreach t : tests
  test(
    t,
    executable(
      t,
      '@0@_tests.cpp'.format(t),
      dependencies: [cpr_dep, gtest_dep],
    ),
  )
endforeach
