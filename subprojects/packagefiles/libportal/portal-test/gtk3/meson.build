
gst_dep = dependency('gstreamer-audio-1.0')

resources = gnome.compile_resources(
  'resources',
  'portal-test.gresource.xml',
  c_name: '_portal_test',
)

src = [
  'main.c',
  'portal-test-app.h',
  'portal-test-app.c',
  'portal-test-win.h',
  'portal-test-win.c',
  resources,
]

portal_test_gtk3 = executable(
  'portal-test-gtk3',
  src,
  include_directories: [top_inc, libportal_inc],
  dependencies: [gst_dep, libportal_gtk3_dep],
  install: true,
)

install_data(
  'test.txt',
  install_dir: 'share/org.gnome.PortalTest.Gtk3',
)
install_data(
  'org.gnome.PortalTest.Gtk3.desktop',
  install_dir: 'share/applications',
)
install_data(
  'org.gnome.PortalTest.Gtk3.service',
  install_dir: 'share/dbus-1/services',
)

executable(
  'portal-linking-test-gtk3',
  ['portal-linking-test.c'],
  include_directories: [libportal_inc],
  dependencies: [libportal_gtk3_dep],
)

if meson.can_run_host_binaries()
  run_target(
    'portal-test-gtk3',
    command: portal_test_gtk3,
  )
endif
