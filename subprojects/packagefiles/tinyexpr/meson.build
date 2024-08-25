project('tinyexpr', 'c',
    version: '0.0.0',
    default_options: ['c_std=c99']
)

cc = meson.get_compiler('c')
m_dep = cc.find_library('m', required: false)

tinyexpr_lib = library(
    'tinyexpr',
    'tinyexpr.c',
    install: true,
    dependencies: m_dep
)

depinc = include_directories('.')
tinyexpr_dep = declare_dependency(
    include_directories: depinc,
    link_with: tinyexpr_lib,
    dependencies: m_dep
)