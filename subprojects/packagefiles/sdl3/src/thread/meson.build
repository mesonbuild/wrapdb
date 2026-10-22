#subdir('generic')

if platform_is_windows
  subdir('windows')
else
  subdir('pthread')
endif

sources += files('SDL_thread.c')
