project(
  'argtable3',
  'c',
  version: '3.3.1',
  license: 'BSD-3-Clause',
  meson_version: '>=0.56.0',
)

cc = meson.get_compiler('c')
if cc.links('#include <math.h>\nint main(){log(0);}')
  libm = []
else
  libm = cc.find_library('m')
endif

argtable3_inc = include_directories('src')
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

# Suppress -Wstringop-truncation for non-MSVC compilers.
# Release builds with _FORTIFY_SOURCE can trigger these warnings in arg_dstr.c.
# These warnings are currently considered benign. This is a temporary measure
# until arg_dstr.c is improved to prevent these warnings.
specific_c_args = cc.get_supported_arguments('-Wno-stringop-truncation')

argtable3_lib = library(
  'argtable3',
  argtable3_sources,
  dependencies: libm,
  include_directories: argtable3_inc,
  version: meson.project_version(),
  install: true,
  vs_module_defs: 'argtable3.def',
  c_args: specific_c_args,
)

install_headers(argtable3_headers)

argtable3_dep = declare_dependency(
  include_directories: argtable3_inc,
  link_with: argtable3_lib,
)

meson.override_dependency('argtable3', argtable3_dep)

pconf = import('pkgconfig')
pconf.generate(
  argtable3_lib,
  description: 'ANSI C command-line parsing library',
)

subdir('examples')
subdir('tests')
