srcs = files('pfmlib_common.c')

if host_machine.system() == 'linux'
  srcs += files(
    'pfmlib_perf_event.c',
    'pfmlib_perf_event_pmu.c',
    'pfmlib_perf_event_raw.c',
  )
endif

args = ['-D_REENTRANT']

if host_machine.cpu_family() == 'ia64'
  args += ['-DCONFIG_PFMLIB_ARCH_IA64']

elif host_machine.cpu_family() in ['x86', 'x86_64']
  if host_machine.system() == 'linux'
    srcs += files(
      'pfmlib_amd64_perf_event.c',
      'pfmlib_intel_netburst_perf_event.c',
      'pfmlib_intel_snbep_unc_perf_event.c',
      'pfmlib_intel_x86_perf_event.c',
    )
  endif

  srcs += files(
    'pfmlib_amd64.c',
    'pfmlib_amd64_fam10h.c',
    'pfmlib_amd64_fam11h.c',
    'pfmlib_amd64_fam12h.c',
    'pfmlib_amd64_fam14h.c',
    'pfmlib_amd64_fam15h.c',
    'pfmlib_amd64_fam16h.c',
    'pfmlib_amd64_fam17h.c',
    'pfmlib_amd64_fam19h.c',
    'pfmlib_amd64_fam19h_l3.c',
    'pfmlib_amd64_k7.c',
    'pfmlib_amd64_k8.c',
    'pfmlib_amd64_rapl.c',
    'pfmlib_intel_atom.c',
    'pfmlib_intel_bdw.c',
    'pfmlib_intel_bdx_unc_cbo.c',
    'pfmlib_intel_bdx_unc_ha.c',
    'pfmlib_intel_bdx_unc_imc.c',
    'pfmlib_intel_bdx_unc_irp.c',
    'pfmlib_intel_bdx_unc_pcu.c',
    'pfmlib_intel_bdx_unc_qpi.c',
    'pfmlib_intel_bdx_unc_r2pcie.c',
    'pfmlib_intel_bdx_unc_r3qpi.c',
    'pfmlib_intel_bdx_unc_sbo.c',
    'pfmlib_intel_bdx_unc_ubo.c',
    'pfmlib_intel_core.c',
    'pfmlib_intel_glm.c',
    'pfmlib_intel_hsw.c',
    'pfmlib_intel_hswep_unc_cbo.c',
    'pfmlib_intel_hswep_unc_ha.c',
    'pfmlib_intel_hswep_unc_imc.c',
    'pfmlib_intel_hswep_unc_irp.c',
    'pfmlib_intel_hswep_unc_pcu.c',
    'pfmlib_intel_hswep_unc_qpi.c',
    'pfmlib_intel_hswep_unc_r2pcie.c',
    'pfmlib_intel_hswep_unc_r3qpi.c',
    'pfmlib_intel_hswep_unc_sbo.c',
    'pfmlib_intel_hswep_unc_ubo.c',
    'pfmlib_intel_icl.c',
    'pfmlib_intel_ivb.c',
    'pfmlib_intel_ivb_unc.c',
    'pfmlib_intel_ivbep_unc_cbo.c',
    'pfmlib_intel_ivbep_unc_ha.c',
    'pfmlib_intel_ivbep_unc_imc.c',
    'pfmlib_intel_ivbep_unc_irp.c',
    'pfmlib_intel_ivbep_unc_pcu.c',
    'pfmlib_intel_ivbep_unc_qpi.c',
    'pfmlib_intel_ivbep_unc_r2pcie.c',
    'pfmlib_intel_ivbep_unc_r3qpi.c',
    'pfmlib_intel_ivbep_unc_ubo.c',
    'pfmlib_intel_knc.c',
    'pfmlib_intel_knl.c',
    'pfmlib_intel_knl_unc_cha.c',
    'pfmlib_intel_knl_unc_edc.c',
    'pfmlib_intel_knl_unc_imc.c',
    'pfmlib_intel_knl_unc_m2pcie.c',
    'pfmlib_intel_netburst.c',
    'pfmlib_intel_nhm.c',
    'pfmlib_intel_nhm_unc.c',
    'pfmlib_intel_rapl.c',
    'pfmlib_intel_skl.c',
    'pfmlib_intel_skx_unc_cha.c',
    'pfmlib_intel_skx_unc_iio.c',
    'pfmlib_intel_skx_unc_imc.c',
    'pfmlib_intel_skx_unc_irp.c',
    'pfmlib_intel_skx_unc_m2m.c',
    'pfmlib_intel_skx_unc_m3upi.c',
    'pfmlib_intel_skx_unc_pcu.c',
    'pfmlib_intel_skx_unc_ubo.c',
    'pfmlib_intel_skx_unc_upi.c',
    'pfmlib_intel_slm.c',
    'pfmlib_intel_snb.c',
    'pfmlib_intel_snb_unc.c',
    'pfmlib_intel_snbep_unc.c',
    'pfmlib_intel_snbep_unc_cbo.c',
    'pfmlib_intel_snbep_unc_ha.c',
    'pfmlib_intel_snbep_unc_imc.c',
    'pfmlib_intel_snbep_unc_pcu.c',
    'pfmlib_intel_snbep_unc_qpi.c',
    'pfmlib_intel_snbep_unc_r2pcie.c',
    'pfmlib_intel_snbep_unc_r3qpi.c',
    'pfmlib_intel_snbep_unc_ubo.c',
    'pfmlib_intel_spr.c',
    'pfmlib_intel_tmt.c',
    'pfmlib_intel_wsm.c',
    'pfmlib_intel_x86.c',
    'pfmlib_intel_x86_arch.c',
  )
  args += ['-DCONFIG_PFMLIB_ARCH_X86']

  if host_machine.cpu_family() == 'x86'
    srcs += files('pfmlib_intel_coreduo.c', 'pfmlib_intel_p6.c')
    args += ['-DCONFIG_PFMLIB_ARCH_I386']
  elif host_machine.cpu_family() == 'x86_64'
    args += ['-DCONFIG_PFMLIB_ARCH_X86_64']
  endif

