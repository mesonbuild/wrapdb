if host_machine.system() == 'windows'
  cdata.set('SDL_JOYSTICK_DINPUT', 1)
  cdata.set('SDL_JOYSTICK_XINPUT', 1)
  subdir('hidapi')
  subdir('windows')
else
  cdata.set('SDL_JOYSTICK_LINUX', 1)
  subdir('linux')
endif

sources += files(
  'SDL_steam_virtual_gamepad.c',
  'SDL_joystick.c',
  'SDL_gamepad.c',
  'controller_type.c',
)
