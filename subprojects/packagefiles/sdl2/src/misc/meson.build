all_sources += files(
  'SDL_url.c',
)

if host_machine.system() == 'windows'
  subdir('windows')
elif host_machine.system() == 'linux'
  subdir('unix')
elif host_machine.system() == 'darwin'
  subdir('macosx')
else
  subdir('dummy')
endif
