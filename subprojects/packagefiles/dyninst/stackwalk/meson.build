srcs = files(
  'src/frame.C',
  'src/framestepper.C',
  'src/libstate.C',
  'src/procstate.C',
  'src/steppergroup.C',
  'src/sw_pcontrol.C',
  'src/swk_errors.C',
  'src/symlookup.C',
  'src/symtab-swk.C',
  'src/walker.C',
)

if host_machine.cpu_family() in ['x86', 'x86_64']
  srcs += files('src/x86-swk.C', 'src/x86-wanderer.C')
endif

if host_machine.system() == 'freebsd'
  srcs += files('src/freebsd-swk.C')
elif host_machine.system() == 'windows'
  srcs += files('src/win-x86-swk.C')
endif

if host_machine.system() in ['linux', 'freebsd']
  srcs += files('src/linux-swk.C', 'src/linuxbsd-swk.C')
  if host_machine.cpu_family() == 'ppc64'
    srcs += files('src/linux-ppc-swk.C', 'src/ppc-swk.C')
  elif host_machine.cpu_family() == 'aarch64'
    srcs += files(
      'src/aarch64-swk.C',
      'src/dbginfo-stepper.C',
      'src/linux-aarch64-swk.C',
    )
  elif host_machine.cpu_family() in ['x86', 'x86_64']
    srcs += files(
      'src/dbginfo-stepper.C',
      'src/linux-x86-swk.C',
      'src/linuxbsd-x86-swk.C',
    )
    if host_machine.system() == 'freebsd'
      srcs += files('src/freebsd-x86-swk.C')
    endif
  endif
endif

args = ['-DSTACKWALKER_EXPORTS', force_frame_pointer_args]

if get_option('sw_analysis_stepper')
  args += ['-DUSE_PARSE_API']
  srcs += files('src/analysis_stepper.C', 'src/callchecker-IAPI.C')
else
  srcs += files('src/callchecker.C')
endif

install_headers(
  'h/basetypes.h',
  'h/frame.h',
  'h/framestepper.h',
  'h/local_var.h',
  'h/procstate.h',
  'h/steppergroup.h',
  'h/swk_errors.h',
  'h/symlookup.h',
  'h/walker.h',
)

iface_deps = [common_dep, instructionapi_dep, pcontrol_dep, boost_dep]
if host_machine.system() in ['linux', 'freebsd']
  iface_deps += [dyndwarf_dep, dynelf_dep]
endif
if get_option('lightweight_symtab')
  iface_deps += [symlite_dep]
else
  iface_deps += [symtabapi_dep]
endif
if get_option('sw_analysis_stepper')
  iface_deps += [parseapi_dep]
endif

stackwalk_lib = library(
  'stackwalk',
  srcs,
  gnu_symbol_visibility: 'inlineshidden',
  override_options: ['b_ndebug=false'],
  include_directories: include_directories(
    '..',
    'src',
    'h',
    # Comes through hacky CMake target trickery
    '../common/src',
    '../instructionAPI/src',
    '../proccontrol/src',
    (host_machine.system() in ['linux', 'freebsd'] ? [
      '../elf/src',
      '../dwarf/src',
    ] : []),
    (get_option('lightweight_symtab') ? ['../symlite/src'] : [
      '../symtabAPI/src',
    ]),
    # (get_option('sw_analysis_stepper') ? ['../parseAPI/src'] : []),
  ),
  c_args: args,
  cpp_args: args,
  dependencies: [iface_deps, libelf_dep],
  version: meson.project_version(),
  soversion: dyninst_soversion,
  install: true,
)
stackwalk_dep = declare_dependency(
  link_with: stackwalk_lib,
  include_directories: include_directories('h'),
  dependencies: iface_deps,
)
all_deps += stackwalk_dep
