if 'joystick' in enabled_subsystems
  if platform_is_windows
    cdata.set('SDL_JOYSTICK_DINPUT', 1)
    cdata.set('SDL_JOYSTICK_HIDAPI', 1)
    subdir('hidapi')
    subdir('windows')
    subdir('gdk')
  elif platform_is_macos
    cdata.set('SDL_JOYSTICK_IOKIT', 1)
    cdata.set('SDL_JOYSTICK_MFI', 1)
    subdir('apple')
    subdir('darwin')
  else
    cdata.set('SDL_JOYSTICK_LINUX', 1)
    subdir('linux')
  endif
else
  subdir('dummy')
endif

subdir('virtual')
cdata.set('SDL_JOYSTICK_VIRTUAL', 1)

sources += files(
  'controller_type.c',
  'SDL_gamepad.c',
  'SDL_joystick.c',
  'SDL_steam_virtual_gamepad.c',
)
