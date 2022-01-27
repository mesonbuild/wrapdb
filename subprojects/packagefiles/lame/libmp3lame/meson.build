lame_sources = [
  'bitstream.c',
  'encoder.c',
  'fft.c',
  'gain_analysis.c',
  'id3tag.c',
  'lame.c',
  'mpglib_interface.c',
  'newmdct.c',
  'presets.c',
  'psymodel.c',
  'quantize.c',
  'quantize_pvt.c',
  'reservoir.c',
  'set_get.c',
  'tables.c',
  'takehiro.c',
  'util.c',
  'vbrquantize.c',
  'VbrTag.c',
  'version.c',
]

vector_sources = []
if cdata.has('HAVE_XMMINTRIN_H')
  vector_sources += ['vector/xmm_quantize_sub.c']
endif

lame_deps = [m_dep]
if build_decoder
  lame_deps += [mpglib_dep]
endif

lamelib = library('mp3lame',
  lame_sources, vector_sources,
  version : '0.0.0',
  include_directories : [lameinc, confinc],
  c_args : common_args,
  dependencies : lame_deps,
  install : true)

lame_dep = declare_dependency(
  include_directories : [lameinc, confinc],
  link_with : lamelib,
  )
