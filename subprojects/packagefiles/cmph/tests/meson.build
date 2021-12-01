tests = [
  'select_tests',
  'compressed_seq_tests',
  'compressed_rank_tests',
] + (
  # XXX this test relies on <unistd.h> and won't compile on Windows
  host_machine.system() != 'windows' ? ['cmph_benchmark_test'] : []
) + (
  # XXX graph_tests are broken on compilers which don't identify as __GNUC__ because
  # of bogus definition of DEBUGP macro which causes segfault/access violation in
  # vfprintf argument parsing
  cc.get_argument_syntax() == 'gcc' and host_machine.system() != 'windows' ? ['graph_tests'] : []
)

foreach t: tests
  test(t, executable(t, [t + '.c'] + (t == 'cmph_benchmark_test' ? ['../src/cmph_benchmark.c'] : []),
      dependencies: cmph_dep,
      include_directories: include_directories('..'),
      c_pch: 'workaround/stdlib_pch.h',
  ))
endforeach

programs = ['packed_mphf_tests', 'mphf_tests']

foreach p: programs
  executable(p, p + '.c',
    dependencies: cmph_dep,
    # XXX those programs use bogus include path '../wingetopt.h' so we trick them
    # to use the correct header by adding the '/workaround' subdir so the path
    # resolves to the actual file '../src/wingetopt.h'
    include_directories: include_directories('..', '../src/workaround'),
    build_by_default: false,
    c_pch: 'workaround/stdlib_pch.h',
  )
endforeach
