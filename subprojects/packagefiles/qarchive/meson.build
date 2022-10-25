project(
  'QArchive',
  'cpp',
  version: '2.0.2',
  license: 'BSD-3-Clause',
  default_options: ['cpp_std=c++11'],
  meson_version: '>=0.49.0'
)

qt5 = import('qt5')

# NOTE: >2.0.2 depends on libarchive-3.5.0 (uses `archive_write_open2()`)
libarchive_dep = dependency('libarchive')
qt5core_dep = dependency('qt5', modules: ['Core'])

configure_file(
  format: 'cmake@',
  input: 'other/cmake/config.h.in',
  output: 'config.h',
  configuration: configuration_data({'QARCHIVE_STATIC': get_option('static')})
)

src = files(
  'src/qarchivediskcompressor.cc',
  'src/qarchivediskextractor.cc',
  'src/qarchive_enums.cc',
  'src/qarchivediskcompressor_p.cc',
  'src/qarchivediskextractor_p.cc',
  'src/qarchiveutils_p.cc',
  'src/qarchiveioreader_p.cc',
)

headers = files(
  'include/qarchive_enums.hpp',
  'include/qarchivediskextractor.hpp',
  'include/qarchivediskcompressor.hpp',
  'include/qarchive_global.hpp',
  'include/qarchivediskcompressor_p.hpp',
  'include/qarchivediskextractor_p.hpp',
  'include/qarchiveutils_p.hpp',
  'include/qarchiveioreader_p.hpp',
)

include_dirs = include_directories('include', '.')

moc_files = qt5.preprocess(
  moc_sources: src,
  moc_headers: headers,
  include_directories: include_dirs,
  dependencies: qt5core_dep
)

qarchive_lib = library(
  'qarchive',
  src,
  moc_files,
  include_directories: include_dirs,
  dependencies: [libarchive_dep, qt5core_dep]
)

qarchive_dep = declare_dependency(
  include_directories: include_dirs,
  link_with: qarchive_lib
)

if meson.version().version_compare('>=0.54.0')
  meson.override_dependency('qarchive', qarchive_dep)
endif
