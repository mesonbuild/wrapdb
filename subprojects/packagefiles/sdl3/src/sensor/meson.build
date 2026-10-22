if 'sensor' in enabled_subsystems
  if host_machine.system() == 'windows'
    subdir('windows')
  else
    subdir('dummy')
  endif
else
  subdir('dummy')
endif

sources += files('SDL_sensor.c')
