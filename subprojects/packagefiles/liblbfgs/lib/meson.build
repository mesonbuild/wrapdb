lbfgs_lib = library('lbfgs', 'lbfgs.c',
    include_directories: '../include',
    dependencies: m_dep,
    install:true)

liblbfgs_dep = declare_dependency(link_with: lbfgs_lib,
    include_directories: '../include')

