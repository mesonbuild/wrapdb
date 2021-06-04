  project('cpputest', 'cpp',
    version : '4.0',
    license : 'BSD-3')

cpputest_dirs = include_directories('include')
subdir('src')

cpputest_dep = declare_dependency(
    link_with : cpputest_lib,
    version : meson.project_version(),
    include_directories : cpputest_dirs)

if get_option('extinctions')
    cpputest_dep = declare_dependency(
        link_with : cpputest_ext_lib,
        version : meson.project_version(),
        include_directories : cpputest_dirs)
endif
