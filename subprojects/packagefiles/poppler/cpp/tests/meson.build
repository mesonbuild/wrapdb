poppler_dump_executable = executable(
  'poppler-dump',
  dependencies: [poppler_cpp_library_dependency],
  include_directories: utils_include_directory,
  sources: ['poppler-dump.cpp', parseargs_cc],
)

poppler_render_executable = executable(
  'poppler-render',
  dependencies: [poppler_cpp_library_dependency],
  include_directories: utils_include_directory,
  sources: ['poppler-render.cpp', parseargs_cc],
)

# @todo fuzz tests
