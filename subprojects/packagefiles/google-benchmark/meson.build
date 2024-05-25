project(
  'benchmark',
  'cpp',
  version: '1.8.4',
  default_options: ['cpp_std=c++14'],
  license: 'Apache-2.0',
)

benchmark_sources = files(
  'src/benchmark.cc',
  'src/benchmark_api_internal.cc',
  'src/benchmark_main.cc',
  'src/benchmark_name.cc',
  'src/benchmark_register.cc',
  'src/benchmark_runner.cc',
  'src/check.cc',
  'src/colorprint.cc',
  'src/commandlineflags.cc',
  'src/complexity.cc',
  'src/console_reporter.cc',
  'src/counter.cc',
  'src/csv_reporter.cc',
  'src/json_reporter.cc',
  'src/perf_counters.cc',
  'src/reporter.cc',
  'src/statistics.cc',
  'src/string_util.cc',
  'src/sysinfo.cc',
  'src/timers.cc',
)

benchmark_main_sources = files('src/benchmark_main.cc')
inc = include_directories('include')

args = ['-DNDEBUG']
if get_option('default_library') != 'static'
  args += '-Dbenchmark_EXPORTS'
else
  args += '-DBENCHMARK_STATIC_DEFINE'
endif

lib_benchmark_deps = [dependency('threads')]
if host_machine.system() == 'windows'
  cc = meson.get_compiler('cpp')
  if cc.get_argument_syntax() == 'msvc'
    add_project_arguments('-D_CRT_SECURE_NO_WARNINGS', language: 'cpp')
  endif
  lib_benchmark_deps += cc.find_library('shlwapi', required: true)
endif

lib_benchmark = library(
  'gbenchmark',
  benchmark_sources,
  include_directories: inc,
  cpp_args: args,
  gnu_symbol_visibility: 'hidden',
  dependencies: lib_benchmark_deps,
)

dargs = []
if get_option('default_library') == 'static'
  dargs += '-DBENCHMARK_STATIC_DEFINE'
endif

google_benchmark_dep = declare_dependency(
  compile_args: dargs,
  link_with: lib_benchmark,
  include_directories: inc,
)

lib_benchmark_main = library(
  'benchmark-main',
  benchmark_main_sources,
  include_directories: inc,
  cpp_args: args,
  dependencies: google_benchmark_dep,
)

google_benchmark_main_dep = declare_dependency(
  compile_args: dargs,
  link_with: lib_benchmark_main,
  dependencies: google_benchmark_dep,
)

if not get_option('tests').disabled()
  subdir('test')
endif
