deps = [threads_dep, libpfm_dep]
args = ['-D_GNU_SOURCE']
common_srcs = files('perf_util.c')

executable(
  'self',
  'self.c',
  common_srcs,
  c_args: args,
  dependencies: deps,
)
executable(
  'self_basic',
  'self_basic.c',
  common_srcs,
  c_args: args,
  dependencies: deps,
)
executable(
  'self_count',
  'self_count.c',
  common_srcs,
  c_args: args,
  dependencies: deps,
)
executable(
  'task',
  'task.c',
  common_srcs,
  c_args: args,
  dependencies: deps,
)
executable(
  'task_attach_timeout',
  'task_attach_timeout.c',
  common_srcs,
  c_args: args,
  dependencies: deps,
)
executable(
  'syst',
  'syst.c',
  common_srcs,
  c_args: args,
  dependencies: deps,
)
executable(
  'notify_self',
  'notify_self.c',
  common_srcs,
  c_args: args,
  dependencies: deps,
)
executable(
  'notify_group',
  'notify_group.c',
  common_srcs,
  c_args: args,
  dependencies: deps,
)
executable(
  'task_smpl',
  'task_smpl.c',
  common_srcs,
  c_args: args,
  dependencies: deps,
)
executable(
  'self_smpl_multi',
  'self_smpl_multi.c',
  common_srcs,
  c_args: args,
  dependencies: deps,
)
executable(
  'self_pipe',
  'self_pipe.c',
  common_srcs,
  c_args: args,
  dependencies: deps,
)
executable(
  'syst_count',
  'syst_count.c',
  common_srcs,
  c_args: args,
  dependencies: deps,
)
executable(
  'task_cpu',
  'task_cpu.c',
  common_srcs,
  c_args: args,
  dependencies: deps,
)
executable(
  'syst_smpl',
  'syst_smpl.c',
  common_srcs,
  c_args: args,
  dependencies: deps,
)
executable(
  'evt2raw',
  'evt2raw.c',
  common_srcs,
  c_args: args,
  dependencies: deps,
)
executable(
  'branch_smpl',
  'branch_smpl.c',
  common_srcs,
  c_args: args,
  dependencies: deps,
)
executable(
  'rtop',
  'rtop.c',
  common_srcs,
  c_args: args,
  dependencies: [curses_dep, m_dep, deps],
)

if host_machine.cpu_family() in ['x86', 'x86_64']
  subdir('x86')
endif
