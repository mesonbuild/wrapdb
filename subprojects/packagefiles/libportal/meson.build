project(
  'libportal',
  'c',
  version: '0.9.1',
  license: 'LGPL-3.0-only',
  default_options: ['warning_level=2'],
  meson_version: '>= 1.9.0',
)

libportal_gtk3_dep = dependency(
  '',
  required: false,
)
libportal_gtk4_dep = dependency(
  '',
  required: false,
)
libportal_qt5_dep = dependency(
  '',
  required: false,
)
libportal_qt6_dep = dependency(
  '',
  required: false,
)

cc = meson.get_compiler('c')
cflags = [
  '-Wno-unused-parameter',
  '-Wno-missing-field-initializers',
]
add_project_arguments(
  cc.get_supported_arguments(cflags),
  language: 'c',
)

gnome = import('gnome')
pkgconfig = import('pkgconfig')

qt5 = import('qt5')

if get_option('backend-qt6').enabled() and meson.version().version_compare(
  '< 0.59.0',
)
  error('qt6 backend requires meson 0.59.0 or newer')
endif

if meson.version().version_compare('>= 0.59.0')
  qt6 = import('qt6')
endif

conf = configuration_data()
conf.set_quoted('G_LOG_DOMAIN', 'libportal')
conf.set_quoted('PACKAGE_NAME', 'libportal')
conf.set_quoted(
  'PKGDATADIR',
  join_paths(get_option('prefix'), get_option('datadir'), 'libportal'),
)
conf.set_quoted(
  'APPDATADIR',
  join_paths(get_option('prefix'), get_option('datadir'), 'org.gnome.PortalTest'),
)

if cc.has_argument('-fvisibility=hidden')
  conf.set('XDP_PUBLIC', '__attribute__((visibility("default"))) extern')
endif

check_headers = ['sys/vfs.h']

foreach header : check_headers
  macro = 'HAVE_' + header.underscorify().to_upper()
  conf.set(macro, cc.has_header(header) ? 1 : false)
endforeach

configure_file(
  output: 'config.h',
  configuration: conf,
)

introspection = get_option('introspection')
vapi = get_option('vapi')

top_inc = include_directories('.')
libportal_inc = include_directories('libportal')

subdir('libportal')

if get_option('portal-tests')
  subdir('portal-test')
endif

if get_option('tests')
  subdir('tests')
endif

if get_option('docs')
  subdir('doc')
endif
