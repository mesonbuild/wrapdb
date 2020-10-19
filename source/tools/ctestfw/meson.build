sources = files(
  'ctest.c',
  'tstdtmod.cpp',
  'testdata.cpp',
  'datamap.cpp',
  'uperf.cpp',
  'ucln_ct.c',
)

ctestfw = library('ctestfw',
  sources,
  c_args : '-DT_CTEST_IMPLEMENTATION',
  cpp_args : '-DT_CTEST_IMPLEMENTATION',
  include_directories : [incdir, toolinc],
  link_with: [toolutil_lib, common_lib],
)
