project('mpack', 'c', version : '1.0', license : 'MIT', default_options : ['c_std=gnu99'])
incdir = include_directories('src/mpack')

src = files([
'src/mpack/mpack-common.c',
'src/mpack/mpack-expect.c',
'src/mpack/mpack-node.c',
'src/mpack/mpack-platform.c',
'src/mpack/mpack-reader.c',
'src/mpack/mpack-writer.c'
])

headers = files([
'src/mpack/mpack.h'
])

mpack = library('mpack', src, install : true)

ludocode_mpack_dep = declare_dependency(link_with : mpack, include_directories : incdir)

install_headers(headers)

pkg = import('pkgconfig')

pkg.generate(name: 'mpack', description: 'mpack msgpack serialization library', libraries: mpack)

