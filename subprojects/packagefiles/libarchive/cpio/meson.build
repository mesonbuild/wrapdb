src = ['cmdline.c', 'cpio.c']

if host_machine.system() == 'windows'
  src += 'cpio_windows.c'
endif

bsdcpio = executable(
  'bsdcpio',
  src,
  dependencies: libarchive_fe_dep,
  install: true,
)
meson.override_find_program('bsdcpio', bsdcpio)
