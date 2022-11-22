gencmn_exe = executable(
  'gencmn',
  'gencmn.c',
  dependencies: [toolutil_dep, icuuc_dep],
  install: true,
)

meson.override_find_program('gencmn', gencmn_exe)
