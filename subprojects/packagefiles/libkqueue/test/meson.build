# tests on Windows are completely broken
if host_machine.system() == 'windows'
  subdir_done()
endif

test_sources = files(
  'common.c',
  'kqueue.c',
  'libkqueue.c',
  'main.c',
  'read.c',
  'test.c',
  'timer.c',
  'user.c',
  'vnode.c',
  'write.c',
)

if host_machine.system() != 'windows'
  test_sources += files('proc.c', 'signal.c')
endif

test(
  'libkqueue-test',
  executable(
    'libkqueue-test',
    test_sources,
    include_directories: '..',
    dependencies: libkqueue_dep,
  ),
)
