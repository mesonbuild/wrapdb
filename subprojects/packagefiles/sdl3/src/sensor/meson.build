if 'sensor' in enabled_subsystems
  if platform_is_windows
    subdir('windows')
  else
    subdir('dummy')
  endif
else
  subdir('dummy')
endif

sources += files('SDL_sensor.c')
