configure_file(
  input: '../port/libport_config.h.cmake.in',
  output: 'libport_config.h',
  format: 'cmake@',
  configuration: cdata,
)

tpinc = include_directories('../port')
if not cc.has_function('getopt')
  tpl = static_library(
    'tiff_port',
    '../port/getopt.c',
    include_directories: tpinc,
  )
  tiff_port = declare_dependency(
    include_directories: tpinc,
    link_with: tpl,
  )
else
  tiff_port = declare_dependency(
    include_directories: tpinc,
  )
endif

tests = [
  'ascii_tag',
  'custom_dir',
  'custom_dir_EXIF_231',
  'defer_strile_loading',
  'defer_strile_writing',
  'rewrite_tag',
  'test_append_to_strip',
  'test_directory',
  'test_IFD_enlargement',
  'test_open_options',
  'test_signed_tags',
  'testtypes',
]

foreach t : tests
  test(t, executable(t, '@0@.c'.format(t), dependencies: [libtiff4_dep, tiff_port]))
endforeach

test('short_tag', executable('short_tag', 'short_tag.c', 'check_tag.c', dependencies: [libtiff4_dep, tiff_port]))
test('long_tag', executable('long_tag', 'long_tag.c', 'check_tag.c', dependencies: [libtiff4_dep, tiff_port]))

test(
  'strip_rw',
  executable(
    'strip_rw',
    'strip_rw.c',
    'strip.c',
    'test_arrays.c',
    dependencies: [libtiff4_dep, tiff_port],
  )
)

if jpeg_dep.found()
  test('raw_decode', executable('raw_decode', 'raw_decode.c', dependencies: [libtiff4_dep, tiff_port, jpeg_dep]), workdir: meson.current_source_dir())
endif
