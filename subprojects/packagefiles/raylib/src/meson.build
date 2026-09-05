cc = meson.get_compiler('c')

if target_platform == 'GLFW'
  deps += dependency('glfw3')

  if host_machine.system() == 'linux'

    deps += cc.find_library('m')
    deps += dependency('gl')
    deps += dependency('threads')
    deps += dependency('dl')
    deps += cc.find_library('rt')

    need_atomic_lib = not cc.has_function(
      'atomic_flag_clear',
      prefix: '#include <stdatomic.h>',
      dependencies: [],
    )
    deps += cc.find_library(
      'atomic',
      required: need_atomic_lib,
    )

  elif host_machine.system() == 'windows'

    deps += cc.find_library('opengl32')
    deps += cc.find_library('winmm')
    deps += cc.find_library('gdi32')

  elif host_machine.system() == 'darwin'

    deps += dependency('OpenGL')
    deps += dependency('Cocoa')
    deps += dependency('IOKit')
    deps += dependency('CoreAudio')
    deps += dependency('CoreVideo')


  endif

elif target_platform == 'SDL'
  deps += dependency('SDL2', 'sdl2')
elif target_platform == 'Web'
  inc_dirs += include_directories('external/glfw/include')
elif target_platform == 'DRM'
  deps += dependency('drm')
  deps += dependency('GLESv2')
  deps += dependency('EGL')
  deps += dependency('gbm')
  deps += dependency('threads')
  deps += cc.find_library('m')
  deps += dependency('dl')
  deps += cc.find_library('rt')

  need_atomic_lib = not cc.has_function(
    'atomic_flag_clear',
    prefix: '#include <stdatomic.h>',
    dependencies: [],
  )
  deps += cc.find_library(
    'atomic',
    required: need_atomic_lib,
  )

elif target_platform == 'Android'
  #TODO: add support
  error('Atm not supported in this meson port')
elif target_platform == 'RGFW'

  if host_machine.system() == 'linux'

    deps += dependency('gl')
    deps += dependency('Xrandr')
    deps += dependency('Xinerama')
    deps += dependency('Xi')
    deps += dependency('Xcursor')
    deps += dependency('threads')
    deps += cc.find_library('m')
    deps += dependency('dl')
    deps += cc.find_library('rt')

  elif host_machine.system() == 'windows'

    deps += cc.find_library('opengl32')
    deps += cc.find_library('winmm')
    deps += cc.find_library('gdi32')

  elif host_machine.system() == 'darwin'

    deps += dependency('Foundation')
    deps += dependency('AppKit')
    deps += dependency('OpenGL')
    deps += dependency('CoreVideo')

  endif

endif

src_files += files(
  'raudio.c',
  'rcore.c',
  'rmodels.c',
  'rshapes.c',
  'rtext.c',
  'rtextures.c',
  'utils.c',
)

inc_dirs += include_directories('.')
