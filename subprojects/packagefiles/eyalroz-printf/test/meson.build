tests_c_args = cc.get_supported_arguments(
  '-g',  # gcc args
  '-Wall',
  '-Wextra',
  '-pedantic',
  '-Wundef',
  '-Wsign-conversion',
  '-Wuninitialized',
  '-Wshadow',
  '-Wunreachable-code',
  '-Wswitch-default',
  '-Wswitch',
  '-Wcast-align',
  '-Wmissing-include-dirs',
  '-Winit-self',
  '-Wdouble-promotion',
  '-gdwarf-2',
  '-fno-exceptions',
  '-ffunction-sections',
  '-fdata-sections',
  '-fverbose-asm',
  '-Wunused-parameter',
  '-ffat-lto-objects',
  '-Wstrict-prototypes',
  '-std=c11',
  '/W4',  # msvc args
  '/std:c11',
)

cxx = meson.get_compiler('cpp')
tests_cpp_args = cxx.get_supported_arguments(
  '-g',  # gcc args
  '-Wall',
  '-Wextra',
  '-pedantic',
  '-Wundef',
  '-Wsign-conversion',
  '-Wuninitialized',
  '-Wshadow',
  '-Wunreachable-code',
  '-Wswitch-default',
  '-Wswitch',
  '-Wcast-align',
  '-Wmissing-include-dirs',
  '-Winit-self',
  '-Wdouble-promotion',
  '-gdwarf-2',
  '-fno-exceptions',
  '-ffunction-sections',
  '-fdata-sections',
  '-fverbose-asm',
  '-Wunused-parameter',
  '-ffat-lto-objects',
  '-std=c++11',
  '/W4',  # msvc args
  '/std:c++11',
)

aliasing_exe = executable(
  'aliasing',
  'aliasing.c',
  cfg_header_file,
  c_args: [cc.get_supported_arguments('-fno-builtin-printf'), tests_c_args],
  dependencies: [eyalroz_printf_dep],
  include_directories: '..',
)
test('printf.aliasing', aliasing_exe)


non_std_fmt_define = []
if get_option('test_with_non_standard_format_strings')
  non_std_fmt_define += '-DTEST_WITH_NON_STANDARD_FORMAT_STRINGS'
endif

autotest_exe = executable(
  'autotest',
  'autotest.cpp',
  cfg_header_file,
  cpp_args: [non_std_fmt_define, tests_cpp_args],
  implicit_include_directories: false,
  include_directories: '..',
  dependencies: eyalroz_printf_dep,
)
# Not running autotest by default - it's randomized after all.

if get_option('alias_standard_function_names') != 'soft'
  test_suite_exe = executable(
    'test_suite',
    'test_suite.cpp',
    cfg_header_file,
    cpp_args: ['-DPRINTF_INCLUDE_CONFIG_H', non_std_fmt_define, tests_cpp_args],
    include_directories: ['..', '../src'],
  )
  test('printf.test_suite', test_suite_exe)
endif
