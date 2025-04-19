project(
  'win-iconv',
  'c',
  version: '0.0.9',
  meson_version: '>=0.54.0',
)

if host_machine.system() != 'windows'
  error(
    'win-iconv is only supported on windows, and not supported on ' + host_machine.system(),
  )
endif

default_libiconv_dll = get_option('default_libiconv_dll')

c_args = [
  '-D_CRT_SECURE_NO_WARNINGS',
  '-DUSE_LIBICONV_DLL',
  '-DDEFAULT_LIBICONV_DLL="' + default_libiconv_dll + '"',
]

c_lib_args = []

if get_option('default_library') == 'both'
  error('default_library=both is not supported')
elif get_option('default_library') == 'shared'
  c_lib_args += '-DMAKE_DLL'
endif

src_files = files('win_iconv.c')

iconv_lib = library(
  'iconv',
  src_files,
  c_args: c_args + c_lib_args,
  vs_module_defs: 'iconv.def',
  install: true,
)

win_iconv_dep = declare_dependency(
  include_directories: include_directories('.'),
  link_with: iconv_lib,
)

meson.override_dependency('iconv', win_iconv_dep)

win_iconv = executable(
  'win_iconv',
  src_files,
  c_args: c_args + ['-DMAKE_EXE'],
  install: true,
)
meson.override_find_program('win_iconv', win_iconv)

install_headers('iconv.h', 'localcharset.h')

if get_option('tests')
  win_iconv_test_exe = executable('win_iconv_test', files('win_iconv_test.c'))
  test('win_iconv_test', win_iconv_test_exe)
endif
