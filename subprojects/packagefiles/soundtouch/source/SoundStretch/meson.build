soundstretch_sources = files('RunParameters.cpp', 'WavFile.cpp', 'main.cpp')

if get_option('soundstretch')
  soundstretch_bin = executable(
    'soundstretch',
    soundstretch_sources,
    cpp_args: soundtouch_args,
    include_directories: include_directories('.'),
    dependencies: soundtouch_dep,
    install: true,
  )
endif
