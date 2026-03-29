sources += files('SDL_locale.c')

if host_machine.system() == 'windows'
  subdir('windows')
elif host_machine.system() == 'darwin'
  subdir('macos')
elif host_machine.system() == 'linux'
  subdir('unix')
else
  error('Platform not supported yet.')
endif
