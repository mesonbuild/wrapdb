project(
    'argparse',
    'cpp',
    version : '2.6',
    license : 'MIT'
)

includes = include_directories(['include'])

install_headers([
    'include/argparse/argparse.hpp',
], subdir: 'argparse')

argparse_dep = declare_dependency(
    include_directories: includes
)
