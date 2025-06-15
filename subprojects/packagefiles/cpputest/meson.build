project(
  'cpputest',
  'cpp',
  license: 'BSD-3-Clause',
  version: '4.0',
)

cpputest_includes = include_directories('include')
subdir('src')

cpputest_libs = [cpputest_lib]

if get_option('enable_cpputest_extensions')
  cpputest_libs += cpputest_ext_lib
endif

cpputest_dep = declare_dependency(
  link_with: cpputest_libs,
  version: meson.project_version(),
  include_directories: cpputest_includes,
)
