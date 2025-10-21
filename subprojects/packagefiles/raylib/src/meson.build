cc = meson.get_compiler('c')

_do_not_use_internal_glfw_dep = disabler()

if target_platform == 'GLFW'

  using_external_glfw = use_external_glfw.enabled()
  if use_external_glfw.allowed()
    glfw_dep = dependency(
      'glfw3',
      required: use_external_glfw,
    )
    if glfw_dep.found()
      deps += glfw_dep
      using_external_glfw = true
      _do_not_use_internal_glfw_dep = glfw_dep
    else
      using_external_glfw = false
      message('using internal glfw')
    endif
  endif

  glfw_deps = []
  glfw_inc_dirs = []
  glfw_c_args = []
  glfw_private_c_args = []
  glfw_src_files = []

  if host_machine.system() == 'linux'
    using_x11_glfw = glfw_build_x11.enabled()

    if glfw_build_x11.allowed()

      x11_deps = [
        ['X11', 'x11'],
        ['Xcursor', 'xcursor'],
        ['Xext', 'xext'],
        ['Xfixes', 'xfixes'],
        ['Xi', 'xi'],
        ['Xinerama', 'xinerama'],
        ['Xrandr', 'xrandr'],
        ['Xrender', 'xrender'],
      ]

      x11_deps_obj = []

      foreach x11_dep : x11_deps
        resolved_x11_dep = dependency(
          x11_dep,
          required: glfw_build_x11,
        )

        if resolved_x11_dep.found()
          x11_deps_obj += resolved_x11_dep
          using_x11_glfw = true
        elif glfw_build_wayland.auto()
          using_x11_glfw = false
          break
        endif
      endforeach

      if using_x11_glfw
        glfw_deps += x11_deps_obj
      endif

    endif

    using_wayland_glfw = glfw_build_wayland.enabled()

    if glfw_build_wayland.allowed()
      wayland_deps = [
        'wayland-client',
        'wayland-cursor',
        'wayland-egl',
        'xkbcommon',
      ]
      wayland_deps_obj = []

      foreach wayland_dep : wayland_deps
        resolved_wayland_dep = dependency(
          wayland_dep,
          required: glfw_build_wayland,
        )
        if resolved_wayland_dep.found()
          wayland_deps_obj += resolved_wayland_dep
          using_wayland_glfw = true
        elif glfw_build_wayland.auto()
          using_wayland_glfw = false
          break
        endif
      endforeach

      if using_wayland_glfw
        wl_scanner = find_program(
          'wayland-scanner',
          required: glfw_build_wayland,
          native: true,
        )

        if not wl_scanner.found()
          using_wayland_glfw = false
        else
          glfw_deps += wayland_deps_obj
        endif

      endif

    endif

    if not using_x11_glfw and not using_wayland_glfw
      error('Cannot disable both Wayland and X11')
    endif

    if using_x11_glfw
      glfw_c_args += '-D_GLFW_X11'
    endif

    if using_wayland_glfw
      glfw_c_args += '-D_GLFW_WAYLAND'

      wl_protocols_dir = meson.project_source_root() / 'src' / 'external' / 'glfw' / 'deps' / 'wayland'

      wl_generate_list = [
        {
          'file': wl_protocols_dir / 'wayland.xml',
          'protocol': 'wayland-client-protocol',
        },
        {
          'file': wl_protocols_dir / 'xdg-shell.xml',
          'protocol': 'xdg-shell-client-protocol',
        },
        {
          'file': wl_protocols_dir / 'xdg-decoration-unstable-v1.xml',
          'protocol': 'xdg-decoration-unstable-v1-client-protocol',
        },
        {
          'file': wl_protocols_dir / 'viewporter.xml',
          'protocol': 'viewporter-client-protocol',
        },
        {
          'file': wl_protocols_dir / 'relative-pointer-unstable-v1.xml',
          'protocol': 'relative-pointer-unstable-v1-client-protocol',
        },
        {
          'file': wl_protocols_dir / 'pointer-constraints-unstable-v1.xml',
          'protocol': 'pointer-constraints-unstable-v1-client-protocol',
        },
        {
          'file': wl_protocols_dir / 'fractional-scale-v1.xml',
          'protocol': 'fractional-scale-v1-client-protocol',
        },
        {
          'file': wl_protocols_dir / 'xdg-activation-v1.xml',
          'protocol': 'xdg-activation-v1-client-protocol',
        },
        {
          'file': wl_protocols_dir / 'idle-inhibit-unstable-v1.xml',
          'protocol': 'idle-inhibit-unstable-v1-client-protocol',
        },
      ]

      wl_scanner = find_program(
        'wayland-scanner',
        native: true,
      )

      foreach wl_generate_item : wl_generate_list
        file = wl_generate_item.get('file')
        protocol = wl_generate_item.get('protocol')

        glfw_src_files += custom_target(
          f'@protocol@ header',
          command: ['wayland-scanner', 'client-header', '@INPUT@', '@OUTPUT@'],
          input: file,
          output: f'@protocol@.h',
        )

        glfw_src_files += custom_target(
          f'@protocol@ code',
          command: ['wayland-scanner', 'private-code', '@INPUT@', '@OUTPUT@'],
          input: file,
          output: f'@protocol@-code.h',
        )

      endforeach

    endif

    glfw_deps += cc.find_library('m')
    glfw_deps += dependency('gl')
    glfw_deps += dependency('threads')
    glfw_deps += dependency('dl')
    glfw_deps += cc.find_library('rt')

    need_atomic_lib = not cc.has_function(
      'atomic_flag_clear',
      prefix: '#include <stdatomic.h>',
      dependencies: [cc.find_library('c')],
    )
    glfw_deps += cc.find_library(
      'atomic',
      required: need_atomic_lib,
    )

  elif host_machine.system() == 'windows'

    glfw_deps += cc.find_library('opengl32')
    glfw_deps += cc.find_library('winmm')
    glfw_deps += cc.find_library('gdi32')

  elif host_machine.system() == 'darwin'

    glfw_deps += dependency('OpenGL')
    glfw_deps += dependency('Cocoa')
    glfw_deps += dependency('IOKit')
    glfw_deps += dependency('CoreAudio')
    glfw_deps += dependency('CoreVideo')

  endif

  if not using_external_glfw
    glfw_inc_dirs += include_directories('external/glfw/include')
    glfw_src_files += files('rglfw.c')
    glfw_private_c_args += '-D_GLFW_BUILD_DLL'

    if host_machine.system() == 'darwin'
      add_languages(
        'objc',
        native: true,
      )
      glfw_private_c_args += ['-x', 'objective-c']
    endif

  endif

  deps += glfw_deps
  inc_dirs += glfw_inc_dirs
  compile_args += glfw_c_args
  private_compile_args += glfw_private_c_args
  src_files += glfw_src_files

  if not using_external_glfw and get_option('examples')
    ## reuse this in the examples

    glfw_inc_dirs += include_directories('.')

    _do_not_use_internal_glfw_lib = library(
      'rglfw',
      glfw_src_files,
      include_directories: glfw_inc_dirs,
      c_args: glfw_private_c_args + glfw_c_args,
      dependencies: glfw_deps,
    )

    _do_not_use_internal_glfw_dep = declare_dependency(
      link_with: _do_not_use_internal_glfw_lib,
      dependencies: glfw_deps,
      include_directories: glfw_inc_dirs,
      compile_args: glfw_c_args,
    )
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
