available_cameras = {
  'coremedia': {},
  'dummy': {},
  'mediafoundation': {},
  'pipewire': {},
}
cameras = ''

if sdl_camera
  if have_pipewire
    cameras += ' pipewire'
    dlopen_table += {
      'option': opt_pipewire_shared,
      'dep_var': 'pipewire_dep',
      'lib': 'pipewire-0.3',
      'conf_var': 'SDL_CAMERA_DRIVER_PIPEWIRE_DYNAMIC',
    }
  endif

  if cdata.get('HAVE_MFAPI_H', 0) != 0
    cameras += ' mediafoundation'
  endif

  if platform_is_apple
    cameras += ' coremedia'
  endif
endif

if opt_camera_dummy.allowed() or cameras == ''
  cameras += ' dummy'
endif

sources += files('SDL_camera.c')

foreach c : cameras.split()
  dir = available_cameras[c].get('subdir', c)
  c_up = c.to_upper()
  cdata.set10(f'SDL_CAMERA_DRIVER_@c_up@', true)
  subdir(dir)
endforeach

enabled_camera = ''
foreach c : available_cameras.keys()
  c_up = c.to_upper()
  if cdata.get(f'SDL_CAMERA_DRIVER_@c_up@', 0) != 0
    enabled_camera += f'@c@ '
  endif
endforeach
