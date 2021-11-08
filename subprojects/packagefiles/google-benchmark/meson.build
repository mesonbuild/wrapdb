project('benchmark', 'cpp',
  version : '1.6.0',
  default_options : ['cpp_std=c++11'],
  license : 'Apache-2.0')

benchmark_sources = [
 'src/benchmark.cc',
 'src/benchmark_api_internal.cc',
 'src/benchmark_main.cc',
 'src/benchmark_name.cc',
 'src/benchmark_register.cc',
 'src/benchmark_runner.cc',
 'src/colorprint.cc',
 'src/commandlineflags.cc',
 'src/complexity.cc',
 'src/console_reporter.cc',
 'src/counter.cc',
 'src/csv_reporter.cc',
 'src/json_reporter.cc',
 'src/perf_counters.cc',
 'src/reporter.cc',
 'src/sleep.cc',
 'src/statistics.cc',
 'src/string_util.cc',
 'src/sysinfo.cc',
 'src/timers.cc'
]

benchmark_main_sources = ['src/benchmark_main.cc']
inc = include_directories('include')


lib_benchmark_deps = [ dependency('threads') ]

if host_machine.system() == 'windows'
  cc = meson.get_compiler('cpp')
  lib_benchmark_deps += cc.find_library('shlwapi', required : true)
endif

lib_benchmark = static_library('gbenchmark',
                        benchmark_sources,
                        include_directories:inc,
                        cpp_args : '-DNDEBUG',
                        dependencies : lib_benchmark_deps)

google_benchmark_dep = declare_dependency(
                        link_with:lib_benchmark,
                        include_directories:inc)

lib_benchmark_main = static_library('benchmark-main',
                        benchmark_main_sources,
                        include_directories:inc,
                        cpp_args : '-DNDEBUG',
                        dependencies : google_benchmark_dep)

google_benchmark_main_dep = declare_dependency(
                        link_with:lib_benchmark_main,
                        include_directories:inc)
