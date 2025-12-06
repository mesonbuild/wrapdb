fs = import('fs')
sources = fs.read('sources.txt').split()

if host_machine.system() == 'windows'
  sources += windows.compile_resources(
    'layoutex.rc',
    include_directories: incdir,
  )
endif

layoutex_name = '@0@lx@1@'.format(library_prefix, library_suffix)

layoutex_lib = library(
  layoutex_name,
  sources,
  c_args: '-DU_LAYOUTEX_IMPLEMENTATION',
  cpp_args: '-DU_LAYOUTEX_IMPLEMENTATION',
  dependencies: icuuc_dep,
  version: U_ICU_VERSION,
  install: true,
)

layoutex_dep = declare_dependency(
  link_with: layoutex_lib,
  dependencies: icuuc_dep,
)
meson.override_dependency('icu-lx', layoutex_lib)

pkg.generate(
  layoutex_lib,
  name: 'icu-lx',
  description: '@0@: Paragraph Layout library @1@'.format(
    PACKAGE_ICU_DESCRIPTION,
    '',
  ),
  url: PACKAGE_ICU_URL,
)
