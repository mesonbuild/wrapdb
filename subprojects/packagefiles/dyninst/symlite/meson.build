if host_machine.system() not in ['linux', 'freebsd'] or not get_option(
  'lightweight_symtab',
)
  subdir_done()
endif

srcs = files('src/SymLite-elf.C')
args = ['-DSYMLITE_LIB']

install_headers('h/SymLite-elf.h')

iface_deps = [common_dep, dynelf_dep]
symLite_lib = library(
  'symLite',
  srcs,
  gnu_symbol_visibility: 'inlineshidden',
  override_options: ['b_ndebug=false'],
  include_directories: include_directories(
    '..',
    'src',
    'h',
    # Come through hacky CMake target trickery
    '../common/src',
    '../elf/src',
  ),
  c_args: args,
  cpp_args: args,
  dependencies: [iface_deps, boost_dep],
  version: meson.project_version(),
  soversion: dyninst_soversion,
  install: true,
)
symlite_dep = declare_dependency(
  link_with: symLite_lib,
  include_directories: include_directories('h'),
  dependencies: iface_deps,
)
all_deps += symlite_dep
