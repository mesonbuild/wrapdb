if platform_is_windows
  subdir('windows')
elif platform_is_apple
  subdir('unix')
else
  subdir('unix')
  subdir('linux')
endif

sources += files('SDL_core_unsupported.c')
