available_joysticks = {
  'dummy': {},
  'gameinput': {
    'subdir': 'gdk',
  },
  'hidapi': {},
  'iokit': {
    'subdir': 'darwin',
  },
  'linux': {},
  'mfi': {
    'subdir': 'apple',
  },
  'virtual': {},
  'windows': {},
}
joysticks = ''

if 'joystick' in enabled_subsystems
  if opt_joystick_hidapi.allowed()
    joysticks += ' hidapi'
  endif

  if platform_is_windows
    cdata.set10('SDL_JOYSTICK_RAWINPUT', true)
    cdata.set10('SDL_JOYSTICK_DINPUT', cdata.get('HAVE_DINPUT_H', 0) != 0)
    cdata.set10('SDL_JOYSTICK_XINPUT', cdata.get('HAVE_XINPUT_H', 0) != 0)
    cdata.set10(
      'SDL_JOYSTICK_WGI',
      cdata.get('HAVE_WINDOWS_GAMING_INPUT_H', 0) != 0,
    )
    if cdata.get('SDL_JOYSTICK_DINPUT', 0) != 0 or cdata.get(
      'SDL_JOYSTICK_XINPUT',
      0,
    ) != 0 or cdata.get(
      'SDL_JOYSTICK_WGI',
      0,
    ) != 0
      joysticks += ' windows'
    endif

    if cdata.get('HAVE_GAMEINPUT_H', 0) != 0
      joysticks += ' gameinput'
    endif
  elif platform_is_apple
    joysticks += ' iokit'
    joysticks += ' mfi'
  elif platform_is_linux
    joysticks += ' linux'
  endif
endif

if joysticks == ''
  joysticks += ' dummy'
endif
# Upstream also builds dummy joystick if only virtual is enabled
if 'joystick' in enabled_subsystems and opt_joystick_virtual.allowed()
  joysticks += ' virtual'
endif

sources += files(
  'controller_type.c',
  'SDL_gamepad.c',
  'SDL_joystick.c',
  'SDL_steam_virtual_gamepad.c',
)

foreach j : joysticks.split()
  dir = available_joysticks[j].get('subdir', j)
  j_up = j.to_upper()
  cdata.set10(f'SDL_JOYSTICK_@j_up@', true)
  subdir(dir)
endforeach
