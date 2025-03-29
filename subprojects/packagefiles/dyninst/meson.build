project(
  'dyninst',
  'c',
  'cpp',
  version: '13.0.0',
  meson_version: '>=1.0.0',
  default_options: ['c_std=c11', 'cpp_std=c++11'],
)
dyninst_soversion = meson.project_version().split('.')
dyninst_soversion = '@0@.@1@'.format(dyninst_soversion[0], dyninst_soversion[1])

cpp_cc = meson.get_compiler('cpp')
if host_machine.system() == 'windows'
  error('This wrap does not support building for Windows')
elif host_machine.system() == 'linux'
  if not cpp_cc.has_header_symbol('features.h', '__GLIBC_PREREQ')
    error('Glibc not detected; this wrap is not supported on this libc')
  endif
  if not cpp_cc.has_header_symbol('sys/ptrace.h', '__ptrace_request')
    error('__ptrace_request not found; this wrap is not supported')
  endif
endif

add_project_arguments(
  '-Dcap_dynamic_heap',
  '-Dcap_liveness',
  '-Dcap_threads',
  language: ['c', 'cpp'],
)
if host_machine.cpu_family() == 'x86'
  add_project_arguments(
    '-Darch_x86',
    '-Dcap_fixpoint_gen',
    '-Dcap_noaddr_gen',
    '-Dcap_stripped_binaries',
    '-Dcap_tramp_liveness',
    '-Dcap_virtual_registers',
    '-Dcap_stack_mods',
    language: ['c', 'cpp'],
  )
  cap_stack_mods = true
elif host_machine.cpu_family() == 'x86_64'
  add_project_arguments(
    '-Darch_x86_64',
    '-Darch_64bit',
    '-Dcap_32_64',
    '-Dcap_fixpoint_gen',
    '-Dcap_noaddr_gen',
    '-Dcap_registers',
    '-Dcap_stripped_binaries',
    '-Dcap_tramp_liveness',
    '-Dcap_stack_mods',
    language: ['c', 'cpp'],
  )
  cap_stack_mods = true
elif host_machine.cpu_family() == 'ppc64'
  add_project_arguments(
    '-Darch_power',
    '-Darch_64bit',
    '-Dcap_32_64',
    '-Dcap_registers',
    '-Dcap_toc_64',
    language: ['c', 'cpp'],
  )
  cap_stack_mods = false
elif host_machine.cpu_family() == 'aarch64'
  add_project_arguments(
    '-Darch_aarch64',
    '-Darch_64bit',
    '-Dcap_registers',
    language: ['c', 'cpp'],
  )
  cap_stack_mods = false
else
  error(
    'Host architecture @0@ is not supported'.format(host_machine.cpu_family()),
  )
endif

if host_machine.system() == 'linux'
  add_project_arguments(
    '-Dos_linux',
    '-Dcap_async_events',
    '-Dcap_binary_rewriter',
    '-Dcap_dwarf',
    '-Dcap_mutatee_traps',
    '-Dcap_ptrace',
    '-Dbug_syscall_changepc_rewind',
    '-Dbug_force_terminate_failure',
    language: ['c', 'cpp'],
  )
  if host_machine.cpu_family() == 'x86'
    add_project_arguments(
      '-Di386_unknown_linux2_0',
      language: ['c', 'cpp'],
    )
  elif host_machine.cpu_family() == 'x86_64'
    add_project_arguments(
      '-Dx86_64_unknown_linux2_4',
      language: ['c', 'cpp'],
    )
  elif host_machine.cpu_family() == 'ppc64'
    add_project_arguments(
      '-Dppc64_linux',
      '-Dbug_registers_after_exit',
      language: ['c', 'cpp'],
    )
  elif host_machine.cpu_family() == 'aarch64'
    add_project_arguments(
      '-Daarch64_unknown_linux',
      language: ['c', 'cpp'],
    )
  endif
elif host_machine.system() == 'freebsd'
  add_project_arguments(
    '-Dos_freebsd',
    '-Dcap_binary_rewriter',
    '-Dcap_dwarf',
    '-Dcap_mutatee_traps',
    '-Dbug_freebsd_missing_sigstop',
    '-Dbug_freebsd_mt_suspend',
    '-Dbug_freebsd_change_pc',
    '-Dbug_phdrs_first_page',
    '-Dbug_syscall_changepc_rewind',
    language: ['c', 'cpp'],
  )
  if host_machine.cpu_family() == 'x86'
    add_project_arguments(
      '-Di386_unknown_freebsd7_0',
      language: ['c', 'cpp'],
    )
  elif host_machine.cpu_family() == 'x86_64'
    add_project_arguments(
      '-Damd64_unknown_freebsd7_0',
      language: ['c', 'cpp'],
    )
  endif
