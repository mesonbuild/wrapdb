if sdl_hidapi
  if platform_is_windows
    subdir('windows')
  elif platform_is_macos
    #  subdir('mac')
  else
    subdir('linux')
  endif
endif

sources += files('SDL_hidapi.c')
