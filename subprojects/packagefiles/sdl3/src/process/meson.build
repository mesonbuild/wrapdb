if platform_is_windows
  cdata.set('SDL_PROCESS_WINDOWS', 1)
  subdir('windows')
else
  cdata.set('SDL_PROCESS_POSIX', 1)
  subdir('posix')
endif

sources += files('SDL_process.c')
