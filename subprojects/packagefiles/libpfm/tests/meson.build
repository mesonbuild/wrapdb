_srcs = files('validate.c')
_deps = [m_dep, libpfm_dep]

if host_machine.cpu_family() in ['x86', 'x86_64']
    _srcs += files('validate_x86.c')
elif host_machine.cpu_family() in ['mips', 'mips64']
    _srcs += files('validate_mips.c')
elif host_machine.cpu_family() == 'arm'
    _srcs += files('validate_arm.c')
elif host_machine.cpu_family() == 'aarch64'
    _srcs += files('validate_arm64.c')
elif host_machine.cpu_family() in ['ppc', 'ppc64']
    _srcs += files('validate_power.c')
endif

if host_machine.system() == 'linux'
    _srcs += files('validate_perf.c')
    _deps += threads_dep
endif

_val = executable(
    'validate',
    _srcs,
    c_args: '-D_GNU_SOURCE',
    dependencies: _deps,
)
test('validate', _val)
