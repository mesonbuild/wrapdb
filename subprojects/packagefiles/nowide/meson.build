project(
    'nowide',
    'cpp',
    version: '11.2.0',
    license: 'BSL-1.0',
    default_options : ['cpp_std=c++14'],
    meson_version : '>=0.37.0',
)

compile_args = []

if get_option('default_library') != 'static'
    add_project_arguments('-DNOWIDE_DYN_LINK', language: 'cpp')
    compile_args += ['-DNOWIDE_DYN_LINK']
endif

sources = []

subdir('src')  # fills in 'sources'

includes = include_directories('include')

nowide_lib = library(
    'nowide',
    sources,
    include_directories: includes,
)

nowide_dep = declare_dependency(
    compile_args: compile_args,
    include_directories: includes,
    link_with: nowide_lib,
)
