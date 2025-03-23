inc = include_directories('..')

glpsol = executable(
  'glpsol',
  'glpsol.c',
  include_directories: inc,
  dependencies: [glpk_dep, libm_dep],
  install: true,
)

test(
  'glpsol version',
  glpsol,
  args: '--version',
)
test(
  'glpsol mps',
  glpsol,
  args: ['--mps', files('murtagh.mps'), '--max'],
  workdir: meson.current_source_dir(),
)
