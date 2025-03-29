project(
  'argtable3',
  'c',
  version: '3.2.2',
)

cc = meson.get_compiler('c')
libm = cc.find_library(
  'm',
  required: false,
)

argtable3_includes = include_directories(['src'])
argtable3_headers = files('src/argtable3.h')
argtable3_sources = files(
  'src/arg_cmd.c',
  'src/arg_date.c',
  'src/arg_dbl.c',
  'src/arg_dstr.c',
  'src/arg_end.c',
  'src/arg_file.c',
  'src/arg_getopt_long.c',
  'src/arg_hashtable.c',
  'src/arg_int.c',
  'src/arg_lit.c',
  'src/arg_rem.c',
  'src/arg_rex.c',
  'src/arg_str.c',
  'src/arg_utils.c',
  'src/argtable3.c',
)
argtable3 = library(
  'argtable3',
  argtable3_sources,
  dependencies: [libm],
  include_directories: argtable3_includes,
  version: meson.project_version(),
  install: true,
  vs_module_defs: 'argtable3.def',
)
install_headers(argtable3_headers)
argtable3_dep = declare_dependency(
  include_directories: argtable3_includes,
  link_with: argtable3,
)

