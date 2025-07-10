common_msvc_args = ['/W4']
common_gcc_args = [
  '-g',
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
]
tests_c_args = []
if cc.get_argument_syntax() == 'msvc'
  tests_c_args += [common_msvc_args, '/std:c11']
elif cc.get_argument_syntax() == 'gcc'
  tests_c_args += [common_gcc_args, '-std=c11']
  tests_c_args += '-Wstrict-prototypes'
  if cc.get_id() == 'gcc'
    tests_c_args += '-ffat-lto-objects'
  endif
endif
tests_cpp_args = []
cxx = meson.get_compiler('cpp')
if cxx.get_argument_syntax() == 'msvc'
  tests_cpp_args += [common_msvc_args, '/std:c++11']
elif cxx.get_argument_syntax() == 'gcc'
  tests_cpp_args += [common_gcc_args, '-std=c++11']
  if cxx.get_id() == 'gcc'
    tests_cpp_args += '-ffat-lto-objects'
  endif
endif

aliasing_opt = []
if cc.get_argument_syntax() == 'gcc'
  aliasing_opt += '-fno-builtin-printf'
endif
aliasing_exe = executable(
  'aliasing',
  'aliasing.c',
  cfg_header_file,
  c_args: [aliasing_opt, tests_c_args],
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
