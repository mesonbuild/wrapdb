sources = files(
  'LXUtilities.cpp',
  'ParagraphLayout.cpp',
  'RunArrays.cpp',
  'playout.cpp',
  'plruns.cpp',
)

if host_machine.system() == 'windows'
  sources += windows.compile_resources(
    'layoutex.rc',
    include_directories: incdir
  )
endif

layoutex_name = '@0@lx@1@'.format(library_prefix, library_suffix)

layoutex_lib = library(
  layoutex_name,
  sources,
  include_directories: [incdir, include_directories('..')],
  c_args: '-DU_LAYOUTEX_IMPLEMENTATION',
  cpp_args: '-DU_LAYOUTEX_IMPLEMENTATION',
  link_with: [common_lib],
  version: U_ICU_VERSION,
  install: true,
)

layoutex_dep = declare_dependency(
  link_with: common_lib,
  compile_args: usage_args,
  include_directories: [incdir, include_directories('..')],
)

if meson.version().version_compare('>=0.54.0')
  meson.override_dependency('icu-lx', layoutex_lib)
endif

