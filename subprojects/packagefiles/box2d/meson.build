project('box2d', 'cpp', version : '2.4.1', license : 'zlib')

incdir = include_directories('include')

subdir('src')

box2d_dep = declare_dependency(link_with: box2d_lib,
    include_directories: incdir,
    version: meson.project_version())

subdir('unit-test')
