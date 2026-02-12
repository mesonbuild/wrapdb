project(
  'sdl3_image',
  'c',
  license: 'Zlib',
  license_files: 'LICENSE.txt',
  meson_version: '>= 1.1.0',
  version: '3.4.0',
  default_options: 'c_std=c99',
)

sdl3_dep = dependency(
  'sdl3',
  version: '>=3.4.0',
)  # Minimum allowed SDL3 version, not SDL3_IMAGE version
libpng_dep = dependency(
  'libpng',
  required: get_option('SDLIMAGE_PNG_LIBPNG'),
)  # STB loadable
libavif_dep = dependency(
  'libavif',
  version: '>=0.1.0',
  required: get_option('SDLIMAGE_AVIF'),
)  # Absent from wrapdb as of Feb 1 2026
libjxl_dep = dependency(
  'libjxl',
  required: get_option('SDLIMAGE_JXL'),
)  # Absent from wrapdb as of Feb 1 2026
libtiff_dep = dependency(
  'libtiff',
  required: get_option('SDLIMAGE_TIF'),
)
libwebp_dep = dependency(
  'libwebp',
  required: get_option('SDLIMAGE_WEBP'),
)
libjpeg_dep = dependency(
  'libjpeg',
  required: get_option('SDLIMAGE_JPG'),
)  # STB loadable

deps = [
  sdl3_dep,
  libpng_dep,
  libavif_dep,
  libjxl_dep,
  libtiff_dep,
  libwebp_dep,
  libjpeg_dep,
]
subdir('src')

get_option('SDLIMAGE_BACKEND_WIC').require(
  target_machine.system() == 'windows',
  error_message: 'Windows must be set as the build target',
)
if get_option('SDLIMAGE_BACKEND_WIC').enabled()
  add_project_arguments(
    '-DSDL_IMAGE_USE_WIC_BACKEND',
    language: 'c',
  )
endif

get_option('SDLIMAGE_BACKEND_IMAGEIO').require(
  target_machine.system() == 'darwin',
  error_message: 'Darwin must be set as the build target',
)
if target_machine.system() == 'darwin'
  add_languages(
    'objc',
    native: false,
  )
  deps += dependency(
    'appleframeworks',
    modules: ['ApplicationServices'],
  )
  if get_option('SDLIMAGE_BACKEND_IMAGEIO').enabled()
    if get_option('SDLIMAGE_PNG').enabled() and not get_option(
      'SDLIMAGE_BACKEND_STB',
    ).enabled()
      add_project_arguments(
        '-DPNG_USES_IMAGEIO',
        language: 'objc',
      )
    endif
    if get_option('SDLIMAGE_JPG').enabled() and not get_option(
      'SDLIMAGE_BACKEND_STB',
    ).enabled()
      add_project_arguments(
        '-DJPG_USES_IMAGEIO',
        language: 'objc',
      )
    endif
  else
    add_project_arguments(
      '-DSDL_IMAGE_USE_COMMON_BACKEND',
      language: 'objc',
    )
  endif
endif

if get_option('SDLIMAGE_BACKEND_STB').enabled()
  add_project_arguments(
    '-DUSE_STBIMAGE',
    language: 'c',
  )
endif


# Boolean correlates to whether the extension is natively savable or not
sdlimage_extensions = {
  'ANI': true,
  'AVIF': true,
  'BMP': true,
  'GIF': true,
  'JPG': true,
  'JXL': false,
  'LBM': false,
  'PCX': false,
  'PNG': true,
  'PNM': false,
  'QOI': false,
  'SVG': false,
  'TGA': true,
  'TIF': false,
  'WEBP': true,
  'XCF': false,
  'XPM': false,
  'XV': false,
}

# Sets load macros, save macros, and guards against
# enabling saving without enabling loading
foreach extension, savable : sdlimage_extensions
  if get_option(f'SDLIMAGE_@extension@').enabled()
    add_project_arguments(
      f'-DLOAD_@extension@',
      language: 'c',
    )
    if savable and get_option(f'SDLIMAGE_@extension@_SAVE').enabled()
      add_project_arguments(
        f'-DSAVE_@extension@',
        language: 'c',
      )
    endif
  elif savable and get_option(f'SDLIMAGE_@extension@_SAVE').enabled()
    get_option(f'SDLIMAGE_@extension@_SAVE').disable_if(
      true,
      error_message: f'"SDLIMAGE_@extension@" must be enabled',
    )
  endif
endforeach

if get_option('default_library') == 'shared'
  c_args = ['-DDLL_EXPORT']
else
  c_args = []
endif

sdl3_image_lib = library(
  'sdl3_image',
  sdl3_image_src,
  include_directories: 'include',
  c_args: c_args,
  dependencies: deps,
  install: true,
)

sdl3_image_dep = declare_dependency(
  include_directories: 'include',
  link_with: sdl3_image_lib,
)

meson.override_dependency('sdl3_image', sdl3_image_dep)
