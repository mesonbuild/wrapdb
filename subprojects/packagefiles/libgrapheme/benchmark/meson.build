bench_sources = files(
  'case.c',
  'character.c',
  'line.c',
  'sentence.c',
  'utf8-decode.c',
  'word.c',
)

libutf8proc_dep = dependency('libutf8proc')

bench_c_flags = ['-Wno-overlength-strings']

foreach bench_src : bench_sources
  exe_name = bench_src.full_path().split('/')[-1].split('.')[0]
  exe = executable(
    exe_name,
    [bench_src, gen_headers, 'util.c'],
    dependencies: [libutf8proc_dep, libgrapheme_dep],
    install: false,
    c_args: bench_c_flags,
  )
  benchmark(
    exe_name,
    exe,
    workdir: meson.project_source_root(),
  )
endforeach
