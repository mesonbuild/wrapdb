# skip tests if disabled
if get_option('tests').disabled()
  subdir_done()
endif

test_src = files(
  'main.cpp',
  'test_async.cpp',
  'test_backtrace.cpp',
  'test_bin_to_hex.cpp',
  'test_cfg.cpp',
  'test_circular_q.cpp',
  'test_create_dir.cpp',
  'test_custom_callbacks.cpp',
  'test_daily_logger.cpp',
  'test_dup_filter.cpp',
  'test_errors.cpp',
  'test_eventlog.cpp',
  'test_file_helper.cpp',
  'test_file_logging.cpp',
  'test_fmt_helper.cpp',
  'test_macros.cpp',
  'test_misc.cpp',
  'test_mpmc_q.cpp',
  'test_pattern_formatter.cpp',
  'test_registry.cpp',
  'test_stdout_api.cpp',
  'test_stopwatch.cpp',
  'test_time_point.cpp',
  'utils.cpp',
)

spdlog_test_dep = [spdlog_dep]

catch2_dep = dependency(
  'catch2-with-main',
  version: '>=3.0.0',
  allow_fallback: false,
  required: false,
)

if not catch2_dep.found()
  if get_option('tests').enabled()
    error('Catch2 is required for tests')
  else
    message('Skipping tests since Catch2 was not found')
  endif
  subdir_done()
endif

test(
  'tests',
  executable(
    'tests_exe',
    test_src,
    override_options: override_cpp,
    dependencies: [catch2_dep, spdlog_dep],
  ),
)
