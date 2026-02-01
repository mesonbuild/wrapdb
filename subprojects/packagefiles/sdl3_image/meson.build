project('sdl3_image', 'c',
  meson_version: '>= 1.1.0',
  version: '3.4.0',
  default_options: 'c_std=c99')

major_version = meson.project_version().split('.')[0]
minor_version = meson.project_version().split('.')[1]
micro_version = meson.project_version().split('.')[2]

sdl3_dep = dependency('sdl3', version: '>=3.4.0') # Minimum allowed SDL3 version, not SDL3_IMAGE version
libpng_dep = dependency('libpng', required: get_option('SDLIMAGE_PNG_LIBPNG'))
libavif_dep = dependency('libavif', version: '>=0.1.0', required: get_option('SDLIMAGE_AVIF')) # Absent from wrapdb as of Feb 1 2026
libjxl_dep = dependency('libjxl', required: get_option('SDLIMAGE_JXL')) # Absent from wrapdb as of Feb 1 2026
libtiff_dep = dependency('libtiff', required: get_option('SDLIMAGE_TIF'))
libwebp_dep = dependency('libwebp', required: get_option('SDLIMAGE_WEBP'))
libjpeg_dep = dependency('libjpeg-turbo', required: get_option('SDLIMAGE_JPG'))

deps = [sdl3_dep, libpng_dep, libavif_dep, libjxl_dep, libtiff_dep, libwebp_dep, libjpeg_dep]
subdir('src')

platform_supports_shared = target_machine.system() == 'emscripten' ? false : true

get_option('POSITION_INDEPENDENT_CODE').require(platform_supports_shared, error_message: 'Target "' + target_machine.system() + '" does not support shared libraries')
if get_option('POSITION_INDEPENDENT_CODE').enabled()
  add_project_arguments('-fPIC', language: 'c')


get_option('SDLIMAGE_SAMPLES').disable_auto_if(meson.is_subproject())
get_option('SDLIMAGE_SAMPLES').disable_auto_if(target_machine.system() == 'android')


get_option('SDLIMAGE_BACKEND_WIC').require(target_machine.system() == 'windows', error_message : 'Windows must be set as the build target')
if get_option('SDLIMAGE_BACKEND_WIC').enabled()
  add_project_arguments('-DSDL_IMAGE_USE_WIC_BACKEND', language: 'c')
endif

get_option('SDLIMAGE_BACKEND_IMAGEIO').require(target_machine.system() == 'darwin', error_message: 'Darwin must be set as the build target')
if target_machine.system() == 'darwin'
  add_language('objc')
  if get_option('SDLIMAGE_PNG').enabled() and not get_option('SDLIMAGE_BACKEND_STB').enabled()
    add_project_arguments('-DPNG_USES_IMAGEIO', language: 'objc')
  endif
  if get_option('SDLIMAGE_JPG').enabled() and not get_option('SDLIMAGE_BACKEND_STB').enabled()
    add_project_arguments('-DJPG_USES_IMAGEIO', language: 'objc')
  endif
else
  add_project_arguments('-DSDL_IMAGE_USE_COMMON_BACKEND', language: 'objc')
endif

if get_option('SDLIMAGE_BACKEND_STB').enabled()
  add_project_arguments('-DUSE_STBIMAGE', language: 'c')
endif



# Boolean correlates to whether the extension is natively savable or not
sdlimage_extensions = {'ANI': true, 'AVIF': true, 'BMP': true, 'GIF': true, 
                      'JPG': true, 'JXL': false, 'LBM': false, 'PCX': false,
                      'PNG': true, 'PNM': false, 'QOI': false, 'SVG': false,
                      'TGA': true, 'TIF': false, 'WEBP': true, 'XCF': false,
                      'XPM': false, 'XV': false} 

# Sets load macros, save macros and guards against
# enabling saving without enabling loading
foreach extension, savable : sdlimage_extensions
  if get_option(f'SDLIMAGE_@extension@').enabled()
    add_project_arguments(f'-DLOAD_@extension@')
    if savable and get_option(f'SDLIMAGE_@extension@_SAVE').enabled()
        add_project_arguments(f'-DSAVE_@extension@')
    endif
  elif savable and get_option(f'SDLIMAGE_@extension@_SAVE').enabled()
    get_option(f'SDLIMAGE_@extension@_SAVE').disable_if(true, error_message: f'"SDLIMAGE_@extension@" must be enabled to enable saving')
  endif
endforeach

sdl3_image_lib = library('sdl3_image',
  sdl3_image_src,
  include_directories: 'include',
  dependencies: deps)

sdl3_image_dep = declare_dependency(include_directories: 'include',
  link_with: sdl3_image_lib)