# (This file requires ../examples/meson.build to be processed already.)


if not meson.can_run_host_binaries()
  subdir_done()  # We are cross-compiling, but could not execute test binaries.
endif


if not find_program(
  '/bin/bash',
  required: false,
).found()
  subdir_done()  # Required command interpreter missing.
endif


if not find_program(
  'cmp',
  required: false,
).found()
  subdir_done()  # Required shell command not found.
endif


# The test scripts need $srcdir pointing to the directory of the 'test*.out' files.
srcdir_param = 'srcdir=' + meson.current_source_dir()


# Required because test*.sh scripts contain relative paths.
wd = meson.current_build_dir()


if find_program(
  'tee',
  required: false,
).found() and find_program(
  'diff',
  required: false,
).found()

  tests = [
    # <Name>     <test script>  <executable>
    ['test 1', 'test1.sh', test1],
    ['test 2', 'test2.sh', test1],
    ['test 3', 'test3.sh', test1],
    ['test 4', 'test4.sh', test1],
    ['test 5', 'test5.sh', test2],
    ['test 6', 'test6.sh', test2],
    ['test 7', 'test7.sh', test2],
    ['test 8', 'test8.sh', test2],
    ['test 9', 'test9.sh', test2],
    ['test 10', 'test10.sh', test2],
    ['test 11', 'test11.sh', test2],
    ['test 12', 'test12.sh', test2],
    ['test 13', 'test13.sh', test3],
    ['test 14', 'test14.sh', test3],
    ['test 15', 'test15.sh', test3],
    ['test 16', 'test16.sh', test3],
    ['test 17', 'test17.sh', test3],
    ['test 18', 'test18.sh', test4],
    ['test 19', 'test19.sh', test4],
    ['test 20', 'test20.sh', test5],
    ['test 21', 'test21.sh', test5],
    ['test 22', 'test22.sh', test5],
    ['test 23', 'test23.sh', test5],
    ['test 24', 'test24.sh', test5],
    ['test 25', 'test25.sh', test5],
    ['test 26', 'test26.sh', test2],
    ['test 27', 'test27.sh', test2],
    ['test 28', 'test28.sh', test2],
    ['test 29', 'test29.sh', test2],
    ['test 30', 'test30.sh', test2],
    ['test 31', 'test31.sh', test3],
    ['test 32', 'test32.sh', test3],
    ['test 33', 'test33.sh', test5],
    ['test 34', 'test34.sh', test6],
    ['test 35', 'test35.sh', test6],
    ['test 36', 'test36.sh', test6],
    ['test 37', 'test37.sh', test7],
    ['test 38', 'test38.sh', test7],
    ['test 39', 'test39.sh', test7],
    ['test 40', 'test40.sh', test1],
    ['test 41', 'test41.sh', test2],
    ['test 42', 'test42.sh', test3],
    ['test 43', 'test43.sh', test4],
    ['test 44', 'test44.sh', test5],
    ['test 45', 'test45.sh', test6],
    ['test 46', 'test46.sh', test7],
    ['test 47', 'test47.sh', test8],
    ['test 48', 'test48.sh', test8],
    ['test 49', 'test49.sh', test8],
    ['test 50', 'test50.sh', test8],
    ['test 51', 'test51.sh', test8],
    ['test 52', 'test52.sh', test8],
    ['test 53', 'test53.sh', test8],
    ['test 54', 'test54.sh', test8],
    ['test 55', 'test55.sh', test3],
    ['test 56', 'test56.sh', test2],
    ['test 57', 'test57.sh', test5],
    ['test 58', 'test58.sh', test9],
    ['test 59', 'test59.sh', test9],
    ['test 60', 'test60.sh', test9],
    ['test 61', 'test61.sh', test2],
    ['test 62', 'test62.sh', test2],
    ['test 63', 'test63.sh', test11],
    ['test 64', 'test64.sh', test11],
    ['test 65', 'test65.sh', test12],
    ['test 66', 'test66.sh', test12],
    ['test 67', 'test67.sh', test12],
    ['test 68', 'test68.sh', test13],
    ['test 69', 'test69.sh', test18],
    ['test 70', 'test70.sh', test18],
    ['test 71', 'test71.sh', test19],
    ['test 72', 'test72.sh', test19],
    ['test 73', 'test73.sh', test2],
    ['test 74', 'test74.sh', test20],
    ['test 75', 'test75.sh', test20],
    ['test 76', 'test76.sh', test20],
    ['test 77', 'test77.sh', test20],
    ['test 78', 'test78.sh', test21],
    ['test 79', 'test79.sh', test21],
  ]

  foreach t : tests
    test(
      t[0],
      find_program(t[1]),
      env: srcdir_param,
      depends: t[2],
      workdir: wd,
      is_parallel: false,  # All test scripts use local filename tmp.out.
    )
  endforeach

endif


tests = [
  # <Name>     <test script>  <executable>
  ['test 80', 'test80.sh', test22],
  ['test 81', 'test81.sh', test22],
  ['test 82', 'test82.sh', test23],
  ['test 83', 'test83.sh', test24],
  ['test 84', 'test84.sh', test25],
  ['test 85', 'test85.sh', test25],
  ['test 86', 'test86.sh', test14],
  ['test 87', 'test87.sh', test26],
  ['test 88', 'test88.sh', test27],
  ['test 89', 'test89.sh', test28],
  ['test 90', 'test90.sh', test29],
  ['test 91', 'test91.sh', test30],
]

foreach t : tests
  test(
    t[0],
    find_program(t[1]),
    env: srcdir_param,
    depends: t[2],
    workdir: wd,
    is_parallel: false,  # All test scripts use local filename tmp.out.
  )
endforeach


