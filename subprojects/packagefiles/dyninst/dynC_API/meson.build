if get_option('lightweight_symtab')
  message('-Dlightweight_symtab=true; dynC_API not built')
  subdir_done()
endif

srcs = files(
  'src/dynC.C',
  'src/dynC.tab.C',
  'src/lex.dynC.C',
  'src/snippetGen.C',
)

args = ['-DDYNC_EXPORTS']
if host_machine.system() == 'windows'
  args += ['-DYY_NO_UNISTD_H']
endif

install_headers('h/dynC.h', 'h/snippetGen.h')

iface_deps = [common_dep, dyninstapi_dep, symtabapi_dep]
dynC_lib = library(
  'dynC_API',
  srcs,
  gnu_symbol_visibility: 'inlineshidden',
  override_options: ['b_ndebug=false'],
  include_directories: include_directories(
    '..',
    'src',
    'h',
    # Comes through hacky CMake target trickery
    '../common/src',
    '../dyninstAPI/src',
    '../symtabAPI/src',
  ),
  c_args: args,
  cpp_args: args,
  dependencies: [iface_deps],
  version: meson.project_version(),
  soversion: dyninst_soversion,
  install: true,
)
dync_dep = declare_dependency(
  link_with: dynC_lib,
  include_directories: include_directories('h'),
  dependencies: iface_deps,
)
all_deps += dync_dep
