if 'dialog' in enabled_subsystems
  if platform_is_windows
    subdir('windows')
  elif platform_is_macos
    subdir('cocoa')
  else
    subdir('unix')
  endif
endif

sources += files('SDL_dialog.c', 'SDL_dialog_utils.c')
