executable('dpfp',
  'dpfp.c',
  include_directories: incdirs,
  link_with: libusb,
)

executable('dpfp_threaded',
  'dpfp.c',
  include_directories: incdirs,
  link_with: libusb,
  c_args: '-DDPFP_THREADED',
  dependencies: thread_dep,
)

fxload_sources = files('fxload.c', 'ezusb.c',)
if cc.get_argument_syntax() == 'msvc'
  fxload_sources += files('../msvc/getopt/getopt.c', '../msvc/getopt/getopt1.c')
endif

executable('fxload',
  fxload_sources,
  include_directories: [ incdirs, include_directories('../msvc/getopt') ],
  link_with: libusb,
  c_args: cc.get_argument_syntax() == 'msvc' ? '-DHAVE_STRING_H' : '',
)

executable('hotplugtest',
  'hotplugtest.c',
  include_directories: incdirs,
  link_with: libusb,
)

executable('listdevs',
  'listdevs.c',
  include_directories: incdirs,
  link_with: libusb,
)

executable('sam3u_benchmark',
  'sam3u_benchmark.c',
  include_directories: incdirs,
  link_with: libusb,
)

executable('testlibusb',
  'testlibusb.c',
  include_directories: incdirs,
  link_with: libusb,
)

executable('xusb',
  'xusb.c',
  include_directories: incdirs,
  link_with: libusb,
)
