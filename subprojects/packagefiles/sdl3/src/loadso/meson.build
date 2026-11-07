if platform_is_windows
  loadso = 'windows'
elif cdata.get('HAVE_DLOPEN', 0) != 0
  loadso = 'dlopen'
else
  loadso = 'dummy'
endif

loadso_up = loadso.to_upper()
cdata.set10(f'SDL_LOADSO_@loadso_up@', true)
subdir(loadso)
