project(
  'ffmpegthumbnailer',
  'cpp',
  license: 'LGPL-2.1-or-later',
  version: '2.2.3',
  meson_version: '>=0.54.1',
)

libavcodec_dep = dependency('libavcodec')
libavfilter_dep = dependency('libavfilter')
libavformat_dep = dependency('libavformat')
libavutil_dep = dependency('libavutil')
libjpeg_dep = dependency(
  'libjpeg',
  required: get_option('jpeg'),
)
libpng_dep = dependency(
  'libpng',
  required: get_option('png'),
)

cpp = meson.get_compiler('cpp')
if meson.version().version_compare('>= 0.62')
  dl_dep = dependency(
    'dl',
    required: get_option('gio'),
  )
else
  dl_dep = cpp.find_library(
    'dl',
    required: get_option('gio'),
  )
endif

ffmpegthumbnailer_deps = [
  libavcodec_dep,
  libavfilter_dep,
  libavformat_dep,
  libavutil_dep,
  dl_dep,
]

cdata = configuration_data()
vers = meson.project_version().split('.')
cdata.set('PACKAGE', 'ffmpegthumbnailer')
cdata.set('PACKAGE_VERSION_MAJOR', vers[0])
cdata.set('PACKAGE_VERSION_MINOR', vers[1])
cdata.set('PACKAGE_VERSION_PATCH', vers[2])
cdata.set('HAVE_PNG', libpng_dep.found())
cdata.set('HAVE_JPEG', libjpeg_dep.found())
cdata.set('ENABLE_GIO', dl_dep.found())

cfile = configure_file(
  input: 'config.h.in',
  output: 'config.h',
  format: 'cmake',
  configuration: cdata,
)

libffmpegthumbnailer_incdir = include_directories('libffmpegthumbnailer')

compfiles = files(
  'libffmpegthumbnailer/filmstripfilter.cpp',
  'libffmpegthumbnailer/moviedecoder.cpp',
  'libffmpegthumbnailer/rgbwriter.cpp',
  'libffmpegthumbnailer/stringoperations.cpp',
  'libffmpegthumbnailer/videothumbnailer.cpp',
  'libffmpegthumbnailer/videothumbnailerc.cpp',
)

if libjpeg_dep.found()
  compfiles += files('libffmpegthumbnailer/jpegwriter.cpp')
  ffmpegthumbnailer_deps += libjpeg_dep
endif

if libpng_dep.found()
  compfiles += files('libffmpegthumbnailer/pngwriter.cpp')
  ffmpegthumbnailer_deps += libpng_dep
endif

libffmpegthumbnailer = library(
  'ffmpegthumbnailer',
  compfiles,
  override_options: 'cpp_std=c++11',
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
  'libffmpegthumbnailer/videothumbnailer.h',
  'libffmpegthumbnailer/videothumbnailerc.h',
  'libffmpegthumbnailer/imagetypes.h',
  'libffmpegthumbnailer/ffmpegthumbnailertypes.h',
  'libffmpegthumbnailer/ifilter.h',
  'libffmpegthumbnailer/videoframe.h',
  'libffmpegthumbnailer/filmstripfilter.h',
  subdir: 'libffmpegthumbnailer',
)

libffmpegthumbnailer_dep = declare_dependency(
  include_directories: '.',
  link_with: libffmpegthumbnailer,
)

meson.override_dependency('libffmpegthumbnailer', libffmpegthumbnailer_dep)

subdir('test')
