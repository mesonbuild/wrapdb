mklist = find_program(
  'mklist.py',
  required: get_option('tests'),
  disabler: true,
)

if get_option('tests').disabled()
  test_utils_sources = disabler()
  test_utils_include = disabler()
else
  test_utils_sources = files('test_main.c', 'test_utils.c')
  test_utils_include = include_directories('.')
endif
