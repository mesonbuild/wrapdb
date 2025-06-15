project(
  'sparrow',
  'cpp',
  meson_version: '>=0.60.0',
  version: '0.0.2',
  license: 'Apache-2.0',
  default_options: ['cpp_std=c++20'],
)

incdir = include_directories('include')

compile_args = []
deps = []
if get_option('use_date_polyfill')
  compile_args += ['-DSPARROW_USE_DATE_POLYFILL']
  deps += dependency('date')
  deps += dependency('tz')
endif

exclude_files = [
  'array_data_concepts.hpp',
  'dictionary_encoded_layout.hpp',
  'reference_wrapper_utils.hpp',
]
install_subdir(
  'include/sparrow',
  exclude_directories: ['details'],
  exclude_files: exclude_files,
  install_dir: get_option('includedir') / 'sparrow',
  install_tag: 'devel',
)

sparrow_dep = declare_dependency(
  include_directories: [incdir],
  dependencies: deps,
  compile_args: compile_args,
)
