subdir('gpu')
subdir('software')

if host_machine.system() == 'windows'
  subdir('direct3d12')
  subdir('vulkan')
else
  subdir('opengl')
  subdir('vulkan')
endif

sources += files(
  'SDL_render.c',
  'SDL_render_unsupported.c',
  'SDL_yuv_sw.c',
  'SDL_d3dmath.c',
)
