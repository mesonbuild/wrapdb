sources += files('SDL_locale.c')

if platform_is_windows
  subdir('windows')
elif platform_is_apple
  subdir('macos')
elif platform_is_linux
  subdir('unix')
else
  error('Platform not supported yet.')
endif
