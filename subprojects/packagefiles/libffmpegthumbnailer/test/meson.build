if not libpng_dep.found()
  subdir_done()
endif

ffmpegthumbnailertest = executable(
  'ffmpegthumbnailertest',
  'histogramtest.cpp',
  'testrunner.cpp',
  'videothumbnailertest.cpp',
  'videothumbnailerctest.cpp',
  cpp_args: '-DTEST_DATADIR="@0@"'.format(meson.current_source_dir()),
  include_directories: ['testframework', confinc],
  override_options: 'cpp_std=c++14',
  dependencies: libffmpegthumbnailer_dep,
)

test('ffmpegthumbnailertest', ffmpegthumbnailertest)
