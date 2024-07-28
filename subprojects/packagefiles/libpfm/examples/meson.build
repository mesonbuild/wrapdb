_deps = [m_dep, libpfm_dep]
if host_machine.system() == 'linux'
    _deps += [threads_dep, rt_dep]
elif host_machine.system() == 'windows'
    _deps += [cc.find_library('gnurx', required: false)]
endif

executable(
    'showevtinfo',
    'showevtinfo.c',
    c_args: ['-D_GNU_SOURCE'],
    dependencies: _deps,
)
executable(
    'check_events',
    'check_events.c',
    c_args: ['-D_GNU_SOURCE'],
    dependencies: _deps,
)
