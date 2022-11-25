benchmark_tests = {
  'benchmark_test': '--benchmark_min_time=0.01',
  'spec_arg_test': '--benchmark_filter=BM_NotChosen',
  'spec_arg_verbosity_test': '--v=42',
  'benchmark_setup_teardown_test': [],
  'options_test': '--benchmark_min_time=0.01',
  'basic_test': '--benchmark_min_time=0.01',
# 'diagnostics_test': '--benchmark_min_time=0.01',
# 'skip_with_error_test': '--benchmark_min_time=0.01',
  'donotoptimize_test': '--benchmark_min_time=0.01',
  'fixture_test': '--benchmark_min_time=0.01',
# 'register_benchmark_test': '--benchmark_min_time=0.01',
  'map_test': '--benchmark_min_time=0.01',
  'multiple_ranges_test': '--benchmark_min_time=0.01',
  'args_product_test': '--benchmark_min_time=0.01',
}

foreach t, a : benchmark_tests
  test(t, executable(t, '@0@.cc'.format(t), dependencies: google_benchmark_dep), args: a)
endforeach
