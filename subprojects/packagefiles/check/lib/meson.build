sources = files('fpclassify.c', 'libcompat.c')

if not librt.found()
  sources += files(
    'clock_gettime.c',
    'timer_create.c',
    'timer_delete.c',
    'timer_settime.c',
  )
endif

foreach f : [
  'getline',
  'gettimeofday',
  'localtime_r',
  'malloc',
  'realloc',
  'snprintf',
  'strsignal',
  'alarm',
]
  if not cdata.has('HAVE_@0@'.format(f.to_upper())) and not cdata.has(
    'HAVE_DECL_@0@'.format(f.to_upper()),
  )
    message('Adding @0@.c to compat sources'.format(f))
    sources += files('@0@.c'.format(f))
  endif
endforeach

if not cdata.has('HAVE_DECL_STRDUP') and not cdata.has('HAVE__STRDUP')
  sources += files('strdup.c')
endif

compatlib = static_library(
  'compat',
  sources,
  c_args: '-DHAVE_CONFIG_H=1',
  pic: true,
  dependencies: librt,
  include_directories: confinc,
)

compatlib_dep = declare_dependency(
  include_directories: '.',
  link_with: compatlib,
)
