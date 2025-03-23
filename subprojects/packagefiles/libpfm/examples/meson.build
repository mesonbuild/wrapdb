deps = [m_dep, libpfm_dep]
if host_machine.system() == 'linux'
  deps += [threads_dep, rt_dep]
elif host_machine.system() == 'windows'
  deps += [
    cc.find_library(
      'gnurx',
      required: false,
    ),
  ]
endif

executable(
  'showevtinfo',
  'showevtinfo.c',
  c_args: ['-D_GNU_SOURCE'],
  dependencies: deps,
)
executable(
  'check_events',
  'check_events.c',
  c_args: ['-D_GNU_SOURCE'],
  dependencies: deps,
)
