project('pcg-cpp', 'cpp',
	license: 'Apache 2.0',
	version: '0.98.1')

install_headers('include/pcg_extras.hpp')
install_headers('include/pcg_random.hpp')
install_headers('include/pcg_uint128.hpp')

pkgc = import('pkgconfig')
pkgc.generate(name: 'pcg-cpp',
    version: meson.project_version(),
    description: 'PCG Random Number Generation, C++ Edition'
)

pcg_cpp_dep = declare_dependency(include_directories: include_directories('include'))
