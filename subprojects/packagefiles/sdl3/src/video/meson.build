subdir('yuv2rgb')

if host_machine.system() == 'windows'
  cdata.set('SDL_VIDEO_DRIVER_WINDOWS', 1)
  subdir('windows')
elif host_machine.system() == 'darwin'
  subdir('cocoa')
else
  cdata.set('SDL_VIDEO_DRIVER_WAYLAND', 1)
  subdir('wayland')
  x11_dep = dependency('x11')
  xext_dep = dependency('xext')

  if x11_dep.found() and xext_dep.found()
    sdl_deps += x11_dep
    sdl_deps += xext_dep
    cdata.set('SDL_VIDEO_DRIVER_X11', 1)
    subdir('x11')
  endif
endif

sources += files(
  'SDL_RLEaccel.c',
  'SDL_blit.c',
  'SDL_blit_0.c',
  'SDL_blit_1.c',
  'SDL_blit_A.c',
  'SDL_blit_N.c',
  'SDL_blit_auto.c',
  'SDL_blit_copy.c',
  'SDL_blit_slow.c',
  'SDL_bmp.c',
  'SDL_clipboard.c',
  'SDL_egl.c',
  'SDL_fillrect.c',
  'SDL_pixels.c',
  'SDL_rect.c',
  'SDL_stb.c',
  'SDL_stretch.c',
  'SDL_surface.c',
  'SDL_video.c',
  'SDL_video_unsupported.c',
  'SDL_vulkan_utils.c',
  'SDL_yuv.c',
)
