project('miniz', 'c', license : 'mit', version : '2.1.0')

miniz_inc = include_directories('.')

install_headers('miniz.h')

miniz_src = files([
    'miniz.c'
])

miniz_lib = library('miniz', miniz_src, install : true)

miniz_dep = declare_dependency(
    link_with : miniz_lib,
    include_directories : miniz_inc
)
                               
pkg = import('pkgconfig')

pkg.generate(
    miniz_lib,
    name : 'miniz',
    version : meson.project_version(),
    description : 'Single C source file zlib-replacement library'
)
