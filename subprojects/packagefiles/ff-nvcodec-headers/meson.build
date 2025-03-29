project(
  'ff-nvcodec-headers',
  version: '11.1.5.1',
)

install_subdir(
  'include/ffnvcodec',
  install_dir: get_option('includedir'),
)

incdir = include_directories('include')
ffnvcodec_dep = declare_dependency(
  include_directories: incdir,
)

pkg = import('pkgconfig')
pkg.generate(
  name: 'ffnvcodec',
  description: 'FFmpeg version of Nvidia Codec SDK headers',
)
