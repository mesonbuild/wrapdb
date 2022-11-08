if host_machine.system() == 'windows'
  ck_dll_exp_interface = get_option('default_library') != 'static' ? '-DCK_DLL_EXP=__declspec(dllimport)' : []
  ck_dll_exp_private = get_option('default_library') != 'static' ? '-DCK_DLL_EXP=__declspec(dllexport)' : []
else
  ck_dll_exp_interface = []
  ck_dll_exp_private = '-DCK_DLL_EXP=__attribute__((visibility("default")))'
endif

configure_file(
  input: 'check.h.in',
  output: 'check.h',
  configuration: cdata,
)

configure_file(
  input: '../cmake/check_stdint.h.in',
  output: 'check_stdint.h',
  configuration: cdata,
  format: 'cmake@',
)

sources = files(
  'check.c',
  'check_error.c',
  'check_list.c',
  'check_log.c',
  'check_msg.c',
  'check_pack.c',
  'check_print.c',
  'check_run.c',
  'check_str.c',
)

checklib = library(
  'check',
  sources,
  c_args: ['-DHAVE_CONFIG_H=1', ck_dll_exp_private],
  include_directories: [confinc],
  dependencies: [libm, compatlib_dep],
)

check_dep = declare_dependency(
  include_directories: '.',
  link_with: checklib,
  compile_args: ck_dll_exp_interface,
)
