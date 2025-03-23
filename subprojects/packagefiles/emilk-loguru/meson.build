project(
  'emilk-loguru',
  'cpp',
  version: '2.1.0',
  license: 'Public Domain',
  meson_version: '>=0.50',
)

cxx = meson.get_compiler('cpp')
compile_opts = [
  '-DLOGURU_SCOPE_TEXT_SIZE=@0@'.format(get_option('loguru_scope_text_size')),
  '-DLOGURU_FILENAME_WIDTH=@0@'.format(get_option('loguru_filename_width')),
  '-DLOGURU_THREADNAME_WIDTH=@0@'.format(get_option('loguru_threadname_width')),
  '-DLOGURU_SCOPE_TIME_PRECISION=@0@'.format(
    get_option('loguru_scope_time_precision'),
  ),
]
loguru_deps_internal = [dependency('threads')]

options = [
  'loguru_debug_logging',
  'loguru_debug_checks',
  'loguru_catch_sigabrt',
  'loguru_redefine_assert',
  'loguru_with_streams',
  'loguru_replace_glog',
  'loguru_with_fileabs',
  'loguru_rtti',
  'loguru_verbose_scope_endings',
]

foreach o : options
  compile_opts += '-D@0@=@1@'.format(o.to_upper(), get_option(o).to_int())
endforeach

dl_dep = cxx.find_library(
  'dl',
  required: get_option('loguru_stacktraces'),
)
loguru_deps_internal += dl_dep
execinfo = cxx.has_header(
  'execinfo.h',
  required: get_option('loguru_stacktraces'),
)
if execinfo
  # execinfo needs -lexecinfo on FreeBSD and others
  libexecinfo_dep = cxx.find_library(
    'execinfo',
    required: false,
  )
  if libexecinfo_dep.found()
    loguru_deps_internal += libexecinfo_dep
  endif

  compile_opts += '-DLOGURU_STACKTRACES=@0@'.format(dl_dep.found().to_int())
else
  compile_opts += '-DLOGURU_STACKTRACES=0'
endif

fmt_dep = dependency(
  'fmt',
  required: get_option('loguru_use_fmtlib'),
)
loguru_deps_internal += fmt_dep
compile_opts += '-DLOGURU_USE_FMTLIB=@0@'.format(fmt_dep.found().to_int())

api = '-DLOGURU_EXPORT=__attribute__((visibility("default")))'
if host_machine.system() == 'windows'
  api = get_option('default_library') != 'static' ? '-DLOGURU_EXPORT=__declspec(dllexport)' : []
endif

emilk_loguru_lib = library(
  'loguru',
  'loguru.cpp',
  include_directories: '.',
  cpp_args: [compile_opts, api],
  dependencies: loguru_deps_internal,
  gnu_symbol_visibility: 'hidden',
  soversion: host_machine.system() == 'windows' ? '' : meson.project_version().split(
    '.',
  )[0],
  version: meson.project_version(),
  install: true,
)

install_headers('loguru.hpp')

pkgc = import('pkgconfig')
pkgc.generate(
  emilk_loguru_lib,
  name: 'loguru',
  description: 'A lightweight and flexible C++ logging library',
)

api = []
if host_machine.system() == 'windows' and get_option('default_library') != 'static'
  api = '-DLOGURU_EXPORT=__declspec(dllimport)'
endif

emilk_loguru_dep = declare_dependency(
  include_directories: '.',
  link_with: emilk_loguru_lib,
  compile_args: [compile_opts, api],
)
