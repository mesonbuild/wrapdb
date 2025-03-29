prog_align = executable(
  'align',
  'align.c',
  dependencies: lzo2_dep,
)
prog_chksum = executable(
  'chksum',
  'chksum.c',
  dependencies: lzo2_dep,
)
prog_promote = executable(
  'promote',
  'promote.c',
  dependencies: lzo2_dep,
)
prog_sizes = executable(
  'sizes',
  'sizes.c',
  dependencies: lzo2_dep,
)

test(
  'align',
  prog_align,
  suite: 'basic',
)
test(
  'chksum',
  prog_chksum,
  suite: 'basic',
)
