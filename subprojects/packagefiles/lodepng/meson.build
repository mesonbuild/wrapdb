project('lodepng', ['c', 'cpp'],
    version: '20210627',
    license: 'zlib')

# C++ version
lodepng_lib = static_library('lodepng', 'lodepng.cpp')
lodepng_dep = declare_dependency(
    include_directories: include_directories('.'),
    link_with: lodepng_lib)

# C89 version
configure_file(input: 'lodepng.cpp', output: 'lodepng.c', copy: true)
lodepng_c_lib = static_library('lodepng_c', 'lodepng.c')
lodepng_c_dep = declare_dependency(
    include_directories: include_directories('.'),
    link_with: lodepng_c_lib)

meson.override_dependency('lodepng', lodepng_dep)
meson.override_dependency('lodepng_c', lodepng_c_dep)
