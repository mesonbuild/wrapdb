project('ffmpegthumbnailer', 'cpp',
  version : '2.2.2',
  default_options : ['warning_level=0', 'cpp_std=c++11'],
  meson_version: '>=0.47.0'
)

libavcodec_dep = dependency('libavcodec')
libavfilter_dep = dependency('libavfilter')
libavformat_dep = dependency('libavformat')
libavutil_dep = dependency('libavutil')
libjpeg_dep = dependency('libjpeg', required : get_option('jpeg'))
libpng_dep = dependency('libpng', required : get_option('png'))

ffmpegthumbnailer_deps = [ libavcodec_dep, libavfilter_dep, libavformat_dep, libavutil_dep, libjpeg_dep, libpng_dep ]

cdata = configuration_data()
cpp = meson.get_compiler('cpp')

cdata.set('HAVE_PNG', libjpeg_dep.found())
cdata.set('HAVE_JPEG', libpng_dep.found())

cfile = configure_file(
  output : 'config.h',
  configuration : cdata,
)

libffmpegthumbnailer_incdir = include_directories([ '.', 'libffmpegthumbnailer' ])

compfiles = [
  'libffmpegthumbnailer/filmstripfilter.cpp',
  'libffmpegthumbnailer/moviedecoder.cpp',
  'libffmpegthumbnailer/rgbwriter.cpp',
  'libffmpegthumbnailer/stringoperations.cpp',
  'libffmpegthumbnailer/videothumbnailer.cpp',
  'libffmpegthumbnailer/videothumbnailerc.cpp',
]

if libjpeg_dep.found()
  compfiles += 'libffmpegthumbnailer/jpegwriter.cpp'
  ffmpegthumbnailer_deps += libjpeg_dep
endif

if libpng_dep.found()
  compfiles += 'libffmpegthumbnailer/pngwriter.cpp'
  ffmpegthumbnailer_deps += libpng_dep
endif

libffmpegthumbnailer = library('ffmpegthumbnailer',
  compfiles,
  dependencies : ffmpegthumbnailer_deps,
  install : true,
  version : '4.15.1',
)

pkg = import('pkgconfig')
pkg.generate(libffmpegthumbnailer, description : 'Generates thumbnails for movie files')

install_headers(
  'libffmpegthumbnailer/videothumbnailer.h',
  'libffmpegthumbnailer/videothumbnailerc.h',
  'libffmpegthumbnailer/imagetypes.h',
  'libffmpegthumbnailer/ffmpegthumbnailertypes.h',
  'libffmpegthumbnailer/ifilter.h',
  'libffmpegthumbnailer/videoframe.h',
  'libffmpegthumbnailer/filmstripfilter.h',
  subdir : 'libffmpegthumbnailer',
)

libffmpegthumbnailer_dep = declare_dependency(
  include_directories : libffmpegthumbnailer_incdir,
  link_with : libffmpegthumbnailer,
)
