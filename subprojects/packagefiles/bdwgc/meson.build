project('bdwgc', 'c', version: '8.2.0',
        meson_version: '>=0.47.0',
        license: 'custom')

add_project_arguments('-D_GNU_SOURCE', language: 'c')

i = include_directories('include')

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
gc_deps = []
defs = []
gclib = library('gc', gc_src,
    dependencies: gc_deps,
    c_args: defs,
    include_directories: i)

bdwgc_dep = declare_dependency(
    include_directories: i,
    link_with: gclib
)
