if 'render' in enabled_subsystems
  subdir('gpu')
  subdir('software')

  if platform_is_windows
    subdir('direct3d12')
    subdir('opengl')
    subdir('vulkan')
  elif platform_is_apple
    subdir('metal')
    subdir('vulkan')
  else
    subdir('opengl')
    subdir('vulkan')
  endif
endif

sources += files('SDL_render.c', 'SDL_render_unsupported.c', 'SDL_yuv_sw.c')
