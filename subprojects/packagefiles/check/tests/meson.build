tests = {
  'check_check' : files([
    'check_check_exit.c',
    'check_check_fixture.c',
    'check_check_fork.c',
    'check_check_limit.c',
    'check_check_log.c',
    'check_check_log_internal.c',
    'check_check_main.c',
    'check_check_master.c',
    'check_check_msg.c',
    'check_check_pack.c',
    'check_check_selective.c',
    'check_check_sub.c',
    'check_check_tags.c',
    'check_list.c',
  ]),
  'check_check_export' : files([
    'check_check_export_main.c',  
    'check_check_fork.c',
    'check_check_log.c',
    'check_check_master.c',
    'check_check_sub.c',
  ]),
  'check_mem_leaks' : files([
    'check_check_exit.c',
    'check_check_fork.c',
    'check_check_log.c',
    'check_check_master.c',
    'check_check_selective.c',
    'check_check_sub.c',
    'check_check_tags.c',
    'check_mem_leaks.c',
  ]),
  'nofork' : files(['check_nofork.c']),
}

if get_option('unused_tests')
  tests += {
    'stress' : files('check_stress.c'),
    'nofork_teardown' : files('check_nofork_teardown.c'),
    'ex_output' : files('ex_output.c'),
  }
endif


if get_option('timeout_tests')
  tests_c_args = ['-DTIMEOUT_TESTS_ENABLED=1']
else
  tests_c_args = ['-DTIMEOUT_TESTS_ENABLED=0']
endif

foreach test_name, file_list : tests
  exe = executable(test_name, file_list,
    c_args: ['-DHAVE_CONFIG_H=1', tests_c_args],
    include_directories: confinc,
    dependencies : check_dep,
    )
  test(test_name, exe)
endforeach
