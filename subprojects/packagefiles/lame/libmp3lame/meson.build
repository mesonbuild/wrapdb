lame_sources = files(
  'VbrTag.c',
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
  'version.c',
  cdata.has('HAVE_XMMINTRIN_H') ? 'vector/xmm_quantize_sub.c' : [],
)

if host_machine.system() == 'windows'
  lame_sources += windows.compile_resources('lame.rc', include_directories: [lameinc, confinc])
endif

lame_deps = [m_dep]
if build_decoder
  lame_deps += [mpglib_dep]
endif

lamelib = library(
  'mp3lame',
  lame_sources,
  version : '0.0.0',
  include_directories : [lameinc, confinc],
  c_args : common_args,
  gnu_symbol_visibility: 'hidden',
  vs_module_defs: '../include/lame.def',
  dependencies: lame_deps,
  install: true,
)

lame_dep = declare_dependency(
  include_directories: [lameinc, confinc],
  link_with: lamelib,
)
