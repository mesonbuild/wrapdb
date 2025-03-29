soundtouch_dll_sources = files('SoundTouchDLL.cpp')

soundtouch_dll_includes = files('SoundTouchDLL.h')

soundtouch_dll_include_directories = [include_directories('.')]

windows = import('windows')

if system in ['windows', 'cygwin']
  if not cpp.has_header('afxres.h')
    # Work around lack of afxres.h (ATL/MFC component missing in MSVS)
    soundtouch_dll_include_directories += [include_directories('meson')]
  endif

  soundtouch_dll_sources += windows.compile_resources(
    files('SoundTouchDLL.rc'),
    include_directories: soundtouch_dll_include_directories,
  )
endif

if get_option('soundtouch_dll')
  soundtouch_dll_args = [soundtouch_args, '-DDLL_EXPORTS']

  soundtouch_dll_lib = shared_library(
    'SoundTouchDLL',
    soundtouch_dll_sources,
    cpp_args: soundtouch_dll_args,
    include_directories: soundtouch_dll_include_directories,
    dependencies: soundtouch_dep,
    gnu_symbol_visibility: 'inlineshidden',
  )

  soundtouch_dll_dep = declare_dependency(
    link_with: soundtouch_dll_lib,
  )

  install_headers(
    soundtouch_dll_includes,
    subdir: 'soundtouch',
  )
endif
