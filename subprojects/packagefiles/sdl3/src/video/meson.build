available_video_drivers = {
  'cocoa': {},
  'dummy': {},
  'kmsdrm': {},
  'offscreen': {},
  'rpi': {
    'subdir': 'raspberry',
  },
  'uikit': {},
  'vivante': {},
  'wayland': {},
  'windows': {},
  'x11': {},
}
video_drivers = ''

subdir('yuv2rgb')

if sdl_video
  want_egl = opt_video_opengl.allowed() or opt_video_opengles.allowed() or opt_video_vivante.allowed()

  if opt_video_rpi.allowed()
    bcm_host_dep = dependency(
      'bcm_host',
      required: opt_video_rpi,
    )
    brcmegl_dep = dependency(
      'brcmegl',
      required: opt_video_rpi,
    )
    sdl_deps += [bcm_host_dep, brcmegl_dep]
    if bcm_host_dep.found() and brcmegl_dep.found()
      video_drivers += ' rpi'
    endif
  endif

  if opt_video_rockchip.allowed()
    mali_dep = dependency(
      'mali',
      required: opt_video_rockchip,
    )
    sdl_deps += mali_dep
    if mali_dep.found()
      video_drivers += ' rockchip'
    endif
  endif

  if want_egl
    # check Kronos EGL support
    have_opengl_egl_code = '''
      #define EGL_API_FB
      #define MESA_EGL_NO_X11_HEADERS
      #define EGL_NO_X11
      #include <EGL/egl.h>
      #include <EGL/eglext.h>
      int main (int argc, char** argv) { return 0; }
    '''
    egl_dep = dependency(
      'egl',
      required: false,
    )
    have_opengl_egl = egl_dep.found() and cc.compiles(
      have_opengl_egl_code,
      name: 'have OpenGL EGL support',
      dependencies: egl_dep,
    )
    if have_opengl_egl
      sdl_deps += egl_dep
      cdata.set10('SDL_VIDEO_OPENGL_EGL', have_opengl_egl)
    endif
  endif

  if opt_video_x11.enable_auto_if(platform_is_unixlike).enabled()
    x11_dep = dependency(
      'x11',
      required: opt_video_x11,
    )
    xext_dep = dependency(
      'xext',
      required: opt_video_x11,
    )
    # xproto is required for some XInput2 functions
    xproto_dep = dependency(
      'xproto',
      required: opt_video_x11,
    )

    if x11_dep.found() and xext_dep.found() and xproto_dep.found()
      sdl_deps += x11_dep
      sdl_deps += xext_dep
      sdl_deps += xproto_dep
      video_drivers += ' x11'
      dlopen_table += {
        'option': opt_video_x11_shared,
        'dep_var': 'x11_dep',
        'lib': 'X11',
        'conf_var': 'SDL_VIDEO_DRIVER_X11_DYNAMIC',
      }
      dlopen_table += {
        'option': opt_video_x11_shared,
        'dep_var': 'xext_dep',
        'lib': 'Xext',
        'conf_var': 'SDL_VIDEO_DRIVER_X11_DYNAMIC_XEXT',
      }
    endif
  endif

  if opt_video_wayland.enable_auto_if(platform_is_unixlike).enabled()
    wayland_client_dep = dependency(
      'wayland-client',
      required: opt_video_wayland,
    )
    wayland_egl_dep = dependency(
      'wayland-egl',
      required: opt_video_wayland,
    )
    wayland_cursor_dep = dependency(
      'wayland-cursor',
      required: opt_video_wayland,
    )
    xkbcommon_dep = dependency(
      'xkbcommon',
      required: opt_video_wayland,
    )
    if wayland_client_dep.found() and wayland_egl_dep.found() and wayland_cursor_dep.found() and xkbcommon_dep.found()
      sdl_deps += wayland_client_dep
      sdl_deps += wayland_egl_dep
      sdl_deps += wayland_cursor_dep
      sdl_deps += xkbcommon_dep
      video_drivers += ' wayland'
      dlopen_table += {
        'option': opt_video_wayland_shared,
        'dep_var': 'wayland_client_dep',
        'lib': 'wayland-client',
        'conf_var': 'SDL_VIDEO_DRIVER_WAYLAND_DYNAMIC',
      }
      dlopen_table += {
        'option': opt_video_wayland_shared,
        'dep_var': 'wayland_egl_dep',
        'lib': 'wayland-egl',
        'conf_var': 'SDL_VIDEO_DRIVER_WAYLAND_DYNAMIC_EGL',
      }
      dlopen_table += {
        'option': opt_video_wayland_shared,
        'dep_var': 'wayland_cursor_dep',
        'lib': 'wayland-cursor',
        'conf_var': 'SDL_VIDEO_DRIVER_WAYLAND_DYNAMIC_CURSOR',
      }
      dlopen_table += {
        'option': opt_video_wayland_shared,
        'dep_var': 'xkbcommon_dep',
        'lib': 'xkbcommon',
        'conf_var': 'SDL_VIDEO_DRIVER_WAYLAND_DYNAMIC_XKBCOMMON',
      }
    endif
  endif

  if opt_video_kmsdrm.enable_auto_if(platform_is_unixlike).enabled()
    libdrm_dep = dependency(
      'kmsdrm',
      required: opt_video_kmsdrm,
    )
    gbm_dep = dependency(
      'gbm',
      required: opt_video_kmsdrm,
    )
    if libdrm_dep.found() and gbm_dep.found()
      sdl_deps += libdrm_dep
      sdl_deps += gbm_dep
      video_drivers += ' kmsdrm'
      dlopen_table += {
        'option': use_video_kmsdrm_shared,
        'dep_var': 'libdrm_dep',
        'lib': 'drm',
        'conf_var': 'SDL_VIDEO_DRIVER_KMSDRM_DYNAMIC',
      }
      dlopen_table += {
        'option': use_video_kmsdrm_shared,
        'dep_var': 'gbm_dep',
        'lib': 'gbm',
        'conf_var': 'SDL_VIDEO_DRIVER_KMSDRM_DYNAMIC_GBM',
      }
    endif
  endif

  if opt_video_offscreen.allowed()
    video_drivers += ' offscreen'
  endif

  if opt_video_vivante.allowed()
    have_vivante_vdk = cc.has_header('gc_vdk.h')
    have_vivante_egl_fb = cc.has_header(
      'EGL/eglvivante.h',
      prefix: '''#define LINUX
      #define EGL_API_FB''',
    )
    if opt_video_vivante.require(have_vivante_vdk or have_vivante_egl_fb).allowed()
      if have_vivante_vdk
        vivante_dep = dependency('vivante', 'drm_vivante')
        sdl_deps += vivante_dep
      else
        add_project_arguments(
          '-DLINUX',
          '-DEGL_API_FB',
          language: 'c',
        )
      endif
      video_drivers += ' vivante'
    endif
  endif

  if platform_is_unixlike
    if opt_video_opengl.allowed()
      # check OpenGL support
      have_opengl_code = '''
        #include <GL/gl.h>
        #include <GL/glext.h>
        int main(int argc, char** argv) { return 0; }
      '''
      have_opengl = cc.compiles(
        have_opengl_code,
        name: 'have OpenGL support',
        required: opt_video_opengl,
      )
      cdata.set10('SDL_VIDEO_OPENGL', have_opengl)
    endif
    if opt_video_opengles.allowed()
      have_glesv1 = cc.compiles(
        '''
          #include <GLES/gl.h>
          #include <GLES/glext.h>
          int main (int argc, char** argv) { return 0; }
        ''',
        name: 'have GLESv1 support',
        required: opt_video_opengles,
      )
      cdata.set10('SDL_VIDEO_OPENGL_ES', have_glesv1)
      have_glesv2 = cc.compiles(
        '''
          #include <GLES2/gl2.h>
          #include <GLES2/gl2ext.h>
          int main (int argc, char** argv) { return 0; }
        ''',
        name: 'have GLESv2 support',
        required: opt_video_opengles,
      )
      cdata.set10('SDL_VIDEO_OPENGL_ES2', have_glesv2)
    endif
  endif

  if platform_is_windows
    video_drivers += ' windows'

    cdata.set10('SDL_VIDEO_OPENGL', opt_video_opengl.allowed())
    cdata.set10('SDL_VIDEO_OPENGL_WGL', opt_video_opengl.allowed())
  endif
  if opt_video_cocoa.allowed()
    video_drivers += ' cocoa'

    cdata.set10('SDL_VIDEO_OPENGL', opt_video_opengl.allowed())
    cdata.set10('SDL_VIDEO_OPENGL_CGL', opt_video_opengl.allowed())
  endif
  if platform_is_ios
    video_drivers += ' uikit'
  endif
endif

cdata.set10('SDL_VIDEO_VULKAN', opt_video_vulkan.allowed())

if opt_video_dummy.allowed() or video_drivers == ''
  video_drivers += ' dummy'
endif

sources += files(
  'SDL_blit.c',
  'SDL_blit_0.c',
  'SDL_blit_1.c',
  'SDL_blit_A.c',
  'SDL_blit_auto.c',
  'SDL_blit_copy.c',
  'SDL_blit_N.c',
  'SDL_blit_slow.c',
  'SDL_bmp.c',
  'SDL_clipboard.c',
  'SDL_egl.c',
  'SDL_fillrect.c',
  'SDL_pixels.c',
  'SDL_rect.c',
  'SDL_RLEaccel.c',
  'SDL_rotate.c',
  'SDL_stb.c',
  'SDL_stretch.c',
  'SDL_surface.c',
  'SDL_video.c',
  'SDL_video_unsupported.c',
  'SDL_vulkan_utils.c',
  'SDL_yuv.c',
)

foreach vd : video_drivers.split()
  dir = available_video_drivers[vd].get('subdir', vd)
  vd_up = vd.to_upper()
  cdata.set10(f'SDL_VIDEO_DRIVER_@vd_up@', true)
  subdir(dir)
endforeach