elif host_machine.cpu_family() in ['ppc', 'ppc64']
  if host_machine.system() == 'linux'
    srcs += files('pfmlib_powerpc_perf_event.c')
  endif

  srcs += files(
    'pfmlib_power10.c',
    'pfmlib_power4.c',
    'pfmlib_power5.c',
    'pfmlib_power6.c',
    'pfmlib_power7.c',
    'pfmlib_power8.c',
    'pfmlib_power9.c',
    'pfmlib_powerpc.c',
    'pfmlib_powerpc_nest.c',
    'pfmlib_ppc970.c',
    'pfmlib_torrent.c',
  )
  args += ['-DCONFIG_PFMLIB_ARCH_POWERPC']

elif host_machine.cpu_family() == 's390x'
  if host_machine.system() == 'linux'
    srcs += files('pfmlib_s390x_perf_event.c')
  endif

  srcs += files('pfmlib_s390x_cpumf.c')
  args += ['-DCONFIG_PFMLIB_ARCH_S390X']

elif host_machine.cpu_family() in ['sparc', 'sparc64']
  if host_machine.system() == 'linux'
    srcs += files('pfmlib_sparc_perf_event.c')
  endif

  srcs += files(
    'pfmlib_sparc.c',
    'pfmlib_sparc_niagara.c',
    'pfmlib_sparc_ultra12.c',
    'pfmlib_sparc_ultra3.c',
    'pfmlib_sparc_ultra4.c',
  )
  args += ['-DCONFIG_PFMLIB_ARCH_SPARC']

elif host_machine.cpu_family() == 'arm'
  if host_machine.system() != 'linux'
    error('ARM is not supported except on Linux')
  endif

  srcs += files(
    'pfmlib_arm.c',
    'pfmlib_arm_armv6.c',
    'pfmlib_arm_armv7_pmuv1.c',
    'pfmlib_arm_armv8.c',
    'pfmlib_arm_armv9.c',
    'pfmlib_arm_perf_event.c',
    'pfmlib_kunpeng_unc_perf_event.c',
    'pfmlib_tx2_unc_perf_event.c',
  )
  args += ['-DCONFIG_PFMLIB_ARCH_ARM']

elif host_machine.cpu_family() == 'aarch64'
  if host_machine.system() != 'linux'
    error('ARM is not supported except on Linux')
  endif

  srcs += files(
    'pfmlib_arm.c',
    'pfmlib_arm_armv8.c',
    'pfmlib_arm_armv9.c',
    'pfmlib_arm_perf_event.c',
    'pfmlib_kunpeng_unc_perf_event.c',
    'pfmlib_tx2_unc_perf_event.c',
  )
  args += ['-DCONFIG_PFMLIB_ARCH_ARM64']

elif host_machine.cpu_family() in ['mips', 'mips64']
  if host_machine.system() == 'linux'
    srcs += files('pfmlib_mips_perf_event.c')
  endif

  srcs += files('pfmlib_mips.c', 'pfmlib_mips_74k.c')
  args += ['-DCONFIG_PFMLIB_ARCH_MIPS']
endif

libpfm_lib = library(
  'pfm',
  srcs,
  c_args: args,
  gnu_symbol_visibility: 'hidden',
  include_directories: inc,
  pic: true,
  install: true,
)
libpfm_dep = declare_dependency(
  link_with: libpfm_lib,
  include_directories: inc,
)
meson.override_dependency('libpfm', libpfm_dep)
