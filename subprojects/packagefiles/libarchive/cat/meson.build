bsdcat = executable(
  'bsdcat',
  files('bsdcat.c', 'cmdline.c'),
  dependencies: libarchive_fe_dep,
  install: true,
)
meson.override_find_program('bsdcat', bsdcat)
