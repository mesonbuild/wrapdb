if 'gpu' in enabled_subsystems
  if platform_is_windows
    subdir('d3d12')
    subdir('vulkan')
  elif platform_is_apple
    subdir('metal')
    subdir('vulkan')
  else
    subdir('vulkan')
  endif
endif

sources += files('SDL_gpu.c')
