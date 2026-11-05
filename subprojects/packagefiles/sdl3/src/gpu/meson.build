if sdl_gpu
  available_gpu_drivers = {
    'd3d12': {},
    'metal': {},
    'vulkan': {},
  }
  gpu_drivers = ''

  if cdata.get('HAVE_DXGI1_6_H', 0) != 0
    gpu_drivers += ' d3d12'
  endif
  if cdata.get('SDL_VIDEO_METAL', 0) != 0
    gpu_drivers += ' metal'
  endif
  if cdata.get('SDL_VIDEO_VULKAN', 0) != 0
    gpu_drivers += ' vulkan'
  endif

  foreach gd : gpu_drivers.split()
    dir = available_gpu_drivers[gd].get('subdir', gd)
    gd_up = gd.to_upper()
    cdata.set10(f'SDL_GPU_@gd_up@', true)
    subdir(dir)
  endforeach
endif

sources += files('SDL_gpu.c')
