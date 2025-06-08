tests = [
  'case',
  'character',
  'line',
  'sentence',
  'utf8-decode',
  'utf8-encode',
  'word',
]

test_c_flags = cc.get_supported_arguments('-Wno-overlength-strings')

foreach test : tests
  test_src = test + '.c'
  exe = executable(
    'test-' + test,
    [test_src, gen_headers, 'util.c'],
    dependencies: [libgrapheme_dep],
    c_args: test_c_flags,
  )
  test(
    exe_name,
    exe,
    workdir: meson.project_source_root(),
  )
endforeach
