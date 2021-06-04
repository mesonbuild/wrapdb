c_args = meson.get_compiler('c').get_id() == 'msvc' ? ['-D_USE_MATH_DEFINES'] : []

testexe = executable('testbin',
  'util.c', 'write_read.c', 'test.c',
  c_args: c_args,
  dependencies : [vorbisenc_dep, vorbis_dep, ogg_dep],
)

test('vorbistest', testexe)
