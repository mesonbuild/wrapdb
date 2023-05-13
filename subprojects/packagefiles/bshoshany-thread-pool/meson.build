project('bshoshany-thread-pool', 'cpp',
  version : '3.4.0',
  license : 'MIT',
  meson_version: '>=0.47.0',
  default_options: ['cpp_std=c++17'],
)

thread_dep = dependency('threads')

bshoshany_thread_pool_dep = declare_dependency(include_directories: include_directories('.'), dependencies: thread_dep)

test_opt = get_option('test')
# MacOS's libc lacks std::quick_exit, which tests use
build_tests = test_opt.auto() ? host_machine.system() != 'darwin' : test_opt.enabled()

if build_tests
  BS_thread_pool_test_exe = executable('thread_pool_test',
    'BS_thread_pool_test.cpp',
    dependencies: [bshoshany_thread_pool_dep],
  )

  test('thread_pool_test', BS_thread_pool_test_exe)
  benchmark('thread_pool_test benchmark', BS_thread_pool_test_exe)

  BS_thread_pool_light_test_exe = executable('thread_pool_light_test',
    'BS_thread_pool_light_test.cpp',
    dependencies: [bshoshany_thread_pool_dep],
  )

  test('thread_pool_light_test', BS_thread_pool_light_test_exe)
endif

if not meson.is_subproject()
  install_headers('BS_thread_pool.hpp', 'BS_thread_pool_light.hpp')
endif

if meson.version().version_compare('>=0.54.0')
  meson.override_dependency('bshoshany-thread-pool', bshoshany_thread_pool_dep)
endif
