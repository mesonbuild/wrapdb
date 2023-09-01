if not get_option('tests')
  subdir_done()
endif

stress = executable('stress',
  'stress.c',
  'testlib.c',
  include_directories: incdirs,
  link_with: libusb,
)

test('libusb_test', stress, timeout: 90)

umockdev_dep = dependency('umockdev', required: false)
if umockdev_dep.found()
  utest = executable('umockdev',
    'umockdev.c',
    include_directories: incdirs,
    link_with: libusb,
  )

  test('umockdev_test', utest, timeout: 60)
endif
