project(
  'raylib',
  'c',
  version: '5.5',
  license: 'zlib',
  default_options: ['c_std=c99'],
  meson_version: '>=0.64.0',
)

# get all available options
platform = get_option('platform')

glfw_build_wayland = get_option('glfw_build_wayland')
glfw_build_x11 = get_option('glfw_build_x11')

forced_opengl_version = get_option('opengl_version')
use_external_glfw = get_option('use_external_glfw')

# resolve target platform
target_platform = platform

if platform == 'Desktop'
  target_platform = 'GLFW'
endif

# Define raylib graphics api depending on selected platform
if target_platform == 'GLFW' or target_platform == 'RGFW' or target_platform == 'SDL'
  graphics = 'OpenGL 3.3'
  if forced_opengl_version != 'off'
    graphics = f'OpenGL @forced_opengl_version@'
  endif
elif target_platform == 'DRM' or target_platform == 'Web' or target_platform == 'Android'
  graphics = 'OpenGL ES 2.0'
endif


graphics_define = 'GRAPHICS_API_' + graphics.replace('.', '').underscorify().to_upper()

target_platform_define = 'PLATFORM_' + target_platform.underscorify().to_upper()

if target_platform == 'GLFW' or target_platform == 'SDL' or target_platform == 'RGFW'
  target_platform_define = 'PLATFORM_DESKTOP_' + target_platform.underscorify().to_upper()
endif

compile_args = [f'-D@target_platform_define@', f'-D@graphics_define@']
private_compile_args = []

cc = meson.get_compiler('c')

compile_args += cc.get_supported_arguments('-fno-strict-aliasing')

is_shared_lib = get_option('default_library') == 'shared'

if is_shared_lib
  private_compile_args += '-DBUILD_LIBTYPE_SHARED'
  compile_args += '-DUSE_LIBTYPE_SHARED'
endif


if target_platform == 'DRM'
  # without EGL_NO_X11 eglplatform.h tears Xlib.h in which tears X.h in
  # which contains a conflicting type Font
  compile_args += '-DEGL_NO_X11'
endif

deps = []
src_files = []
inc_dirs = []

subdir('src')

raylib = library(
  'raylib',
  src_files,
  include_directories: inc_dirs,
  c_args: private_compile_args + compile_args,
  dependencies: deps,
  install: true,
  version: meson.project_version(),
  gnu_symbol_visibility: 'hidden',
)

raylib_dep = declare_dependency(
  link_with: raylib,
  dependencies: deps,
  include_directories: inc_dirs,
  compile_args: compile_args,
)

meson.override_dependency('raylib', raylib_dep)

if get_option('examples')
  subdir('examples')
endif
