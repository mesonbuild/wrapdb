sources = files('jbig.c', 'jbig_ar.c')
sources85 = files('jbig85.c', 'jbig_ar.c')

libjbig = library(
  'jbig',
  sources,
  vs_module_defs: '../jbig.def',
  install: true,
)
install_headers('jbig.h')
libjbig_dep = declare_dependency(
  include_directories: include_directories('.'),
  link_with: libjbig,
)
# meson.override_dependency('libjbig', libjbig_dep)

libjbig85 = library(
  'jbig85',
  sources85,
  vs_module_defs: '../jbig85.def',
  install: true,
)
install_headers('jbig85.h')
libjbig85_dep = declare_dependency(
  include_directories: include_directories('.'),
  link_with: libjbig85,
)
# meson.override_dependency('libjbig85', libjbig85_dep)
