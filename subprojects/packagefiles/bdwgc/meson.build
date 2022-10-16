project(
  'bdwgc',
  'c',
  version: '8.2.2',
  meson_version: '>=0.47.0',
  license: 'custom',
)

add_project_arguments('-D_GNU_SOURCE', language: 'c')

gc_src = files(
  'allchblk.c',
  'alloc.c',
  'blacklst.c',
  'dbg_mlc.c',
  'dyn_load.c',
  'finalize.c',
  'gc_dlopen.c',
  'headers.c',
  'mach_dep.c',
  'malloc.c',
  'mallocx.c',
  'mark.c',
  'mark_rts.c',
  'misc.c',
  'new_hblk.c',
  'obj_map.c',
  'os_dep.c',
  'ptr_chck.c',
  'reclaim.c',
  'specific.c',
  'typd_mlc.c',
)

if host_machine.cpu().contains('sparc')
  gc_src += files('sparc_mach_dep.S')
endif

gclib = library(
  'gc',
  gc_src,
  include_directories: 'include',
)

bdwgc_dep = declare_dependency(
  include_directories: 'include',
  link_with: gclib,
)
