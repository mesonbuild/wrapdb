examples = [
  'dbus-service',
  'https-client-test',
  'https-server-test',
  'dbus-client',
  'dhcp-client',
  'dhcp6-client',
  'dhcp-server',
  'acd-client',
  'netconfig-test',
]

if get_option('examples')
  foreach example : examples
    exe = executable(
      example,
      '@0@.c'.format(example),
      include_directories: include_directories('..'),
      dependencies: libell_private_dep,
      install: false,
    )
  endforeach
endif

if get_option('glib') and get_option('examples')
  exe = executable(
    'glib-eventloop',
    'glib-eventloop.c',
    include_directories: include_directories('..'),
    dependencies: [libell_private_dep, glib_dep],
    install: false,
  )
endif

