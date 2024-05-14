# Plain tests

benchmark_tests = {
  'benchmark_test': '--benchmark_min_time=0.01s',
  'spec_arg_test': '--benchmark_filter=BM_NotChosen',
  'spec_arg_verbosity_test': '--v=42',
  'benchmark_setup_teardown_test': [],
  'benchmark_min_time_flag_time_test': [],
  'benchmark_min_time_flag_iters_test': [],
  'options_test': '--benchmark_min_time=0.01s',
  'basic_test': '--benchmark_min_time=0.01s',
# 'diagnostics_test': '--benchmark_min_time=0.01s',
  'skip_with_error_test': '--benchmark_min_time=0.01s',
  'donotoptimize_test': '--benchmark_min_time=0.01s',
  'fixture_test': '--benchmark_min_time=0.01s',
  'register_benchmark_test': '--benchmark_min_time=0.01s',
  'map_test': '--benchmark_min_time=0.01s',
  'multiple_ranges_test': '--benchmark_min_time=0.01s',
  'args_product_test': '--benchmark_min_time=0.01s',
}

foreach t, a : benchmark_tests
  test(t,
    executable(t, '@0@.cc'.format(t),
      dependencies: google_benchmark_dep),
    args: a
  )
endforeach

# Filter tests (omitted here)

# Output tests

benchmark_output_tests = {
  'repetitions_test': ['--benchmark_min_time=0.01s', '--benchmark_repetitions=3'],
  'reporter_output_test': '--benchmark_min_time=0.01s',
  'templated_fixture_test': '--benchmark_min_time=0.01s',
  'user_counters_test': '--benchmark_min_time=0.01s',
  'perf_counters_test': ['--benchmark_min_time=0.01s', '--benchmark_perf_counters=CYCLES,BRANCHES'],
  'internal_threading_test': '--benchmark_min_time=0.01s',
  'report_aggregates_only_test': '--benchmark_min_time=0.01s',
  'display_aggregates_only_test': '--benchmark_min_time=0.01s',
  'user_counters_tabular_test': ['--benchmark_counters_tabular=true', '--benchmark_min_time=0.01s'],
  'user_counters_thousands_test': '--benchmark_min_time=0.01s',
  'memory_manager_test': '--benchmark_min_time=0.01s',
}

foreach t, a : benchmark_output_tests
  test(t,
    executable(t, ['@0@.cc'.format(t), 'output_test_helper.cc'],
      dependencies: google_benchmark_dep),
    args: a
  )
endforeach

# Link-main test

test('link_main_test',
  executable('link_main_test', 'link_main_test.cc',
    dependencies: google_benchmark_main_dep),
  args: '--benchmark_min_time=0.01s'
)
