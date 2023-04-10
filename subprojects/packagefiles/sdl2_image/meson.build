project(
  'sdl2-image',
  'c',
  version: '2.6.3',
  meson_version: '>=0.59.0',
)

feature_args = []
extra_library_args = []

if host_machine.system() == 'windows' and get_option('default_library') != 'static'
    extra_library_args += '-DDLL_EXPORT'
endif

# Files that are not directly tied to loaders
sources = files(
  'IMG.c',
  'IMG_stb.c',
  'IMG_WIC.c',
)

sdl2_dep = dependency('sdl2')

deps = [sdl2_dep]

# Backends provide support for certain formats, allowing not to depend on external library or use potentially better optimized algorithm
backend_provided_loaders = []

use_stbimage_backend = get_option('use_stbimage').allowed()
if use_stbimage_backend
  feature_args += '-DUSE_STBIMAGE'
  backend_provided_loaders += ['png', 'jpg']
endif

use_imageio_backend = get_option('use_imageio').require(host_machine.system() == 'darwin', error_message: 'Image I/O backend is exclusive to MacOS').allowed()
if use_imageio_backend
  add_languages('objc', native: false)
  sources += files('IMG_ImageIO.m')
  deps += dependency('appleframeworks', modules : ['ApplicationServices'])

  backend_provided_loaders += ['png', 'jpg', 'tif', 'bmp', 'gif', 'tga']
endif

if not use_imageio_backend and host_machine.system() == 'darwin'
  feature_args += '-DSDL_IMAGE_USE_COMMON_BACKEND'
endif

use_wic_backend = get_option('use_wic').require(host_machine.system() == 'windows', error_message: 'WIC backend is exclusive to Windows').allowed()
if use_wic_backend
  feature_args += '-DSDL_IMAGE_USE_WIC_BACKEND'
  backend_provided_loaders += ['png', 'jpg', 'tif']
endif

summary({
  'stb_image': use_stbimage_backend,
  'Image I/O': use_imageio_backend,
  'Windows Imaging Component': use_wic_backend,
}, section: 'Backends')

# Loaders that don't depend on anything
self_contained_loaders = [
  'bmp',
  'gif',
  'lbm',
  'pcx',
  'pnm',
  'qoi',
  'svg',
  'tga',
  'xcf',
  'xpm',
  'xv',
]

foreach format_name : self_contained_loaders
  sources += files('IMG_@0@.c'.format(format_name))
  if get_option(format_name).allowed()
    feature_args += '-DLOAD_@0@'.format(format_name.to_upper())
    summary(format_name, format_name in backend_provided_loaders ? 'handled by backend' : 'built-in loader', section: 'Formats')
  else
    summary(format_name, 'disabled', section: 'Formats')
  endif
endforeach

# Loaders that depend on external libraries
external_dep_loaders = {
  'avif': 'libavif',
  'jpg': 'libjpeg',
  'jxl': 'libjxl',
  'png': 'libpng',
  'tif': 'libtiff-4',
  'webp': 'libwebp',
}

foreach format_name, library_name : external_dep_loaders
  sources += files('IMG_@0@.c'.format(format_name))
  if format_name in backend_provided_loaders
    if get_option(format_name).allowed()
      feature_args += '-DLOAD_@0@'.format(format_name.to_upper())
      summary(format_name, 'handled by backend', section: 'Formats')
    else
      summary(format_name, 'disabled', section: 'Formats')
    endif
  else
    loader_library = dependency(library_name, required: get_option(format_name))
    if loader_library.found()
      deps += loader_library
      feature_args += '-DLOAD_@0@'.format(format_name.to_upper())
      summary(format_name, 'handled by @0@'.format(library_name), section: 'Formats')
    else
      summary(format_name, 'disabled', section: 'Formats')
    endif
  endif
endforeach

# Image saving

jpg_save_support = get_option('jpg_save')
feature_args += '-DSDL_IMAGE_SAVE_JPG=@0@'.format(jpg_save_support.to_int())

png_save_support = get_option('png_save')
feature_args += '-DSDL_IMAGE_SAVE_PNG=@0@'.format(png_save_support.to_int())

summary({
  'jpg': jpg_save_support,
  'png': png_save_support,
}, section: 'Image saving (depends on corresponding loaders)')

sdl2_image_lib = library(
  'sdl2image',
  sources,
  c_args: [feature_args, extra_library_args],
  dependencies: deps,
  gnu_symbol_visibility: 'hidden',
)

depinc = include_directories('.')
sdl2_image_dep = declare_dependency(
  include_directories: depinc,
  link_with: sdl2_image_lib,
)

if get_option('test')
  subdir('test')
endif
