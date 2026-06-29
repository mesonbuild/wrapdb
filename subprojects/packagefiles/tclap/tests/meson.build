# (This file requires ../examples/meson.build to be processed already.)


if not meson.can_run_host_binaries()
  subdir_done()  # We are cross-compiling, but could not execute test binaries.
endif


test_wrapper = executable(
  'test_wrapper',
  'test_wrapper.cpp',
  dependencies: tclap_dep,
)


# Required because test*.sh scripts contain relative paths.
wd = meson.current_build_dir()


tests = [
  # <Name>     <reference>   <executable> <parametres>
  ['test 1', 'test1.out', test1, '-r -n mike'],
  ['test 2', 'test2.out', test1, '-n mike'],
  ['test 3', 'test3.out', test1, '-n mike -r'],
  ['test 4', 'test4.out', test1, ''],
  ['test 5', 'test5.out', test2, '-i 10 -s homer marge bart lisa'],
  ['test 6', 'test6.out', test2, '-i 10 -s hello goodbye -ABC'],
  ['test 7', 'test7.out', test2, '-i 10 -s hello goodbye -hABC'],
  ['test 8', 'test8.out', test2, '--version'],
  ['test 9', 'test9.out', test2, '-i 10 -s hello goodbye -- -hv one two'],
  ['test 10', 'test10.out', test2, '-i 10 -s hello'],
  ['test 11', 'test11.out', test2, '-i 10 -s hello -i 9'],
  ['test 12', 'test12.out', test2, '-i 10 -s hello -f nine'],
  [
    'test 13',
    'test13.out',
    test3,
    '--stringTest=bill -i=9 -i=8 -B homer marge bart',
  ],
  [
    'test 14',
    'test14.out',
    test3,
    '--stringTest=aaa homer marge bart -- one two',
  ],
  [
    'test 15',
    'test15.out',
    test3,
    '--stringTest bbb homer marge bart -- -hv two',
  ],
  ['test 16', 'test16.out', test3, '--stringTest one homer -B -Bh'],
  ['test 17', 'test17.out', test3, '--stringTest=one homer -B'],
  ['test 18', 'test18.out', test4, '-Bs --Bs asdf'],
  ['test 19', 'test19.out', test4, '-BA --Bs asdf'],
  [
    'test 20',
    'test20.out',
    test5,
    '-a asdf -c fdas --eee blah -i sss -i fdsf',
  ],
  ['test 21', 'test21.out', test5, '-b asdf -c fdas -g asdf -j homer'],
  ['test 22', 'test22.out', test5, '-a fdsa -b asdf -c fdas'],
  ['test 23', 'test23.out', test5, '-d junk -c fdas'],
  ['test 24', 'test24.out', test5, '--aaa dilbert -b asdf -c fdas'],
  [
    'test 25',
    'test25.out',
    test5,
    '--aaa asdf -c fdas --fff blah -i one -i two',
  ],
  ['test 26', 'test26.out', test2, '-i 2 -f 4..2 -s asdf asdf'],
  ['test 27', 'test27.out', test2, '-i 2 -f 4.0.2 -s asdf asdf'],
  ['test 28', 'test28.out', test2, '-i 2a -f 4.2 -s asdf asdf'],
  ['test 29', 'test29.out', test2, '-i 0xA -f 4.2 -s asdf asdf'],
  ['test 30', 'test30.out', test2, '-i 2.1 -f 4.2 -s asdf asdf'],
  ['test 31', 'test31.out', test3, '-i=9a -i=1 -s=asdf asdf asdf'],
  ['test 32', 'test32.out', test3, '-f=9 -f=1.0.0 -s=asdf asdf asdf'],
  [
    'test 33',
    'test33.out',
    test5,
    '-a asdf -c fdas --eee blah --ddd -j o --jjj t',
  ],
  ['test 34', 'test34.out', test6, '-n homer 2'],
  ['test 35', 'test35.out', test6, '-n mike 2'],
  ['test 36', 'test36.out', test6, '-n homer 6'],
  ['test 37', 'test37.out', test7, '-n homer 2 -n marge 1 3'],
  ['test 38', 'test38.out', test7, '-n mike 2 1'],
  ['test 39', 'test39.out', test7, '2 -n homer -n bart 6'],
  ['test 40', 'test40.out', test1, '--help'],
  ['test 41', 'test41.out', test2, '--help'],
  ['test 42', 'test42.out', test3, '--help'],
  ['test 43', 'test43.out', test4, '--help'],
  ['test 44', 'test44.out', test5, '--help'],
  ['test 45', 'test45.out', test6, '--help'],
  ['test 46', 'test46.out', test7, '--help'],
  ['test 47', 'test47.out', test8, '-s=bill -i=9 -i=8 -B homer marge bart'],
  ['test 48', 'test48.out', test8, '-s=aaa homer marge bart -- one two'],
  ['test 49', 'test49.out', test8, '-s bbb homer marge bart -- -hv two'],
  ['test 50', 'test50.out', test8, '-s one homer -B -Bh'],
  ['test 51', 'test51.out', test8, '-s=one homer -B'],
  ['test 52', 'test52.out', test8, '-i=9a -i=1 -s=asdf asdf asdf'],
  ['test 53', 'test53.out', test8, '-f=9 -f=1.0.0 -s=asdf asdf asdf'],
  ['test 54', 'test54.out', test8, '--help'],
  ['test 55', 'test55.out', test3, '--stringTest=asdf - asdf zero one'],
  ['test 56', 'test56.out', test2, '-i 1 - -s fdsa one two'],
  [
    'test 57',
    'test57.out',
    test5,
    '--aaa asdf -c fdas --fff blah -i one -i two -j huh',
  ],
  ['test 58', 'test58.out', test9, ''],
  ['test 59', 'test59.out', test9, '-VVV -N --noise -r blah'],
  ['test 60', 'test60.out', test9, '-VVV -N --noise -rr'],
  ['test 61', 'test61.out', test2, '-i 10 -s hello "-1 -1"'],
  ['test 62', 'test62.out', test2, ''],
  ['test 63', 'test63.out', test11, ''],
  ['test 64', 'test64.out', test11, '-v "1 2 3"'],
  [
    'test 65',
    'test65.out',
    test12,
    '-v "1 2 3" -v "4 5 6" -v "7 8 9" -v "-1 0.2 0.4"',
  ],
  ['test 66', 'test66.out', test12, ''],
  ['test 67', 'test67.out', test12, '-v "a 1 0.3"'],
  ['test 68', 'test68.out', test13, ''],
  ['test 69', 'test69.out', test18, '--bob'],
  ['test 70', 'test70.out', test18, '--help'],
  ['test 71', 'test71.out', test19, '-i 0xA'],
  ['test 72', 'test72.out', test19, '-i 012'],
  ['test 73', 'test73.out', test2, '-i 1 -s asdf fff*fff'],
  ['test 74', 'test74.out', test20, '-a -b'],
  ['test 75', 'test75.out', test20, '-b -a'],
  ['test 76', 'test76.out', test20, '-ba'],
  ['test 77', 'test77.out', test20, '-ab'],
  ['test 78', 'test78.out', test21, '~~reverse /n mike'],
  ['test 79', 'test79.out', test21, ''],
  ['test 80', 'test80.out', test22, 'asdf -n mike asdf fds xxx'],
  ['test 81', 'test81.out', test22, 'asdf  asdf -r fds xxx'],
  [
    'test 82',
    'test82.out',
    test23,
    'blah --blah -s=bill -i=9 -i=8 -B homer marge bart',
  ],
  ['test 83', 'test83.out', test24, ''],
  ['test 84', 'test84.out', test25, '-h x'],
  ['test 85', 'test85.out', test25, '-h'],
  ['test 86', 'test86.out', test14, '-v "3.2 -47.11 0"'],
  ['test 87', 'test87.out', test26, '-v "1 2 3"'],
  ['test 88', 'test88.out', test27, ''],
  ['test 89', 'test89.out', test28, ''],
  ['test 90', 'test90.out', test29, ''],
  ['test 91', 'test91.out', test30, '-p "1 2.3"'],
]


foreach t : tests
  test(
    t[0],
    test_wrapper,
    args: [meson.current_source_dir() / t[1], t[2], t[3]],
    depends: t[2],
    workdir: wd,
  )
endforeach


