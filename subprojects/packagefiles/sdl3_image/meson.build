project('sdl3_image', 'c',
  version: '3.2.4')

sdl_dep = dependency('sdl3', version: '>=3.2.4')

png_dep = dependency('libpng')
jpg_dep = dependency('libjpeg', required: false)

img_args = []

# These are enabled by default it seems.
#img_args = ['-DWANT_LIBPNG']
#if jpg_dep.found()
#  img_args += '-DWANT_JPEGLIB'
#endif

subdir('src')
img_lib = library('sdl3_image',
  img_src,
  c_args: img_args,
  include_directories: 'include',
  dependencies: [png_dep, sdl_dep])

sdl3_image_dep = declare_dependency(include_directories: 'include',
  link_with: img_lib)
