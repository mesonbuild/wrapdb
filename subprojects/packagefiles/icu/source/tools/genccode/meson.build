genccode_exe = executable(
  'genccode',
  'genccode.c',
  dependencies: [toolutil_dep, icuuc_dep],
)

meson.override_find_program('genccode', genccode_exe)
