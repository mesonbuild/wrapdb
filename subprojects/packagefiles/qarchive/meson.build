project(
  'QArchive',
  'cpp',
  version: '2.2.1',
  license: 'BSD-3-Clause',
  default_options: ['cpp_std=c++17'],
  meson_version: '>=0.49.0'
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

configure_file(
  format: 'cmake@',
  input: 'other/cmake/config.h.in',
  output: 'config.h',
  configuration: configuration_data({'QARCHIVE_STATIC': get_option('default_library') == 'static'})
)

src = files(
  'src/qarchive_enums.cc',
  'src/qarchiveutils_p.cc',
  'src/qarchivememoryfile.cc',
  'src/qarchivememoryextractoroutput.cc',
  'src/qarchiveioreader_p.cc',
  'src/qarchiveextractor_p.cc',
  'src/qarchiveextractor.cc',
  'src/qarchivecompressor_p.cc',
  'src/qarchivecompressor.cc',
  'src/qarchivediskextractor.cc',
  'src/qarchivememoryextractor.cc',
  'src/qarchivediskcompressor.cc',
  'src/qarchivememorycompressor.cc',
)

headers = files(
  'include/qarchive_enums.hpp',
  'include/qarchiveutils_p.hpp',
  'include/qarchivememoryfile.hpp',
  'include/qarchivememoryextractoroutput.hpp',
  'include/qarchiveioreader_p.hpp',
  'include/qarchiveextractor_p.hpp',
  'include/qarchiveextractor.hpp',
  'include/qarchivecompressor_p.hpp',
  'include/qarchivecompressor.hpp',
  'include/qarchivediskextractor.hpp',
  'include/qarchivememoryextractor.hpp',
  'include/qarchivediskcompressor.hpp',
  'include/qarchivememorycompressor.hpp',
  'include/qarchive_global.hpp',
)

include_dirs = include_directories('include', '.')

moc_files = qt.preprocess(
  moc_sources: src,
  moc_headers: headers,
  include_directories: include_dirs,
  dependencies: qt_dep
)

qarchive_lib = library(
  'qarchive',
  src,
  moc_files,
  cpp_args: '-DQARCHIVE_BUILD',
  include_directories: include_dirs,
  dependencies: [libarchive_dep, qt_dep]
)

qarchive_dep = declare_dependency(
  include_directories: include_dirs,
  link_with: qarchive_lib
)

if meson.version().version_compare('>=0.54.0')
  meson.override_dependency('qarchive', qarchive_dep)
endif

if get_option('tests')
  test_src = files(
    'tests/main.cc',
    'tests/TestRunner.cc',
    'tests/QArchiveDiskCompressorTests.cc',
    'tests/QArchiveMemoryCompressorTests.cc',
    'tests/QArchiveDiskExtractorTests.cc',
    'tests/QArchiveMemoryExtractorTests.cc',
  )

  test_headers = files(
    'tests/TestRunner.hpp',
    'tests/QArchiveTestCases.hpp',
    'tests/QArchiveDiskCompressorTests.hpp',
    'tests/QArchiveMemoryCompressorTests.hpp',
    'tests/QArchiveDiskExtractorTests.hpp',
    'tests/QArchiveMemoryExtractorTests.hpp',
  )

  test_include_dirs = include_directories('tests')

  test_moc_files = qt.preprocess(
    moc_sources: test_src,
    moc_headers: test_headers,
    include_directories: test_include_dirs,
    dependencies: qt_dep,
  )

  test_dep = dependency(
    'qt6',
    modules: ['Test', 'Concurrent'],
    required: get_option('qt6'),
  )
  if not test_dep.found()
    test_dep = dependency('qt5', modules: ['Test', 'Concurrent'])
  endif

  test_exe = executable(
    'QArchiveTests',
    test_src, test_moc_files,
    include_directories: include_directories('tests'),
    dependencies: [qarchive_dep, test_dep],
  )

  test('QArchiveTests', test_exe)
endif
