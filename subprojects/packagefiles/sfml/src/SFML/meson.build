subdir('System')
sfml_libs += system_lib

if host_machine.system() == 'windows'
  subdir('Main')
  sfml_libs += main_lib
endif

if get_option('window') or get_option('graphics')
  subdir('Window')
  sfml_libs += window_lib
endif

if get_option('network')
  subdir('Network')
  sfml_libs += network_lib
endif

if get_option('graphics')
  subdir('Graphics')
  sfml_libs += graphics_lib
endif

if get_option('audio')
  subdir('Audio')
  sfml_libs += audio_lib
endif
