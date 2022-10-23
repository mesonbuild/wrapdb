sources = files(
  'ctest.c',
  'datamap.cpp',
  'testdata.cpp',
  'tstdtmod.cpp',
  'ucln_ct.c',
  'uperf.cpp',
)

ctestfw = library(
  'ctestfw',
  sources,
  c_args: '-DT_CTEST_IMPLEMENTATION',
  cpp_args: '-DT_CTEST_IMPLEMENTATION',
  include_directories: [incdir, toolinc],
  link_with: [toolutil_lib, common_lib],
)
