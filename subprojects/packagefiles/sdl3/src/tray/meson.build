if 'tray' in enabled_subsystems
  if host_machine.system() == 'windows'
    subdir('windows')
  elif host_machine.system() == 'darwin'
    subdir('cocoa')
  else
    subdir('unix')
  endif
else
  cdata.set10('SDL_TRAY_DUMMY', true)
  subdir('dummy')
endif

sources += files('SDL_tray_utils.c')
