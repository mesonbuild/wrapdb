system_sources = files(
  'Clock.cpp',
  'Err.cpp',
  'FileInputStream.cpp',
  'Lock.cpp',
  'MemoryInputStream.cpp',
  'Mutex.cpp',
  'Sleep.cpp',
  'String.cpp',
  'Thread.cpp',
  'ThreadLocal.cpp',
  'Time.cpp',
)

if host_machine.system() == 'windows'
  system_sources += files(
    'Win32/ClockImpl.cpp',
    'Win32/MutexImpl.cpp',
    'Win32/SleepImpl.cpp',
    'Win32/ThreadImpl.cpp',
    'Win32/ThreadLocalImpl.cpp',
  )
else
  system_sources += files(
    'Unix/ClockImpl.cpp',
    'Unix/MutexImpl.cpp',
    'Unix/SleepImpl.cpp',
    'Unix/ThreadImpl.cpp',
    'Unix/ThreadLocalImpl.cpp',
  )
endif

thread_dep = dependency('threads')

system_lib = library(
  'sfml-system',
  system_sources,
  cpp_args: get_option('default_library') != 'static' ? '-DSFML_SYSTEM_EXPORTS' : '-DSFML_STATIC',
  include_directories: [pub_inc, priv_inc],
  dependencies: [thread_dep, winmm_dep],
  install: true
)

sfml_system_dep = declare_dependency(
  include_directories: pub_inc,
  link_with: system_lib,
  compile_args: get_option('default_library') == 'static' ? '-DSFML_STATIC' : [],
)

meson.override_dependency('sfml-system', sfml_system_dep)
