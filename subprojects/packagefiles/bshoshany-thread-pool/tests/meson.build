BS_thread_pool_test_exe = executable(
  'BS_thread_pool_test',
  'BS_thread_pool_test.cpp',
  dependencies: [bshoshany_thread_pool_dep],
)

test(
  'BS_thread_pool_test',
  BS_thread_pool_test_exe,
  args: 'log stdout tests',
)
benchmark(
  'BS_thread_pool_test benchmark',
  BS_thread_pool_test_exe,
  args: 'log stdout benchmarks',
)
