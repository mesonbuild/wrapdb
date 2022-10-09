src_includes = include_directories(
  '.',
  'bindings',
  'drivers',
  'midi',
  'rvoice',
  'sfloader',
  'synth',
  'utils',
)

fluidsynth_sources = files(
  'bindings/fluid_cmd.c',
  'bindings/fluid_filerenderer.c',
  'bindings/fluid_ladspa.c',
  'drivers/fluid_adriver.c',
  'drivers/fluid_mdriver.c',
  'midi/fluid_midi.c',
  'midi/fluid_midi_router.c',
  'midi/fluid_seq.c',
  'midi/fluid_seq_queue.cpp',
  'midi/fluid_seqbind.c',
  'midi/fluid_seqbind_notes.cpp',
  'rvoice/fluid_adsr_env.c',
  'rvoice/fluid_chorus.c',
  'rvoice/fluid_iir_filter.c',
  'rvoice/fluid_lfo.c',
  'rvoice/fluid_rev.c',
  'rvoice/fluid_rvoice.c',
  'rvoice/fluid_rvoice_dsp.c',
  'rvoice/fluid_rvoice_event.c',
  'rvoice/fluid_rvoice_mixer.c',
  'sfloader/fluid_defsfont.c',
  'sfloader/fluid_samplecache.c',
  'sfloader/fluid_sffile.c',
  'sfloader/fluid_sfont.c',
  'synth/fluid_chan.c',
  'synth/fluid_event.c',
  'synth/fluid_gen.c',
  'synth/fluid_mod.c',
  'synth/fluid_synth.c',
  'synth/fluid_synth_monopoly.c',
  'synth/fluid_tuning.c',
  'synth/fluid_voice.c',
  'utils/fluid_conv.c',
  'utils/fluid_hash.c',
  'utils/fluid_list.c',
  'utils/fluid_ringbuffer.c',
  'utils/fluid_settings.c',
  'utils/fluid_sys.c',
)

make_tables_sources = files(
  'gentables/gen_conv.c',
  'gentables/gen_rvoice_dsp.c',
  'gentables/make_tables.c',
)

make_tables_exe = executable(
  'make_tables',
  make_tables_sources,
  native: true,
  dependencies: m_dep,
  include_directories: '.',
  c_args: cc.get_argument_syntax() == 'msvc' ? ['-D_USE_MATH_DEFINES'] : [],
)

gen_tables = custom_target(
  'gen_tables',
  command: [make_tables_exe, meson.current_build_dir() + '/'],
  output: ['fluid_conv_tables.inc.h', 'fluid_rvoice_dsp_tables.inc.h']
)
