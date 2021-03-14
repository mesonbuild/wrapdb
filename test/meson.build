fluid_tests = [
  'test_sample_cache',
  'test_sfont_loading',
  'test_sample_rate_change',
  'test_preset_sample_loading',
  'test_bug_635',
  'test_settings_unregister_callback',
  'test_pointer_alignment',
  'test_seqbind_unregister',
  'test_synth_chorus_reverb',
  'test_snprintf',
  'test_synth_process',
  'test_ct2hz',
  'test_sample_validate',
  'test_jack_obtaining_synth',
  'test_sfont_unloading',
  'test_seq_scale',
  'test_seq_event_queue_sort', # this test takes ~70s
]

foreach name : fluid_tests
  exe = executable(name, name + '.c',
                   dependencies : [fluidsynth_dep, glib_dep],
                   include_directories : lib_includes)
  test(name, exe, timeout : 100)
endforeach
