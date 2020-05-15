sources = files('libcompat.c', 'fpclassify.c')

if not librt.found()
  sources += files(
      'clock_gettime.c',
      'timer_create.c',
      'timer_delete.c',
      'timer_settime.c',
  )
endif

foreach function : [
        'getline',
        'gettimeofday',
        'localtime_r',
        'malloc',
        'realloc',
        'snprintf',
        'strsignal',
        'alarm',
    ]
  if (not cdata.has('HAVE_@0@'.format(function.to_upper()))
      and not cdata.has('HAVE_DECL_@0@'.format(function.to_upper())))
    message('Adding @0@.c to compat sources'.format(function))
    sources += files('@0@.c'.format(function))
  endif
endforeach

if not cdata.has('HAVE_DECL_STRDUP') and not cdata.has('HAVE__STRDUP')
  sources += files('strdup.c')
endif

compatlib = static_library('compat',
  sources,
  c_args: '-DHAVE_CONFIG_H=1',
  dependencies : librt,
  include_directories : confinc,
)

compatlib_dep = declare_dependency(
  include_directories : include_directories('.'),
  link_with : compatlib,
)
