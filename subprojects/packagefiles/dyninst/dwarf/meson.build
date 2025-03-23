if host_machine.system() not in ['linux', 'freebsd']
  subdir_done()
endif

args = ['-DDYNDWARF_LIB']
srcs = files(
  'src/dwarfExprParser.C',
  'src/dwarfFrameParser.C',
  'src/dwarfHandle.C',
  'src/dwarfResult.C',
  'src/dwarf_subrange.cpp',
)

install_headers(
  'h/dwarfExprParser.h',
  'h/dwarfFrameParser.h',
  'h/dwarfHandle.h',
  'h/dwarfResult.h',
  'h/dwarf_unit_info.h',
)

iface_deps = [common_dep, dynelf_dep]
dynDwarf_lib = library(
  'dynDwarf',
  srcs,
  gnu_symbol_visibility: 'inlineshidden',
  override_options: ['b_ndebug=false'],
  include_directories: include_directories(
    '..',
    'src',
    'h',
    # Come through hacky CMake target tricks
    '../common/src',
    '../elf/src',
  ),
  c_args: args,
  cpp_args: args,
  dependencies: [iface_deps, libdw_dep],
  version: meson.project_version(),
  soversion: dyninst_soversion,
  install: true,
)
dyndwarf_dep = declare_dependency(
  link_with: dynDwarf_lib,
  include_directories: include_directories('h'),
  dependencies: iface_deps,
)
all_deps += dyndwarf_dep
