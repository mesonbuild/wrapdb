if platform_is_windows
  subdir('windows')
elif cdata.get('SDL_LOADSO_DLOPEN', 0) != 0
  subdir('dlopen')
else
  subdir('dummy')
endif
