if platform_is_windows
  cdata.set('SDL_TIMER_WINDOWS', 1)
  subdir('windows')
else
  cdata.set('SDL_TIMER_UNIX', 1)
  subdir('unix')
endif

sources += files('SDL_timer.c')
