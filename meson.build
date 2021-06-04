project('tinyxml2', 'cpp',
    version: '7.0.1',
    license: 'zlib')

tinyxml2_lib = library('tinyxml2', 'tinyxml2.cpp',
    install: true)

tinyxml2_dep = declare_dependency(link_with: tinyxml2_lib,
    include_directories: '.')

t = executable('xmltest', 'xmltest.cpp',
    dependencies: tinyxml2_dep)
test('tinyxml2test', t,
    args: meson.current_source_dir() / 'resources/dream.xml')

install_headers('tinyxml2.h')

pkg = import('pkgconfig')
pkg.generate(description: 'simple, small, C++ XML parser',
    libraries: tinyxml2_lib,
    url: 'https://github.com/leethomason/tinyxml2',
    filebase:'tinyxml2',
    name: 'TinyXML2')
