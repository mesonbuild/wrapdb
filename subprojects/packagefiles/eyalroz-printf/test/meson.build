common_compiler_args = [
  '-gdwarf-2',
  '-ffunction-sections',
  '-fdata-sections',
  '-fverbose-asm',
  '-Wundef',
  '-Wshadow',
  '-Wunreachable-code',
  '-Wswitch-default',
  '-Wcast-align',
  '-Wmissing-include-dirs',
  '-Winit-self',
  '-Wdouble-promotion',
  '-Wunused-parameter',
  '-Wstrict-prototypes',
  '-Wsign-conversion',
]

c_common_args = cc.get_supported_arguments(common_compiler_args)
c_common_args += cc.get_supported_arguments('-fno-builtin-printf')
aliasing_exe = executable(
  'aliasing',
  'aliasing.c',
  cfg_header_file,
  build_by_default: false,
  c_args: c_common_args,
  dependencies: [eyalroz_printf_dep],
  include_directories: '..',
  override_options: ['c_std=c11'],
)
test('printf.aliasing', aliasing_exe)

cxx = meson.get_compiler('cpp')
cxx_common_args = cxx.get_supported_arguments(common_compiler_args)
if get_option('test_with_non_standard_format_strings')
  cxx_common_args += '-DTEST_WITH_NON_STANDARD_FORMAT_STRINGS'
endif
autotest_exe = executable(
  'autotest',
  'autotest.cpp',
  cfg_header_file,
  build_by_default: false,
  cpp_args: cxx_common_args,
  implicit_include_directories: false,
  include_directories: '..',
  dependencies: eyalroz_printf_dep,
  override_options: ['cpp_std=c++11', 'cpp_eh=none'],
)
# Not running autotest by default - it's randomized after all.

# Ignore next test while 'test/test_suite_main_testcases.hpp:829' is not fixed in new version
#
# if get_option('alias_standard_function_names') != 'soft'
#   test_suite_exe = executable(
#     'test_suite',
#     'test_suite.cpp',
#     cfg_header_file,
#     build_by_default: false,
#     cpp_args: ['-DPRINTF_INCLUDE_CONFIG_H', cxx_common_args],
#     include_directories: ['..', '../src'],
#     override_options: ['cpp_std=c++11', 'cpp_eh=none'],
#   )
#   test('printf.test_suite', test_suite_exe)
# endif
