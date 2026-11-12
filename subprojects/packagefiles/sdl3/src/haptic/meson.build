available_haptic = {
  'dinput': {
    'subdir': 'windows',
  },
  'dummy': {},
  'iokit': {
    'subdir': 'darwin',
  },
  'linux': {},
}
haptic = ''

if 'haptic' in enabled_subsystems
  if platform_is_unixlike and cdata.get('HAVE_LINUX_INPUT_H', 0) != 0
    haptic += ' linux'
  endif

  if platform_is_apple
    haptic += ' iokit'
  endif

  if platform_is_windows and cdata.get('HAVE_DINPUT_H', 0) != 0
    haptic += ' dinput'
  endif

  subdir('hidapi')
endif

if haptic == ''
  haptic += ' dummy'
endif

sources += files('SDL_haptic.c')

foreach h : haptic.split()
  dir = available_haptic[h].get('subdir', h)
  h_up = h.to_upper()
  cdata.set10(f'SDL_HAPTIC_@h_up@', true)
  subdir(dir)
endforeach

enabled_haptic = ''
foreach h : available_haptic.keys()
  h_up = h.to_upper()
  if cdata.get(f'SDL_HAPTIC_@h_up@', 0) != 0
    enabled_haptic += f'@h@ '
  endif
endforeach
