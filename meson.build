project('liblbfgs', 'c',
    version: '1.10',
    license: 'MIT')

cc = meson.get_compiler('c')
m_dep = cc.find_library('m', required: false)

subdir('lib')
subdir('sample')

install_headers('include/lbfgs.h')
pkg = import('pkgconfig')
pkg.generate(description: 'Limited BFGS minimization library',
    libraries: lbfgs_lib,
    url: 'https://github.com/chokkan/liblbfgs',
    filebase:'liblbfgs',
    name: 'liblbfgs')