elif host_machine.system() == 'windows'
  add_project_arguments(
    '-Dos_windows',
    '-Dcap_mutatee_traps',
    '-Di386_unknown_nt4_0',
    language: ['c', 'cpp'],
  )
else
  error('Host OS @0@ is not supported'.format(host_machine.system()))
endif

if get_option('lightweight_symtab')
  add_project_arguments(
    '-DWITHOUT_SYMTAB_API',
    '-DWITH_SYMLITE',
    language: ['c', 'cpp'],
  )
else
  add_project_arguments(
    '-DWITH_SYMTAB_API',
    '-DWITHOUT_SYMLITE',
    language: ['c', 'cpp'],
  )
endif
if get_option('sw_analysis_stepper')
  add_project_arguments(
    '-DUSE_PARSE_API',
    language: ['c', 'cpp'],
  )
endif

force_frame_pointer_args = cpp_cc.get_supported_arguments(
  '-fno-omit-frame-pointer',
  '/Oy-',
)
if force_frame_pointer_args.length() == 0
  error(
    'Unable to find compiler argument to enforce frame pointers (equiv. -fno-omit-frame-pointer)',
  )
endif

threads_dep = dependency(
  'threads',
  required: host_machine.system() in ['linux', 'freebsd'],
)
boost_dep = dependency(
  'boost',
  version: '>=1.71.0',
  modules: [
    'atomic',
    'chrono',
    'date_time',
    'filesystem',
    'system',
    'thread',
    'timer',
  ],
)
tbb_dep = dependency(
  'tbb',
  'TBB',
  components: ['tbb'],
)
tbbmalloc_dep = dependency(
  'tbbmalloc',
  'TBB',
  components: ['tbb', 'tbbmalloc'],
)

libdw_dep = dependency(
  '',
  required: false,
)
libelf_dep = dependency(
  '',
  required: false,
)
debuginfod_dep = dependency(
  '',
  required: false,
)
libiberty_dep = dependency(
  '',
  required: false,
)
thread_db_dep = dependency(
  '',
  required: false,
)
valgrind_dep = dependency(
  '',
  required: false,
)
if host_machine.system() in ['linux', 'freebsd']
  libdw_dep = dependency(
    'libdw',
    version: '>=0.186',
  )
  libelf_dep = dependency(
    'libelf',
    version: '>=0.186',
  )
  debuginfod_dep = dependency(
    'libdebuginfod',
    version: '>=0.186',
    required: get_option('debuginfod'),
  )
  libiberty_dep = dependency(
    'LibIberty',
    cmake_module_path: meson.current_source_dir() / 'cmake/Modules',
  )
  thread_db_dep = cpp_cc.find_library(
    'thread_db',
    has_headers: ['thread_db.h'],
    required: false,
  )
  if thread_db_dep.found()
    add_project_arguments(
      '-Dcap_thread_db',
      language: ['c', 'cpp'],
    )
  endif
  if get_option('valgrind_annotations')
    valgrind_dep = dependency('valgrind')
    add_project_arguments(
      '-DENABLE_VG_ANNOTATIONS',
      language: ['c', 'cpp'],
    )
  endif
endif

openmp_dep = dependency(
  'openmp',
  required: get_option('openmp'),
)
dl_dep = dependency('dl')

version_h_in = files('cmake/dyninstversion.h.in')

all_deps = []

subdir('common')
subdir('elf')
subdir('dwarf')
subdir('symlite')
subdir('instructionAPI')
subdir('symtabAPI')
subdir('parseAPI')
subdir('proccontrol')
subdir('stackwalk')
subdir('patchAPI')
subdir('dyninstAPI')
subdir('dynC_API')
subdir('parseThat')
# FIXME: Omitted due to weird CMake logic that cannot be implemented in Meson.
# subdir('dyninstAPI_RT')

dyninst_dep = declare_dependency(
  dependencies: all_deps,
)
