if not get_option('tests')
  subdir_done()
endif

testlib = static_library(
  'testlib',
  objects: argtable3_lib.extract_all_objects(
    recursive: false,
  ),
  dependencies: libm,
)

testlib_dep = declare_dependency(
  include_directories: argtable3_inc,
  link_with: testlib,
)

test_files = files(
  'CuTest.c',
  'testall.c',
  'testargcmd.c',
  'testargdate.c',
  'testargdbl.c',
  'testargdstr.c',
  'testargfile.c',
  'testarghashtable.c',
  'testargint.c',
  'testarglit.c',
  'testargrex.c',
  'testargstr.c',
)

test(
  'tests',
  executable(
    'tests',
    test_files,
    dependencies: testlib_dep,
  ),
)
