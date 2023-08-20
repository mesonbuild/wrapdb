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
  # FIXME: broken in 1.12.0 (see https://github.com/gabime/spdlog/pull/2827).
  # 'test_misc.cpp',
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
    'catch2',
    version: '>=3.0.0',
    allow_fallback: false,
    required: false,
)
if catch2_dep.found()
    spdlog_test_dep += catch2_dep
else
    spdlog_test_dep += dependency('catch2-with-main', version: '>=3.0.0')
endif

test('tests', executable('tests_exe', test_src, dependencies: spdlog_test_dep))
