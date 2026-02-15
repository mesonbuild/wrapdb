subdir('System')
csfml_libs += system_lib

if host_machine.system() == 'windows'
  subdir('Main')
  csfml_libs += main_lib
endif

if get_option('window') or get_option('graphics')
  subdir('Window')
  csfml_libs += window_lib
endif

if get_option('network')
  subdir('Network')
  csfml_libs += network_lib
endif

if get_option('graphics')
  subdir('Graphics')
  csfml_libs += graphics_lib
endif

if get_option('audio')
  subdir('Audio')
  csfml_libs += audio_lib
endif
