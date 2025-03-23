#Windows does not have random
if not cc.has_function('random')
  subdir_done()
endif

runtest = executable(
  'runtest',
  ['runtest.c', 'test.c'],
  dependencies: mpdec_dep,
)

testdata = custom_target(
  'testdata',
  command: [
    find_program('gettests.py'),
    join_paths(meson.current_source_dir(), 'testdata_dist'),
    join_paths(meson.current_build_dir(), 'testdata'),
  ],
  output: 'testdata.stamp',
)

# These tests require to download test data.
# test(
#   'libmpdec/official', runtest,
#   args: files('official.decTest'),
#   depends: testdata,
#   workdir: meson.current_build_dir())

test(
  'libmpdec/additional',
  runtest,
  args: files('additional.decTest'),
  depends: testdata,
  workdir: meson.current_build_dir(),
  timeout: 660,
)
