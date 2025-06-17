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
  #  'file_upload',
  #  'get',
  #  'head',
  #  'interceptor_multi',
  #  'interceptor',
  #  'multiasync',
  #  'multiasync',
  #  'multiperform',
  #  'options',
  #  'patch',
  #  'post',
  #  'prepare',
  #  'proxy_auth',
  #  'proxy',
  #  'put',
  #  'raw_body',
  #  'resolve',
  #  'session',
  'singleton',
  #  'ssl',
  'structures',
  'threadpool',
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
