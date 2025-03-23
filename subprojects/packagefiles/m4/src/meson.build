m4_src = [
  'builtin.c',
  'debug.c',
  'eval.c',
  'format.c',
  'freeze.c',
  'input.c',
  'macro.c',
  'output.c',
  'path.c',
  'symtab.c',
  'm4.c',
]

nononnull_h = configure_file(
  input: 'nononnull.h.meson',
  output: 'nononnull.h',
  copy: true,
)

m4 = executable(
  'm4',
  m4_src,
  nononnull_h,
  dependencies: m4_dep,
  install: true,
)
