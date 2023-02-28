src = files(
  'async.cpp',
  'cfg.cpp',
  'color_sinks.cpp',
  'file_sinks.cpp',
  'spdlog.cpp',
  'stdout_sinks.cpp',
)

if not fmt_dep.found()
  src += files('bundled_fmtlib_format.cpp')
endif

spdlog_lib = library(
  'spdlog',
  src,
  include_directories: inc,
  dependencies: spdlog_dependencies,
  cpp_args: spdlog_compile_args,
)
