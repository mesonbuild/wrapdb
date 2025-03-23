
project(
  'oatpp-zlib',
  'cpp',
  default_options: ['default_library=static', 'cpp_std=c++11'],
  version: '1.3.0',
  license: 'Apache-2.0',
)

oatpp_module_version = meson.project_version()
oatpp_module_so_version = (oatpp_module_version.split('.').get(0) + '.' + oatpp_module_version.split(
  '.',
).get(
  1,
)
)

install = get_option('install')

deps = []
src_files = []
inc_dirs = []


deps += dependency(
  'oatpp',
  version: '1.3.0',
  default_options: ['tests=disabled'],
)
deps += dependency('zlib')


subdir('src')


lib_oatpp_zlib = library(
  'oatpp-zlib',
  src_files,
  dependencies: deps,
  include_directories: inc_dirs,
  install: install,
  soversion: oatpp_module_so_version,
  version: oatpp_module_version,
)


oatpp_zlib_dep = declare_dependency(
  include_directories: inc_dirs,
  link_with: lib_oatpp_zlib,
  version: oatpp_module_version,
)


if get_option('tests')
  subdir('test')
endif
