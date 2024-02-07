project('cpputest', 'cpp',
  license: 'BSD-3',
  version: '4.0',
)

cpputest_includes = include_directories('include')
subdir('src')

cpputest_dep = declare_dependency(
    link_with : cpputest_lib,
    version : meson.project_version(),
    include_directories : cpputest_includes)

if get_option('provide_extensions')
    cpputest_ext_dep = declare_dependency(
        link_with : cpputest_ext_lib,
        version : meson.project_version(),
        include_directories : cpputest_includes)
endif
