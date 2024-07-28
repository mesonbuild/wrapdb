_deps = [threads_dep, libpfm_dep]
_args = ['-D_GNU_SOURCE']
_common_srcs = files('perf_util.c')

executable('self', 'self.c', _common_srcs, c_args: _args, dependencies: _deps)
executable(
    'self_basic',
    'self_basic.c',
    _common_srcs,
    c_args: _args,
    dependencies: _deps,
)
executable(
    'self_count',
    'self_count.c',
    _common_srcs,
    c_args: _args,
    dependencies: _deps,
)
executable('task', 'task.c', _common_srcs, c_args: _args, dependencies: _deps)
executable(
    'task_attach_timeout',
    'task_attach_timeout.c',
    _common_srcs,
    c_args: _args,
    dependencies: _deps,
)
executable('syst', 'syst.c', _common_srcs, c_args: _args, dependencies: _deps)
executable(
    'notify_self',
    'notify_self.c',
    _common_srcs,
    c_args: _args,
    dependencies: _deps,
)
executable(
    'notify_group',
    'notify_group.c',
    _common_srcs,
    c_args: _args,
    dependencies: _deps,
)
executable(
    'task_smpl',
    'task_smpl.c',
    _common_srcs,
    c_args: _args,
    dependencies: _deps,
)
executable(
    'self_smpl_multi',
    'self_smpl_multi.c',
    _common_srcs,
    c_args: _args,
    dependencies: _deps,
)
executable(
    'self_pipe',
    'self_pipe.c',
    _common_srcs,
    c_args: _args,
    dependencies: _deps,
)
executable(
    'syst_count',
    'syst_count.c',
    _common_srcs,
    c_args: _args,
    dependencies: _deps,
)
executable(
    'task_cpu',
    'task_cpu.c',
    _common_srcs,
    c_args: _args,
    dependencies: _deps,
)
executable(
    'syst_smpl',
    'syst_smpl.c',
    _common_srcs,
    c_args: _args,
    dependencies: _deps,
)
executable(
    'evt2raw',
    'evt2raw.c',
    _common_srcs,
    c_args: _args,
    dependencies: _deps,
)
executable(
    'branch_smpl',
    'branch_smpl.c',
    _common_srcs,
    c_args: _args,
    dependencies: _deps,
)
executable(
    'rtop',
    'rtop.c',
    _common_srcs,
    c_args: _args,
    dependencies: [curses_dep, m_dep, _deps],
)

if host_machine.cpu_family() in ['x86', 'x86_64']
    subdir('x86')
endif
