BS_thread_pool_test_exe = executable('thread_pool_test',
  'BS_thread_pool_test.cpp',
  dependencies: [bshoshany_thread_pool_dep],
)

test('thread_pool_test', BS_thread_pool_test_exe)
benchmark('thread_pool_test benchmark', BS_thread_pool_test_exe)
