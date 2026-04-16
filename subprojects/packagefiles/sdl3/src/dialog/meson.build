if host_machine.system() == 'windows'
  subdir('windows')
elif host_machine.system() == 'darwin'
  subdir('cocoa')
else
  subdir('unix')
endif

sources += files('SDL_dialog.c', 'SDL_dialog_utils.c')
