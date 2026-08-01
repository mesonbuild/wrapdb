src = files(
  'bsdtar.c',
  'cmdline.c',
  'creation_set.c',
  'read.c',
  'subst.c',
  'util.c',
  'write.c',
)

if host_machine.system() == 'windows'
  src += files('bsdtar_windows.c')
  src += import('windows').compile_resources(
    'bsdtar.rc',
    depend_files: 'bsdtar.exe.manifest',
  )
endif

bsdtar = executable(
  'bsdtar',
  src,
  dependencies: [libarchive_fe_dep, rx_dep],
  install: true,
)
meson.override_find_program('bsdtar', bsdtar)
