src = [
  'bsdtar.c',
  'cmdline.c',
  'creation_set.c',
  'read.c',
  'subst.c',
  'util.c',
  'write.c',
]

if host_machine.system() == 'windows'
  src += 'bsdtar_windows.c'
endif

bsdtar = executable(
  'bsdtar',
  src,
  dependencies: [libarchive_fe_dep, rx_dep],
  install: true,
)
meson.override_find_program('bsdtar', bsdtar)
