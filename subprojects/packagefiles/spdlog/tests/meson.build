test_src = files(
  'main.cpp',
  'test_async.cpp',
  'test_backtrace.cpp',
  'test_cfg.cpp',
  'test_create_dir.cpp',
  'test_daily_logger.cpp',
  'test_dup_filter.cpp',
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

test('tests', executable('tests_exe', test_src, dependencies: spdlog_dep))
