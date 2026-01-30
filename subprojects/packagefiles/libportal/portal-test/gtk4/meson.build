
if not introspection
  error('The GTK4 test portal requires introspection')
endif

gst_dep = dependency('gstreamer-audio-1.0')

package_name = 'portal-test-gtk4'
pkgdatadir = get_option('datadir') / package_name

data_resouces = gnome.compile_resources(
  'org.gnome.PortalTest.Gtk4.data',
  'org.gnome.PortalTest.Gtk4.data.gresource.xml',
  gresource_bundle: true,
  install: true,
  install_dir: pkgdatadir,
)

js_resouces = gnome.compile_resources(
  'org.gnome.PortalTest.Gtk4.src',
  'org.gnome.PortalTest.Gtk4.src.gresource.xml',
  gresource_bundle: true,
  install: true,
  install_dir: pkgdatadir,
)

bin_conf = configuration_data()
bin_conf.set('GJS', find_program('gjs').full_path())
bin_conf.set('PACKAGE_NAME', package_name)
bin_conf.set('PACKAGE_VERSION', '1.0.0')
bin_conf.set('prefix', get_option('prefix'))
bin_conf.set('libdir', get_option('prefix') / get_option('libdir'))
bin_conf.set('datadir', get_option('prefix') / get_option('datadir'))

portal_test_gtk4 = configure_file(
  input: 'org.gnome.PortalTest.Gtk4.in',
  output: 'org.gnome.PortalTest.Gtk4',
  configuration: bin_conf,
)
install_data(
  portal_test_gtk4,
  install_mode: 'rwxr-xr-x',
  install_dir: get_option('bindir'),
)
install_data(
  'test.txt',
  install_dir: 'share/org.gnome.PortalTest.Gtk4',
)
install_data(
  'org.gnome.PortalTest.Gtk4.desktop',
  install_dir: 'share/applications',
)
install_data(
  'org.gnome.PortalTest.Gtk4.service',
  install_dir: 'share/dbus-1/services',
)

executable(
  'portal-linking-test-gtk4',
  ['portal-linking-test.c'],
  include_directories: [libportal_inc],
  dependencies: [libportal_gtk4_dep],
)
