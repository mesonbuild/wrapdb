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

version_parts = meson.project_version().split('.')

spdlog_lib = library(
  'spdlog',
  src,
  include_directories: inc,
  dependencies: spdlog_dependencies,
  cpp_args: spdlog_compile_args,
  override_options: override_cpp,
  soversion: version_parts[0] + '.' + version_parts[1],
  version: meson.project_version(),
  install: true,
)
