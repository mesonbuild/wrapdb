libffmpegthumbnailer_incdir = include_directories('.')

compfiles = files(
  'filmstripfilter.cpp',
  'moviedecoder.cpp',
  'rgbwriter.cpp',
  'stringoperations.cpp',
  'videothumbnailer.cpp',
  'videothumbnailerc.cpp',
)

if libjpeg_dep.found()
  compfiles += files('jpegwriter.cpp')
endif

if libpng_dep.found()
  compfiles += files('pngwriter.cpp')
endif

libffmpegthumbnailer = library(
  'ffmpegthumbnailer',
  compfiles,
  override_options: 'cpp_std=c++14',
  include_directories: confinc,
  dependencies: ffmpegthumbnailer_deps,
  install: true,
  version: '4.15.1',
)

pkg = import('pkgconfig')
pkg.generate(
  libffmpegthumbnailer,
  description: 'Generates thumbnails for movie files',
)

install_headers(
  'videothumbnailer.h',
  'videothumbnailerc.h',
  'imagetypes.h',
  'ffmpegthumbnailertypes.h',
  'ifilter.h',
  'videoframe.h',
  'filmstripfilter.h',
  subdir: 'libffmpegthumbnailer',
)

depinc = include_directories('.')
libffmpegthumbnailer_dep = declare_dependency(
  include_directories: depinc,
  link_with: libffmpegthumbnailer,
)

meson.override_dependency('libffmpegthumbnailer', libffmpegthumbnailer_dep)
