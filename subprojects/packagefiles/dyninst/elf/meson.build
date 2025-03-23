if host_machine.system() not in ['linux', 'freebsd']
  subdir_done()
endif

args = ['-DDYNELF_LIB']

install_headers('h/Elf_X.h')

iface_deps = [common_dep, libelf_dep]
dynElf_lib = library(
  'dynElf',
  'src/Elf_X.C',
  gnu_symbol_visibility: 'inlineshidden',
  override_options: ['b_ndebug=false'],
  include_directories: include_directories(
    '..',
    'src',
    'h',
    # Comes through hacky CMake target trickery
    '../common/src',
  ),
  dependencies: [iface_deps, boost_dep],
  version: meson.project_version(),
  soversion: dyninst_soversion,
  install: true,
)
dynelf_dep = declare_dependency(
  link_with: dynElf_lib,
  include_directories: include_directories('h'),
  dependencies: iface_deps,
)
all_deps += dynelf_dep
