project(
  'QArchive',
  'cpp',
  version: '2.2.3',
  license: 'BSD-3-Clause',
  default_options: ['cpp_std=c++17'],
  meson_version: '>=0.49.0',
)

libarchive_dep = dependency('libarchive')
qt_dep = dependency('qt6', modules: ['Core'], required: get_option('qt6'))
if qt_dep.found() and meson.version().version_compare('>=0.57.0')
  qt = import('qt6')
elif qt_dep.found() and get_option('qt6').enabled()
  error('Qt6 support needs meson 0.57.0 or higher')
else
  qt_dep = dependency('qt5', modules: ['Core'])
  qt = import('qt5')
endif

conf = configure_file(
  format: 'cmake@',
  input: 'other/cmake/config.h.in',
  output: 'config.h',
  configuration: configuration_data({'QARCHIVE_STATIC': get_option('default_library') == 'static'}),
)

src = files(
  'src/qarchive_enums.cc',
  'src/qarchivecompressor.cc',
  'src/qarchivecompressor_p.cc',
  'src/qarchivediskcompressor.cc',
  'src/qarchivediskextractor.cc',
  'src/qarchiveextractor.cc',
  'src/qarchiveextractor_p.cc',
  'src/qarchiveioreader_p.cc',
  'src/qarchivememorycompressor.cc',
  'src/qarchivememoryextractor.cc',
  'src/qarchivememoryextractoroutput.cc',
  'src/qarchivememoryfile.cc',
  'src/qarchiveutils_p.cc',
)

headers = files(
  'include/qarchivecompressor.hpp',
  'include/qarchivecompressor_p.hpp',
  'include/qarchivediskcompressor.hpp',
  'include/qarchivediskextractor.hpp',
  'include/qarchiveextractor.hpp',
  'include/qarchiveextractor_p.hpp',
  'include/qarchivememorycompressor.hpp',
  'include/qarchivememoryextractor.hpp',
  'include/qarchivememoryextractoroutput.hpp',
)

maininc = include_directories('include')

moc_files = qt.preprocess(
  moc_sources: [],
  moc_headers: headers,
  include_directories: maininc,
  dependencies: qt_dep,
)

qarchive_lib = library(
  'QArchive',
  src,
  moc_files,
  cpp_args: '-DQARCHIVE_BUILD',
  include_directories: maininc,
  dependencies: [libarchive_dep, qt_dep],
  install: true,
)

pconf = import('pkgconfig')
pconf.generate(qarchive_lib, description: 'A Qt wrapper for libarchive.')

install_headers(
  'include/qarchive_enums.hpp',
  'include/qarchive_global.hpp',
  'include/qarchivecompressor.hpp',
  'include/qarchivediskcompressor.hpp',
  'include/qarchivediskextractor.hpp',
  'include/qarchiveextractor.hpp',
  'include/qarchivememorycompressor.hpp',
  'include/qarchivememoryextractor.hpp',
  'include/qarchivememoryextractoroutput.hpp',
  'include/qarchivememoryfile.hpp',
  'QArchive',
  conf,
  subdir: 'QArchive',
)

depinc = include_directories('.')
qarchive_dep = declare_dependency(
  include_directories: depinc,
  link_with: qarchive_lib,
)

if meson.version().version_compare('>=0.54.0')
  meson.override_dependency('qarchive', qarchive_dep)
endif

if get_option('tests')
  test_src = files(
    'tests/QArchiveDiskCompressorTests.cc',
    'tests/QArchiveDiskExtractorTests.cc',
    'tests/QArchiveMemoryCompressorTests.cc',
    'tests/QArchiveMemoryExtractorTests.cc',
    'tests/TestRunner.cc',
    'tests/main.cc',
  )

  test_headers = files(
    'tests/QArchiveDiskCompressorTests.hpp',
    'tests/QArchiveDiskExtractorTests.hpp',
    'tests/QArchiveMemoryCompressorTests.hpp',
    'tests/QArchiveMemoryExtractorTests.hpp',
    'tests/TestRunner.hpp',
  )

  test_include_dirs = include_directories('include', 'tests')

  test_moc_files = qt.preprocess(
    moc_sources: [],
    moc_headers: test_headers,
    include_directories: test_include_dirs,
    dependencies: qt_dep,
  )

  test_dep = dependency(
    'qt6',
    modules: ['Test', 'Core', 'Concurrent'],
    required: get_option('qt6'),
  )
  if not test_dep.found()
    test_dep = dependency('qt5', modules: ['Test', 'Core', 'Concurrent'])
  endif

  test_exe = executable(
    'QArchiveTests',
    test_src,
    test_moc_files,
    include_directories: test_include_dirs,
    cpp_args: '-DBUILD_TESTS',
    dependencies: [qarchive_dep, test_dep],
  )

  test('QArchiveTests', test_exe)
endif
