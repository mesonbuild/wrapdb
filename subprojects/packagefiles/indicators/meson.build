project(
    'indicators',
    'cpp',
    version : '2.2',
    license : 'MIT'
)

install_headers([
    'single_include/indicators/indicators.hpp',
], subdir: 'indicators')

includes = include_directories(['single_include'])

indicators_dep = declare_dependency(
    include_directories: includes
)
