if 'power' in enabled_subsystems
  if platform_is_windows
    subdir('windows')
  elif platform_is_macos
    subdir('macos')
  else
    subdir('linux')
  endif
endif

sources += files('SDL_power.c')
