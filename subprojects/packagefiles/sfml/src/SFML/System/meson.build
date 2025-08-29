system_sources = files(
  'Clock.cpp',
  'Err.cpp',
  'FileInputStream.cpp',
  'MemoryInputStream.cpp',
  'Sleep.cpp',
  'String.cpp',
  'Utils.cpp',
  'Vector2.cpp',
  'Vector3.cpp',
)

if host_machine.system() == 'windows'
  system_sources += files('Win32/SleepImpl.cpp')
else
  system_sources += files('Unix/SleepImpl.cpp')
endif

system_lib = library(
  'sfml-system',
  system_sources,
  cpp_args: get_option('default_library') != 'static' ? '-DSFML_SYSTEM_EXPORTS' : '-DSFML_STATIC',
  include_directories: [pub_inc, priv_inc],
  dependencies: [thread_dep, winmm_dep],
)
