if 'tray' in enabled_subsystems
  if platform_is_windows
    subdir('windows')
  elif platform_is_macos
    subdir('cocoa')
  else
    subdir('unix')
  endif
else
  cdata.set10('SDL_TRAY_DUMMY', true)
  subdir('dummy')
endif

sources += files('SDL_tray_utils.c')
