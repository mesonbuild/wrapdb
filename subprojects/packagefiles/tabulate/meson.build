project(
    'tabulate',
    'cpp',
    version : '1.4',
    license : 'MIT'
)

install_headers([
    'single_include/tabulate/tabulate.hpp',
], subdir: 'tabulate')

includes = include_directories(['single_include'])

tabulate_dep = declare_dependency(
    include_directories: includes
)
