sources = [
  'src/init.c',
  'src/x86/isa.c',
  'src/x86/x86_init.c',
  'src/x86/vendor.c',
  'src/api.c',
  'deps/clog/src/clog.c',
]

if host_machine.system() == 'linux'
  sources += 'src/x86/linux/init.c'
elif host_machine.system() == 'windows'
  sources += 'src/x86/windows/init.c'
elif host_machine.system() == 'darwin'
  sources += 'src/x86/mach/x86_mach_init.c'
else
  error('Unsupported host system: ' + host_machine.system())
endif

libcpuinfo = static_library(
  'cpuinfo',
  sources,
  include_directories: ['include', 'src', 'deps/clog/include'],
)

cpuinfo_dep = declare_dependency(
  include_directories: ['include'],
  link_with: libcpuinfo,
)
