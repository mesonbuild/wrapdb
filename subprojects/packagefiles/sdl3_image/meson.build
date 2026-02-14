project(
  'sdl3_image',
  'c',
  license: 'Zlib',
  license_files: 'LICENSE.txt',
  meson_version: '>= 1.1.0',
  version: '3.4.0',
  default_options: 'c_std=c99',
)

# Targets
windows = target_machine.system() == 'windows'
darwin = target_machine.system() == 'darwin'

macos = target_machine.subsystem() == 'macos'

# Backends
sdlimage_png_libpng = get_option('SDLIMAGE_PNG_LIBPNG').require(
  get_option('SDLIMAGE_PNG').enabled(),
  error_message: 'SDLIMAGE_PNG must be enabled to use libpng',
).enabled()
sdlimage_backend_wic = get_option('SDLIMAGE_BACKEND_WIC').require(
  windows,
  error_message: 'Windows must be set as the build target',
).allowed()
sdlimage_backend_imageio = get_option('SDLIMAGE_BACKEND_IMAGEIO').require(
  darwin,
  error_message: 'Darwin must be set as the build target',
).allowed()
sdlimage_backend_stb = get_option('SDLIMAGE_BACKEND_STB').disable_auto_if(
  sdlimage_backend_wic or sdlimage_backend_imageio,
).allowed()




required_deps = []

if get_option('enable-all').enabled()
  foreach key, dep : deps_dict
    required_deps += key.split('_')[0]
  endforeach
else
  if sdlimage_png_libpng  # If libpng explicity requested, add it to required
    required_deps += 'libpng'
  endif
  if not (  # If no loadable PNG backends and PNG is requested,
    sdlimage_backend_stb  # require libpng if it isn't already
    or sdlimage_backend_wic
    or sdlimage_backend_imageio
  )
    if get_option('SDLIMAGE_PNG').enabled()
      if 'libpng' not in required_deps
        required_deps += 'libpng'
      endif
    endif
    if get_option('SDLIMAGE_JPG').enabled()  # If no JPEG loadable backends and
      required_deps += 'libjpeg'      # JPEG is requested, require libjpeg
    endif
  endif
endif

deps_dict = {
  'sdl3_dep': dependency(
    'sdl3',
    version: '>=3.4.0',
  ),
  'libpng_dep': dependency(
    'libpng',
    required: 'libpng' in required_deps,
  ),
  'libavif_dep': dependency(
    'libavif',
    required: 'libavif' in required_deps,
  ),
  'libjxl_dep': dependency(
    'libjxl',
    required: 'libjxl' in required_deps,
  ),
  'libtif_dep': dependency(
    'libtif',
    required: 'libtif' in required_deps,
  ),
  'libwebp_dep': dependency(
    'libwebp',
    required: 'libwebp' in required_deps,
  ),
  'libjpeg_dep': dependency(
    'libjpeg',
    required: 'libjpeg' in required_deps,
  ),
}

c_args = []

subdir('src')

if sdlimage_backend_wic
  add_project_arguments(
    '-DSDL_IMAGE_USE_WIC_BACKEND',
    language: 'c',
  )
  deps_dict += {
    'windowscodecs': meson.get_compiler('c').find_library('windowscodecs'),
  }
endif

if sdlimage_backend_imageio
  if macos
    deps_dict += {
      'appleframeworks_dep': dependency(
        'appleframeworks',
        modules: ['CoreGraphics', 'Foundation', 'CoreServices', 'ImageIO'],
      ),
    }
  else
    deps_dict += {
      'appleframeworks_dep': dependency(
        'appleframeworks',
        modules: [
          'CoreGraphics',
          'Foundation',
          'CoreServices',
          'ImageIO',
          'UIKit',
        ],
      ),
    }
  endif

  if get_option('SDLIMAGE_PNG').allowed() and not sdlimage_backend_stb
    add_project_arguments(
      '-DPNG_USES_IMAGEIO',
      language: 'objc',
    )
  endif
  if get_option('SDLIMAGE_JPG').allowed() and not sdlimage_backend_stb
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

if sdlimage_backend_stb
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

# Sets load macros, save macros, guards against
# loading without required dependencies, and
# guards against enabling saving without
# enabling loading
foreach extension, savable : sdlimage_extensions
  foreach key, dep : deps_dict
    if key.split('_')[0].endswith(extension)
      auto = dep.found() ? true : false
    else
      auto = false
    endif
  endforeach
  if get_option(f'SDLIMAGE_@extension@').enable_auto_if(auto).enabled()
    add_project_arguments(
      f'-DLOAD_@extension@',
      language: 'c',
    )
    if savable and get_option(f'SDLIMAGE_@extension@_SAVE').enable_auto_if(auto).enabled()
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

deps = []

foreach key, dep : deps_dict
  deps += dep
endforeach

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
