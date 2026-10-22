if 'haptic' in enabled_subsystems
  if platform_is_windows
    cdata.set('SDL_HAPTIC_DINPUT', 1)
    subdir('windows')
  elif platform_is_apple
    cdata.set('SDL_HAPTIC_IOKIT', 1)
    subdir('darwin')
  else
    cdata.set('SDL_HAPTIC_LINUX', 1)
    subdir('linux')
  endif

  subdir('hidapi')
else
  subdir('dummy')
endif

sources += files('SDL_haptic.c')
