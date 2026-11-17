project(
  'llm-cpp',
  'cpp',
  version: '1.2.0',
  license: 'MIT',
  meson_version: '>=0.56.0',
  default_options: ['cpp_std=c++17'],
)

curl_dep = dependency(
  'libcurl',
  required: get_option('curl'),
)
thread_dep = dependency('threads')

# include/llm is on the path too, so #include "llm_cache.hpp" written against
# the single-header repositories keeps working.
llm_cpp_dep = declare_dependency(
  include_directories: include_directories('include', 'include/llm'),
  dependencies: [curl_dep, thread_dep],
)
meson.override_dependency('llm-cpp', llm_cpp_dep)

install_subdir(
  'include/llm',
  install_dir: get_option('includedir'),
  exclude_files: ['SOURCES.md'],
)

pkg = import('pkgconfig')
pkg.generate(
  name: 'llm-cpp',
  description: 'Single-header C++17 libraries for LLM features',
  version: meson.project_version(),
  subdirs: ['.', 'llm'],
)

if get_option('tests').enabled()
  cpp = meson.get_compiler('cpp')
  test_args = cpp.get_argument_syntax() == 'msvc' ? ['/utf-8'] : []
  foreach name : ['cache', 'compress', 'cost', 'format', 'guard', 'json']
    test(
      'offline_' + name,
      executable(
        'offline_' + name,
        'examples/offline/' + name + '.cpp',
        cpp_args: test_args,
        dependencies: llm_cpp_dep,
      ),
    )
  endforeach
  test(
    'cost_table',
    executable(
      'cost_table',
      'tests/upstream/cost/cost_table.cpp',
      cpp_args: test_args,
      dependencies: llm_cpp_dep,
    ),
  )
  test(
    'retry',
    executable(
      'test_llm_retry',
      'tests/upstream/retry/test_llm_retry.cpp',
      cpp_args: test_args,
      dependencies: llm_cpp_dep,
    ),
  )
endif
