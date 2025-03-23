#Windows does not have random
if not cc.has_function('random')
  subdir_done()
endif

conf = configuration_data()

if cc.has_header('pthread.h')
  conf.set('HAVE_PTHREAD_H', 1)
endif

configure_file(
  output: 'config.h',
  configuration: conf,
)

threads_dep = dependency('threads')

runtest = executable(
  'runtest',
  ['runtest.cc', 'test.cc'],
  dependencies: [mpdecpp_dep, threads_dep],
)

# These tests require to download test data.
# test(
#   'libmpdec++/official', runtest,
#   args: files('official.topTest'),
#   depends: testdata,
#   workdir: join_paths(meson.current_build_dir(), '..', 'tests'))

test(
  'libmpdec++/additional',
  runtest,
  args: files('additional.topTest'),
  depends: testdata,
  workdir: join_paths(meson.current_build_dir(), '..', 'tests'),
  timeout: 660,
)
