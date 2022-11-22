testlib = static_library(
  'staticlib',
  objects: libffmpegthumbnailer.extract_all_objects(recursive: false),
  include_directories: libffmpegthumbnailer_incdir,
  dependencies: [ffmpegthumbnailer_deps, libffmpegthumbnailer_dep],
)

tdepinc = [include_directories('.'), depinc]
testdep = declare_dependency(
  include_directories: tdepinc,
  link_with: testlib,
)

ffmpegthumbnailertest = executable(
  'ffmpegthumbnailertest',
  'histogramtest.cpp',
  'testrunner.cpp',
  'videothumbnailertest.cpp',
  'videothumbnailerctest.cpp',
  cpp_args: '-DTEST_DATADIR="@0@"'.format(meson.current_source_dir()),
  dependencies: [catch_dep, testdep],
)

test('ffmpegthumbnailertest', ffmpegthumbnailertest)
