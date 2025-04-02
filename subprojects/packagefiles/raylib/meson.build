project(
  'raylib',
  'c',
  version: '5.5',
  license: 'zlib',
  default_options: ['c_std=none'],
  meson_version: '>=1.1.0',
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

glfw_compile_flags = []

# define some flags based on OS
if target_platform == 'GLFW'
  if host_machine.system() == 'darwin'
    add_languages(
      'objc',
      native: true,
    )
    glfw_compile_flags = ['-x', 'objective-c']
  endif
endif

graphics_define = 'GRAPHICS_API_' + graphics.replace('.', '').underscorify().to_upper()

target_platform_define = 'PLATFORM_' + target_platform.underscorify().to_upper()

if target_platform == 'GLFW' or target_platform == 'SDL' or target_platform == 'RGFW'
  target_platform_define = 'PLATFORM_DESKTOP_' + target_platform.underscorify().to_upper()
endif

compile_args = [f'-D@target_platform_define@', f'-D@graphics_define@']
public_compile_args = []

cc = meson.get_compiler('c')

compile_args += cc.get_supported_arguments('-fno-strict-aliasing')

# Detect if compiling in an MSYS2-based MinGW/Clang environment
host_is_msys2 = host_machine.system() == 'windows' and cc.get_argument_syntax() == 'gcc'

is_shared_lib = get_option('default_library') == 'shared'

if is_shared_lib
  compile_args += '-DBUILD_LIBTYPE_SHARED'
  public_compile_args += '-DUSE_LIBTYPE_SHARED'
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
  c_args: compile_args,
  dependencies: deps,
  install: true,
  version: meson.project_version(),
  gnu_symbol_visibility: 'hidden',
)

raylib_dep = declare_dependency(
  link_with: raylib,
  dependencies: deps,
  include_directories: inc_dirs,
  compile_args: public_compile_args,
)

meson.override_dependency('raylib', raylib_dep)

if get_option('examples')
  subdir('examples')
endif
