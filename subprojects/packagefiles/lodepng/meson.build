project('lodepng', ['c', 'cpp'],
    version: '20210627',
    license: 'zlib')

# C++ version
lodepng_dep = declare_dependency(
    include_directories: include_directories('.'),
    sources: files('lodepng.cpp'))

# C89 version
copy = find_program('cp', 'copy', required: true)
run_command(copy, 'lodepng.cpp', 'lodepng.c')
lodepng_c_dep = declare_dependency(
    include_directories: include_directories('.'),
    sources: files('lodepng.c'))

meson.override_dependency('lodepng', lodepng_dep)
meson.override_dependency('lodepng_c', lodepng_c_dep)
