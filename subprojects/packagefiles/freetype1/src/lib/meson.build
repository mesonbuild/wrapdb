if target_machine.system() == 'darwin'
    arch = 'mac'
elif target_machine.system() == 'windows'
    arch = 'win32'
elif target_machine.system() == 'linux'
    arch = 'unix'
else
    error('Architecture not supported: @0@'.format(target_machine.system()))
endif

ttf_inc = include_directories(
        '.',
        'arch/mac',
)

ttf_lib = static_library('ttf',
    include_directories: ttf_inc,
    sources: [
        'ttapi.c',
        'ttcache.c',
        'ttcalc.c',
        'ttcmap.c',
        'ttdebug.c',
        'ttextend.c',
        'ttfile.c',
        'ttgload.c',
        'ttinterp.c',
        'ttload.c',
        'ttmemory.c',
        'ttmutex.c',
        'ttobjs.c',
        'ttraster.c',
    ],
)

ttf_dep = declare_dependency(
    link_with: ttf_lib,
    include_directories: ttf_inc,
)
