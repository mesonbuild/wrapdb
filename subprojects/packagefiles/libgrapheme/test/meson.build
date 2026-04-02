tests = [
  'case',
  'character',
  'line',
  'sentence',
  'utf8-decode',
  'utf8-encode',
  'word',
]

tests_failing = ['line']

test_c_flags = cc.get_supported_arguments('-Wno-overlength-strings')

foreach exe_name : tests
  test_src = exe_name + '.c'
  should_fail = tests_failing.contains(exe_name)
  exe = executable(
    exe_name,
    [test_src, gen_headers, 'util.c'],
    dependencies: [libgrapheme_dep],
    c_args: test_c_flags,
  )
  test(
    exe_name,
    exe,
    workdir: meson.project_source_root(),
    should_fail: should_fail,
  )
endforeach
