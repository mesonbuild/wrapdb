if not get_option('programs')
  subdir_done()
endif

alsa_dep = dependency(
  'alsa',
  required: cdata.get('HAVE_ALSA_ASOUNDLIB_H', 0) == 1,
)
if alsa_dep.found()
  executable(
    'sndfile-play',
    'sndfile-play.c',
    'common.c',
    install: true,
    dependencies: [libsndfile_dep, libm_dep, alsa_dep, sndio_dep],
  )
endif

tests = [
  'sndfile-info',
  'sndfile-convert',
  'sndfile-cmp',
  'sndfile-metadata-set',
  'sndfile-metadata-get',
  'sndfile-interleave',
  'sndfile-deinterleave',
  'sndfile-concat',
  'sndfile-salvage',
]

foreach t : tests
  executable(
    t,
    '@0@.c'.format(t),
    'common.c',
    install: true,
    dependencies: [libsndfile_dep, libm_dep],
  )
endforeach
