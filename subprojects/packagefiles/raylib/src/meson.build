cc = meson.get_compiler('c')

if target_platform == 'GLFW'

  using_external_glfw = use_external_glfw.enabled()
  if use_external_glfw.allowed()
    glfw_dep = dependency(
      'glfw',
      required: use_external_glfw,
    )
    if glfw_dep.found()
      deps += glfw_dep
      using_external_glfw = true
    endif
  endif

  if host_machine.system() == 'linux' or host_is_msys2
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
          deps += wayland_deps_obj
        endif

      endif

    endif

    if not using_x11_glfw and not using_wayland_glfw
      error('Cannot disable both Wayland and X11')
    endif

    if using_x11_glfw
      compile_args += '-D_GLFW_X11'
    endif

    if using_wayland_glfw
      compile_args += '-D_GLFW_WAYLAND'

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

        src_files += custom_target(
          f'@protocol@ header',
          command: ['wayland-scanner', 'client-header', '@INPUT@', '@OUTPUT@'],
          input: file,
          output: f'@protocol@.h',
        )

        src_files += custom_target(
          f'@protocol@ code',
          command: ['wayland-scanner', 'private-code', '@INPUT@', '@OUTPUT@'],
          input: file,
          output: f'@protocol@-code.h',
        )

      endforeach

    endif

    deps += cc.find_library('m')
    deps += dependency('gl')
    deps += dependency('threads')
    deps += dependency('dl')
    deps += cc.find_library('rt')

    need_atomic_lib = not cc.has_function(
      'atomic_flag_clear',
      prefix: '#include <stdatomic.h>',
      dependencies: [cc.find_library('c')],
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

  if not using_external_glfw
    inc_dirs += include_directories('external/glfw/include')
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
    dependencies: [cc.find_library('c')],
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

if target_platform == 'GLFW' and not using_external_glfw
  if glfw_compile_flags.length() == 0
    src_files += files('rglfw.c')
  else
    glfw_external = static_library(
      'glfw_external',
      files('rglfw.c'),
      include_directories: inc_dirs,
      c_args: compile_args + glfw_compile_flags,
      dependencies: deps,
    )

    deps += declare_dependency(
      link_with: glfw_external,
    )
  endif
endif

inc_dirs += include_directories('.')
