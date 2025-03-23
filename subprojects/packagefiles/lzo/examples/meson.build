prog_dict = executable(
  'dict',
  'dict.c',
  dependencies: lzo2_dep,
)
prog_lzopack = executable(
  'lzopack',
  'lzopack.c',
  dependencies: lzo2_dep,
)
prog_overlap = executable(
  'overlap',
  'overlap.c',
  dependencies: lzo2_dep,
)
prog_precomp = executable(
  'precomp',
  'precomp.c',
  dependencies: lzo2_dep,
)
prog_precomp2 = executable(
  'precomp2',
  'precomp2.c',
  dependencies: lzo2_dep,
)
prog_simple = executable(
  'simple',
  'simple.c',
  dependencies: lzo2_dep,
)

test(
  'simple',
  prog_simple,
  suite: 'basic',
)
