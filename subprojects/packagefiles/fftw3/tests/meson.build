bench_sources = files(
  'bench.c',
  'fftw-bench.c',
  'hook.c',
)

# Problems use the libbench2 syntax, as tests/check.pl does: in-place (i) or
# out-of-place (o), forward (f) or backward (b), complex (c), real (r) or
# r2r (k) with a kind per dimension, dimensions separated by x, vector loops
# (*n and vn), split arrays (//) and destroyable input (d).
dft_problems = [
  '//ibc35',
  '//ofc64',
  'dofc32x12',
  'ibc12',
  'ibc15x17',
  'ibc210',
  'ibc33v3',
  'ibc4',
  'ibc64',
  'ifc1024',
  'ifc101',
  'ifc16',
  'ifc2',
  'ifc9',
  'obc15',
  'obc256',
  'obc3',
  'obc4096',
  'obc8',
  'obc8x12x16',
  'obc97',
  'ofc1',
  'ofc1000',
  'ofc11',
  'ofc128',
  'ofc13',
  'ofc16x16v5',
  'ofc17',
  'ofc32',
  'ofc32x64',
  'ofc4099',
  'ofc5',
  'ofc64*4',
  'ofc6x5x4x3',
  'ofc7',
]
rdft_problems = [
  '//obr21',
  '//ofr32',
  'dobr12x10',
  'ibr100',
  'ibr15x16',
  'ibr16',
  'ibr5',
  'ifr1000',
  'ifr12',
  'ifr4',
  'ifr64',
  'obr17v4',
  'obr256',
  'obr3',
  'obr32',
  'obr4096',
  'obr8',
  'obr8x12x16',
  'ofr1',
  'ofr1024',
  'ofr128',
  'ofr15',
  'ofr17',
  'ofr2',
  'ofr32x64',
  'ofr64*3',
  'ofr7',
  'ofr97',
]
r2r_problems = [
  'ik15o01',
  'ik16e10',
  'ik8hx6e11',
  'ok10e01*3',
  'ok12e00x10o11',
  'ok16o10',
  'ok17o11',
  'ok30b',
  'ok31e11',
  'ok31f',
  'ok32e00',
  'ok32e10',
  'ok32h',
  'ok32o00',
  'ok33e01',
  'ok33o01',
  'ok9o10v4',
]
threads_problems = [
  'ibc96x64',
  'obr64x48',
  'ofc1024',
  'ofc32x32x32',
  'ofr2048',
  'ok64e10x32o01',
]

bench_tests = {}
foreach kind, options_problems : {
  'dft': [[], dft_problems],
  'rdft': [[], rdft_problems],
  'r2r': [[], r2r_problems],
  'estimate': [['-oestimate'], dft_problems + rdft_problems + r2r_problems],
  'threads': [['-onthreads=2'], threads_problems],
}
  args = options_problems[0]
  foreach problem : options_problems[1]
    args += ['--verify', problem]
  endforeach
  bench_tests += {
    kind: args,
  }
endforeach
