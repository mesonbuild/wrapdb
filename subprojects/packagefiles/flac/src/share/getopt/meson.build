if meson.version().version_compare('>= 0.59')
  intl_dep = dependency(
    'intl',
    required: false,
  )
else
  intl_dep = dependency(
    '',
    required: false,
  )
endif

# fix problem with conflicting getenv() declaration in getopt.c
# when using clang-cl
getopt_c_args = []
if host_machine.system() == 'windows'
  getopt_c_args += '-Dgetenv=getenv'
endif

libgetopt = static_library(
  'getopt',
  'getopt.c',
  'getopt1.c',
  c_args: getopt_c_args,
  include_directories: main_inc,
  dependencies: intl_dep,
)
