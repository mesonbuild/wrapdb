if cdata.get('SDL_THREAD_WINDOWS', 0) != 0
  subdir('windows')
elif cdata.get('SDL_THREAD_PTHREAD', 0) != 0
  subdir('pthread')
else
  subdir('generic')
endif

sources += files('SDL_thread.c')
