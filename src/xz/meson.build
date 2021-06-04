sources = [
  'args.c',
  'args.h',
  'coder.c',
  'file_io.c',
  'file_io.h',
  'hardware.c',
  'list.c',
  'list.h',
  'main.c',
  'message.c',
  'mytime.c',
  'options.c',
  'signals.c',
  'suffix.c',
  'util.c',
  '../common/tuklib_open_stdxxx.c',
  '../common/tuklib_progname.c',
  '../common/tuklib_exit.c',
  '../common/tuklib_mbstr_width.c',
  '../common/tuklib_mbstr_fw.c',
]

xzinc = include_directories('../common',
  '../liblzma/api', '../../lib')

xz = executable('xz', sources,
  c_args : ['-DHAVE_CONFIG_H'],
  include_directories : [confinc, xzinc],
  link_with : liblzma,
)
