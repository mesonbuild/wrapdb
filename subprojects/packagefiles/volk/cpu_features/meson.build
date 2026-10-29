cpu_features_args = ['-DSTACK_LINE_READER_BUFFER_SIZE=1024']
cpu_features_deps = []
if host_machine.system() == 'darwin'
  cpu_features_args += '-DHAVE_SYSCTLBYNAME'
endif

cpu_features_sources = files(
  'src/filesystem.c',
  'src/impl_aarch64_linux_or_android.c',
  'src/impl_aarch64_macos_or_iphone.c',
  'src/impl_aarch64_windows.c',
  'src/impl_arm_linux_or_android.c',
  'src/impl_loongarch_linux.c',
  'src/impl_mips_linux_or_android.c',
  'src/impl_ppc_linux.c',
  'src/impl_riscv_linux.c',
  'src/impl_s390x_linux.c',
  'src/impl_x86_freebsd.c',
  'src/impl_x86_linux_or_android.c',
  'src/impl_x86_macos.c',
  'src/impl_x86_windows.c',
  'src/stack_line_reader.c',
  'src/string_view.c',
)

if not cpu_is_x86 and host_machine.system() != 'windows'
  cpu_features_sources += files('src/hwcaps.c')
  if cc.has_header_symbol('sys/auxv.h', 'getauxval')
    cpu_features_args += '-DHAVE_STRONG_GETAUXVAL'
  elif cc.has_header('dlfcn.h')
    cpu_features_args += '-DHAVE_DLFCN_H'
    cpu_features_deps += dependency(
      'dl',
      required: false,
    )
  endif
endif

cpu_features_lib = static_library(
  'cpu_features',
  cpu_features_sources,
  c_args: cpu_features_args,
  include_directories: include_directories('include', 'include/internal'),
  dependencies: cpu_features_deps,
)

volk_incs += include_directories('include')
