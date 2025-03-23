if not get_option('examples')
  subdir_done()
endif

add_languages('cpp')

executable(
  'sndfile-to-text',
  'sndfile-to-text.c',
  dependencies: libsndfile_dep,
)
executable(
  'sndfile-loopify',
  'sndfile-loopify.c',
  dependencies: libsndfile_dep,
)
executable(
  'make_sine',
  'make_sine.c',
  dependencies: [libsndfile_dep, libm_dep],
)
executable(
  'sfprocess',
  'sfprocess.c',
  dependencies: libsndfile_dep,
)
executable(
  'list_formats',
  'list_formats.c',
  dependencies: libsndfile_dep,
)
executable(
  'generate',
  'generate.c',
  dependencies: libsndfile_dep,
)
executable(
  'sndfilehandle',
  'sndfilehandle.cc',
  dependencies: libsndfile_dep,
)
