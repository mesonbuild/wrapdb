catch_dep = dependency(
  'catch',
  required: false,
)
if not catch_dep.found() or not libpng_dep.found()
  subdir_done()
endif

testlib = static_library(
  'staticlib',
  objects: libffmpegthumbnailer.extract_all_objects(
    recursive: false,
  ),
  include_directories: libffmpegthumbnailer_incdir,
  dependencies: [ffmpegthumbnailer_deps, libffmpegthumbnailer_dep],
)

testdep = declare_dependency(
  include_directories: ['.', depinc],
  link_with: testlib,
)

ffmpegthumbnailertest = executable(
  'ffmpegthumbnailertest',
  'histogramtest.cpp',
  'testrunner.cpp',
  'videothumbnailertest.cpp',
  'videothumbnailerctest.cpp',
  cpp_args: '-DTEST_DATADIR="@0@"'.format(meson.current_source_dir()),
  override_options: 'cpp_std=c++11',
  dependencies: [catch_dep, testdep],
)

test('ffmpegthumbnailertest', ffmpegthumbnailertest)
