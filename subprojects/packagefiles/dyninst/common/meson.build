srcs = files(
  'src/AST.C',
  'src/Annotatable.C',
  'src/Buffer.C',
  'src/DOT.C',
  'src/Edge.C',
  'src/Graph.C',
  'src/MachSyscall.C',
  'src/MappedFile.C',
  'src/Node.C',
  'src/Timer.C',
  'src/VariableLocation.C',
  'src/addrtranslate.C',
  'src/arch-aarch64.C',
  'src/arch-power.C',
  'src/arch-x86.C',
  'src/concurrent.C',
  'src/debug_common.C',
  'src/dyn_regs.C',
  'src/lprintf.C',
  'src/pathName.C',
  'src/pfq-rwlock.C',
  'src/sha1.C',
  'src/stats.C',
  'src/util.C',
)
args = []

if host_machine.system() in ['linux', 'freebsd']
  srcs += files(
    'src/addrtranslate-sysv.C',
    'src/symbolDemangle.c',
    'src/symbolDemangleWithCache.C',
  )
endif

if host_machine.system() == 'freebsd'
  srcs += files('src/addrtranslate-freebsd.C', 'src/freebsdKludges.C')
elif host_machine.system() == 'linux'
  srcs += files(
    'src/addrtranslate-auxv.C',
    'src/addrtranslate-linux.C',
    'src/linuxKludges.C',
    'src/parseauxv.C',
  )
elif host_machine.system() == 'windows'
  srcs += files('src/addrtranslate-win.C', 'src/ntKludges.C')
  args += ['-DWIN32', '-D_WIN32_WINNT=0x500']
endif

args += ['-DCOMMON_LIB']

subdir('h')

iface_deps = [boost_dep, tbb_dep]
common_lib = library(
  'common',
  # This file must be listed first to dodge an initialization order bug.
  # See https://github.com/dyninst/dyninst/issues/1730
  'src/registers/MachRegister.C',
  srcs,
  gnu_symbol_visibility: 'inlineshidden',
  override_options: ['b_ndebug=false'],
  include_directories: include_directories('..', 'src', 'h'),
  c_args: args,
  cpp_args: args,
  dependencies: [
    iface_deps,
    libiberty_dep,
    openmp_dep,
    valgrind_dep,
    threads_dep,
  ],
  version: meson.project_version(),
  soversion: dyninst_soversion,
  install: true,
)
common_dep = declare_dependency(
  link_with: common_lib,
  include_directories: include_directories('h'),
  dependencies: iface_deps,
)
all_deps += common_dep
