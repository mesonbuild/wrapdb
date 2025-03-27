add_languages('cpp')
cpp = meson.get_compiler('cpp')

testlib = static_library(
  'testlib',
  objects: minizip_ng.extract_all_objects(
    recursive: false,
  ),
  dependencies: [
    bcrypt_dep,
    bsd_dep,
    crypt_dep,
    iconv_dep,
    bzip2_dep,
    lzma_dep,
    zlib_dep,
    zstd_dep,
    minizip_ng_dep,
  ],
)

testinc = include_directories('.')
testlib_dep = declare_dependency(
  include_directories: [depinc, testinc],
  link_with: testlib,
)

test_srcs = files(
  'test_crypt.cc',
  'test_encoding.cc',
  'test_path.cc',
  'test_stream.cc',
  'test_stream_compress.cc',
  'test_stream_crypt.cc',
)

test_srcs += files('test_main.cc')

if cpp.get_id() == 'msvc'
  test_srcs += 'test_file.cc'
endif

test(
  'gtest_minizip',
  executable(
    'gtest_minizip',
    test_srcs,
    cpp_args: margs,
    dependencies: [gtest_dep, testlib_dep],
  ),
  workdir: testdir,
  timeout: 300,
)
