if host_machine.system() == 'windows'
  subdir('windows')
else
  subdir('unix')
  subdir('linux')
endif

sources += files(
  'SDL_core_unsupported.c',
)
