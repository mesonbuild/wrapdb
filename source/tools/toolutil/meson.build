sources = files(
  'filestrm.cpp',
  'package.cpp',
  'pkgitems.cpp',
  'swapimpl.cpp',
  'toolutil.cpp',
  'unewdata.cpp',
  'collationinfo.cpp',
  'denseranges.cpp',
  'ucm.cpp',
  'ucmstate.cpp',
  'uoptions.cpp',
  'uparse.cpp',
  'ucbuf.cpp',
  'xmlparser.cpp',
  'writesrc.cpp',
  'pkg_icu.cpp',
  'pkg_genc.cpp',
  'pkg_gencmn.cpp',
  'ppucd.cpp',
  'flagparser.cpp',
  'filetools.cpp',
  'udbgutil.cpp',
  'dbgutil.cpp',
  'ucln_tu.cpp',
)

toolutil_c_args = ['-DU_TOOLUTIL_IMPLEMENTATION']
toolutil_cpp_args = ['-DU_TOOLUTIL_IMPLEMENTATION']

if host_machine.system() != 'windows' and host_machine.system() != 'darwin'
  toolutil_c_args += ['-DU_ELF']
  toolutil_cpp_args += ['-DU_ELF']
endif


toolutil_lib = static_library('toolutil',
  sources,
  include_directories : incdir,
  c_args : toolutil_c_args,
  cpp_args : toolutil_cpp_args,
  link_with: [i18n_lib, common_lib],
)
