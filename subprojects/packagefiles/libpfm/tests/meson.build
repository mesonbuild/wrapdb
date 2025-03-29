srcs = files('validate.c')
deps = [m_dep, libpfm_dep]

if host_machine.cpu_family() in ['x86', 'x86_64']
  srcs += files('validate_x86.c')
elif host_machine.cpu_family() in ['mips', 'mips64']
  srcs += files('validate_mips.c')
elif host_machine.cpu_family() == 'arm'
  srcs += files('validate_arm.c')
elif host_machine.cpu_family() == 'aarch64'
  srcs += files('validate_arm64.c')
elif host_machine.cpu_family() in ['ppc', 'ppc64']
  srcs += files('validate_power.c')
endif

if host_machine.system() == 'linux'
  srcs += files('validate_perf.c')
  deps += threads_dep
endif

val = executable(
  'validate',
  srcs,
  c_args: '-D_GNU_SOURCE',
  dependencies: deps,
)
test('validate', val)
