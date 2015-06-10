testexe = executable('testbin',
  'util.c', 'write_read.c', 'test.c',
  include_directories : [incdir, ogg_inc],
  link_with : [vorbisenc_lib, vorbis_lib, ogg_lib],
  dependencies : ogg_dep,
)

test('vorbistest', testexe)
