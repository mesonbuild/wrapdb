vorbis_sources = ['mdct.c', 'smallft.c', 'block.c', 'envelope.c',
  'window.c', 'lsp.c', 'lpc.c', 'analysis.c', 'synthesis.c', 'psy.c',
  'info.c', 'floor1.c', 'floor0.c', 'res0.c', 'mapping0.c', 'registry.c',
  'codebook.c', 'sharedbook.c', 'lookup.c', 'bitrate.c'
]

vorbisfile_sources = ['vorbisfile.c']

vorbisenc_sources = ['vorbisenc.c']

vorbis_lib = build_target('vorbis', vorbis_sources,
  include_directories : [incdir, ogg_inc],
  link_with : ogg_lib,
  dependencies : ogg_dep,
  target_type : libtype,
)

vorbisfile_lib = build_target('vorbisfile', vorbisfile_sources,
  include_directories : [incdir, ogg_inc],
  link_with : vorbis_lib,
  target_type : libtype,
  dependencies : ogg_dep,
)

vorbisenc_lib = build_target('vorbisenc', vorbisenc_sources,
  include_directories : [incdir, ogg_inc],
  link_with : vorbis_lib,
  target_type : libtype,
  dependencies : ogg_dep,
)

test_sharedbook = executable('test_sharedbook', 'sharedbook.c',
  c_args : '-D_V_SELFTEST',
  include_directories : [incdir, ogg_inc],
  link_with : vorbis_lib,
)
test('sharedbook', test_sharedbook)
