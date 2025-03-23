if not get_option('tests')
  subdir_done()
endif

tests = [
  # 'extract',
  'fuzzer',
  # 'fuzzer-persistent',
  'gps',
  'integers',
  'mem',
  # 'mnote',
  'null',
  'parse',
  # 'parse-from-data',
  'sorted',
  'tagtable',
  'value',
]

foreach t : tests
  test(
    'test-@0@'.format(t),
    executable(
      'test-@0@'.format(t),
      'test-@0@.c'.format(t),
      dependencies: exif_dep,
    ),
    workdir: meson.current_source_dir(),
  )
endforeach
