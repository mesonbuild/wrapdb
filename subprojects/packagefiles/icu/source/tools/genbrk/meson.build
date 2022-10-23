genbrk_exe = executable(
  'genbrk',
  'genbrk.cpp',
  dependencies: [toolutil_dep, icuuc_dep],
)

meson.override_find_program('genbrk', genbrk_exe)
