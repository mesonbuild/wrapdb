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
libgetopt = static_library(
  'getopt',
  'getopt.c',
  'getopt1.c',
  include_directories: main_inc,
  dependencies: intl_dep,
)
