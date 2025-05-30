test_sources = files(
  'case.c',
  'character.c',
  'line.c',
  'sentence.c',
  'utf8-decode.c',
  'utf8-encode.c',
  'word.c',
)

test_c_flags = ['-Wno-overlength-strings']

foreach test_src : test_sources
  exe_name = test_src.full_path().split('/')[-1].split('.')[0]
  exe = executable(
    exe_name,
    [test_src, gen_headers, 'util.c'],
    dependencies: [libgrapheme_dep],
    install: false,
    c_args: test_c_flags,
  )
  test(
    exe_name,
    exe,
    workdir: meson.project_source_root(),
  )
endforeach
