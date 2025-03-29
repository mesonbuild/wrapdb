project(
  'bshoshany-thread-pool',
  'cpp',
  version: '5.0.0',
  license: 'MIT',
  meson_version: '>=0.47.0',
  default_options: ['cpp_std=c++17'],
)

thread_dep = dependency('threads')

bshoshany_thread_pool_dep = declare_dependency(
  include_directories: include_directories('include', 'modules'),
  dependencies: thread_dep,
)

test_opt = get_option('test')
build_tests = test_opt.enabled()

if build_tests
  subdir('tests')
endif

if not meson.is_subproject()
  install_headers('include/BS_thread_pool.hpp', 'modules/BS.thread_pool.cppm')
endif

if meson.version().version_compare('>=0.54.0')
  meson.override_dependency('bshoshany-thread-pool', bshoshany_thread_pool_dep)
endif
