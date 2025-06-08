benches = ['case', 'character', 'line', 'sentence', 'utf8-decode', 'word']

libutf8proc_dep = dependency('libutf8proc')

bench_c_flags = cc.get_supported_arguments('-Wno-overlength-strings')

foreach exe_name : benches
  src = exe_name + '.c'
  exe = executable(
    'bench-' + exe_name,
    [src, gen_headers, 'util.c'],
    dependencies: [libutf8proc_dep, libgrapheme_dep],
    c_args: bench_c_flags,
  )
  benchmark(
    exe_name,
    exe,
    workdir: meson.project_source_root(),
  )
endforeach
