project(
  'ffmpegthumbnailer',
  'cpp',
  license: 'LGPL-2.1-or-later',
  version: '2.2.4',
  meson_version: '>=0.56.0',
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
  libjpeg_dep,
  libpng_dep,
  dl_dep,
]

cdata = configuration_data()
vers = meson.project_version().split('.')
cdata.set('PACKAGE', meson.project_name())
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

confinc = include_directories('.')
subdir('libffmpegthumbnailer')
subdir('test')
