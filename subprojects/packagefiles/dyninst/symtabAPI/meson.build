srcs = files(
  'src/AddrLookup.C',
  'src/Aggregate.C',
  'src/Collections.C',
  'src/ExceptionBlock.C',
  'src/Function.C',
  'src/LineInformation.C',
  'src/Module.C',
  'src/Object.C',
  'src/Region.C',
  'src/Statement.C',
  'src/Symbol.C',
  'src/Symtab-edit.C',
  'src/Symtab-lookup.C',
  'src/Symtab.C',
  'src/SymtabReader.C',
  'src/Type.C',
  'src/Variable.C',
  'src/annotations.C',
  'src/debug.C',
  'src/relocationEntry.C',
)
if host_machine.system() in ['linux', 'freebsd']
  srcs += files(
    'src/Archive-elf.C',
    'src/Archive.C',
    'src/LinkMap.C',
    'src/Object-elf.C',
    'src/dwarfWalker.C',
    'src/emitElf.C',
    'src/emitElfStatic.C',
    'src/parseDwarf.C',
  )

  if host_machine.cpu_family() in ['x86_64', 'x86']
    srcs += files('src/emitElfStatic-x86.C', 'src/relocationEntry-elf-x86.C')
  elif host_machine.cpu_family() == 'ppc64'
    srcs += files('src/emitElfStatic-ppc64.C', 'src/relocationEntry-elf-ppc64.C')
  elif host_machine.cpu_family() == 'aarch64'
    srcs += files(
      'src/emitElfStatic-aarch64.C',
      'src/relocationEntry-elf-aarch64.C',
    )
  else
    srcs += files('src/emitElfStatic-stub.C', 'src/relocationEntry-stub.C')
  endif

elif host_machine.system() == 'windows'
  srcs += files('src/Object-nt.C', 'src/emitWin.C', 'src/relocationEntry-stub.C')
endif

args = ['-DSYMTAB_LIB']

install_headers(
  'h/AddrLookup.h',
  'h/Aggregate.h',
  'h/Archive.h',
  'h/Collections.h',
  'h/ExceptionBlock.h',
  'h/Function.h',
  'h/LineInformation.h',
  'h/Module.h',
  'h/RangeLookup.h',
  'h/Region.h',
  'h/relocationEntry.h',
  'h/Statement.h',
  'h/StringTable.h',
  'h/Symbol.h',
  'h/Symtab.h',
  'h/SymtabReader.h',
  'h/symutil.h',
  'h/Type.h',
  'h/Variable.h',
)

iface_deps = [common_dep]
if host_machine.system() in ['linux', 'freebsd']
  iface_deps += [dynelf_dep, dyndwarf_dep, libelf_dep, libdw_dep]
endif

symtabAPI_lib = library(
  'symtabAPI',
  srcs,
  gnu_symbol_visibility: 'inlineshidden',
  override_options: ['b_ndebug=false'],
  include_directories: include_directories(
    '..',
    'src',
    'h',
    # Comes through hacky CMake target trickery
    '../common/src',
    '../elf/src',
    '../dwarf/src',
  ),
  c_args: args,
  cpp_args: args,
  dependencies: [iface_deps, boost_dep, openmp_dep],
  version: meson.project_version(),
  soversion: dyninst_soversion,
  install: true,
)
symtabapi_dep = declare_dependency(
  link_with: symtabAPI_lib,
  include_directories: include_directories('h'),
  dependencies: iface_deps,
)
all_deps += symtabapi_dep
