enabled_render = ''
if sdl_render
  subdir('software')  # enabled via headers

  available_renderers = {
    'd3d': {
      'subdir': 'direct3d',
    },
    'd3d11': {
      'subdir': 'direct3d11',
    },
    'd3d12': {
      'subdir': 'direct3d12',
    },
    'gpu': {},
    'metal': {},
    'ogl': {
      'subdir': 'opengl',
    },
    'ogl_es2': {
      'subdir': 'opengles2',
    },
    'vulkan': {},
  }
  renderers = ''

  if opt_render_d3d.allowed()
    renderers += ' d3d'
  endif
  if opt_render_d3d11.allowed()
    renderers += ' d3d11'
  endif
  if opt_render_d3d12.allowed()
    renderers += ' d3d12'
  endif
  if opt_render_gpu.allowed()
    renderers += ' gpu'
  endif
  if opt_render_metal.allowed()
    renderers += ' metal'
  endif
  if opt_video_vulkan.allowed()
    renderers += ' vulkan'
  endif
  if cdata.get('SDL_VIDEO_OPENGL', 0) != 0
    renderers += ' ogl'
  endif
  if cdata.get('SDL_VIDEO_OPENGL_ES2', 0) != 0
    renderers += ' ogl_es2'
  endif

  foreach r : renderers.split()
    dir = available_renderers[r].get('subdir', r)
    r_up = r.to_upper()
    cdata.set10(f'SDL_VIDEO_RENDER_@r_up@', true)
    subdir(dir)
  endforeach

  foreach r : available_renderers.keys()
    r_up = r.to_upper()
    if cdata.get(f'SDL_VIDEO_RENDER_@r_up@', 0) != 0
      enabled_render += f'@r@ '
    endif
  endforeach
endif

sources += files('SDL_render.c', 'SDL_render_unsupported.c', 'SDL_yuv_sw.c')
