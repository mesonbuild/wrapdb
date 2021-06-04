project('bdwgc', 'c', version: '7.6.8',
        meson_version: '>=0.47.0',
        license: 'custom')


i = include_directories('include')

gc_src = files(
    'alloc.c',
    'reclaim.c',
    'allchblk.c',
    'misc.c',
    'mach_dep.c' ,
    'os_dep.c',
    'mark_rts.c',
    'headers.c' ,
    'mark.c' ,
    'obj_map.c' ,
    'blacklst.c' ,
    'finalize.c',
    'new_hblk.c' ,
    'dbg_mlc.c' ,
    'malloc.c' ,
    'stubborn.c',
    'dyn_load.c',
    'typd_mlc.c' ,
    'ptr_chck.c' ,
    'mallocx.c' 
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
