generated_files = []
version = '1.0.0'
gir_version = '1.0'

headers = [
  'portal.h',
  'portal-helpers.h',
  'account.h',
  'background.h',
  'camera.h',
  'dynamic-launcher.h',
  'email.h',
  'filechooser.h',
  'glib-backports.h',
  'inhibit.h',
  'inputcapture.h',
  'inputcapture-zone.h',
  'inputcapture-pointerbarrier.h',
  'location.h',
  'notification.h',
  'openuri.h',
  'parent.h',
  'print.h',
  'remote.h',
  'screenshot.h',
  'session.h',
  'settings.h',
  'spawn.h',
  'trash.h',
  'types.h',
  'updates.h',
  'wallpaper.h',
]

portal_enums = gnome.mkenums(
  'portal-enums',
  sources: headers,
  c_template: 'portal-enums.c.template',
  h_template: 'portal-enums.h.template',
  install_dir: join_paths(get_option('includedir'), 'libportal'),
  install_header: true,
)
generated_files += portal_enums

src = [
  'account.c',
  'background.c',
  'camera.c',
  'dynamic-launcher.c',
  'email.c',
  'filechooser.c',
  'inhibit.c',
  'inputcapture.c',
  'inputcapture-zone.c',
  'inputcapture-pointerbarrier.c',
  'location.c',
  'notification.c',
  'openuri.c',
  'parent.c',
  'portal.c',
  'print.c',
  'remote.c',
  'screenshot.c',
  'session.c',
  'settings.c',
  'spawn.c',
  'trash.c',
  'updates.c',
  'wallpaper.c',
  generated_files,
]

gio_dep = dependency(
  'gio-2.0',
  version: '>= 2.72',
)
gio_unix_dep = dependency('gio-unix-2.0')

install_headers(
  headers,
  subdir: 'libportal',
)

libportal = library(
  'portal',
  src,
  version: version,
  include_directories: [top_inc, libportal_inc],
  install: true,
  dependencies: [gio_dep, gio_unix_dep],
  gnu_symbol_visibility: 'hidden',
)

pkgconfig.generate(
  libportal,
  description: 'Portal API wrappers',
  name: 'libportal',
  requires: [gio_dep],
)

libportal_dep = declare_dependency(
  sources: generated_files,
  include_directories: top_inc,
  dependencies: [gio_dep, gio_unix_dep],
  link_with: libportal,
)

if introspection
  libportal_gir = gnome.generate_gir(
    libportal,
    sources: generated_files + headers + src,
    nsversion: gir_version,
    namespace: 'Xdp',
    symbol_prefix: 'xdp',
    identifier_prefix: 'Xdp',
    header: 'libportal/portal.h',
    link_with: libportal,
    includes: ['Gio-2.0'],
    install: true,
    export_packages: ['libportal'],
  )
  if vapi
    libportal_vapi = gnome.generate_vapi(
      'libportal',
      sources: [libportal_gir[0]],
      packages: ['gio-2.0'],
      install: true,
    )
  endif
endif

enabled_backends = []

########
# GTK3 #
########

gtk3_dep = dependency(
  'gtk+-3.0',
  required: get_option('backend-gtk3'),
)
if gtk3_dep.found()
  gtk3_headers = ['portal-gtk3.h']
  gtk3_sources = ['portal-gtk3.c']

  install_headers(
    gtk3_headers,
    subdir: 'libportal-gtk3',
  )

  libportal_gtk3 = library(
    'portal-gtk3',
    gtk3_sources,
    version: version,
    include_directories: [top_inc, libportal_inc],
    install: true,
    dependencies: [libportal_dep, gtk3_dep],
    gnu_symbol_visibility: 'hidden',
  )

  pkgconfig.generate(
    libportal_gtk3,
    description: 'Portal API wrappers (GTK3)',
    name: 'libportal-gtk3',
    requires: [gtk3_dep, libportal],
  )

  libportal_gtk3_dep = declare_dependency(
    dependencies: [libportal_dep, gtk3_dep],
    link_with: libportal_gtk3,
  )

  if introspection
    libportal_gtk3_gir = gnome.generate_gir(
      libportal_gtk3,
      sources: gtk3_sources + gtk3_headers,
      nsversion: gir_version,
      namespace: 'XdpGtk3',
      symbol_prefix: 'xdp',
      identifier_prefix: 'Xdp',
      header: 'libportal-gtk3/portal-gtk3.h',
      link_with: [libportal_gtk3],
      includes: [libportal_gir[0], 'Gtk-3.0'],
      install: true,
      export_packages: ['libportal-gtk3'],
    )

    if vapi
      libportal_gtk3_vapi = gnome.generate_vapi(
        'libportal-gtk3',
        sources: libportal_gtk3_gir[0],
        packages: ['gio-2.0', 'gtk+-3.0', libportal_vapi],
        gir_dirs: [meson.current_build_dir()],
        vapi_dirs: [meson.current_build_dir()],
        install: true,
      )
    endif
  endif
  enabled_backends += ['gtk3']
endif

########
# GTK4 #
########

gtk4_dep = dependency(
  'gtk4',
  required: get_option('backend-gtk4'),
)
if gtk4_dep.found()
  gtk4_headers = ['portal-gtk4.h']
  gtk4_sources = ['portal-gtk4.c']

  install_headers(
    gtk4_headers,
    subdir: 'libportal-gtk4',
  )

  libportal_gtk4 = library(
    'portal-gtk4',
    gtk4_sources,
    version: version,
    include_directories: [top_inc, libportal_inc],
    install: true,
    dependencies: [libportal_dep, gtk4_dep],
    gnu_symbol_visibility: 'hidden',
  )

  pkgconfig.generate(
    libportal_gtk4,
    description: 'Portal API wrappers (GTK4)',
    name: 'libportal-gtk4',
    requires: [gtk4_dep, libportal],
  )

  libportal_gtk4_dep = declare_dependency(
    dependencies: [libportal_dep, gtk4_dep],
    link_with: libportal_gtk4,
  )

  if introspection
    libportal_gtk4_gir = gnome.generate_gir(
      libportal_gtk4,
      sources: gtk4_sources + gtk4_headers,
      nsversion: gir_version,
      namespace: 'XdpGtk4',
      symbol_prefix: 'xdp',
      identifier_prefix: 'Xdp',
      header: 'libportal-gtk4/portal-gtk4.h',
      link_with: [libportal_gtk4],
      includes: [libportal_gir[0], 'Gtk-4.0'],
      install: true,
      export_packages: ['libportal-gtk4'],
    )

    if vapi
      libportal_gtk4_vapi = gnome.generate_vapi(
        'libportal-gtk4',
        sources: libportal_gtk4_gir[0],
        packages: ['gio-2.0', 'gtk4', libportal_vapi],
        gir_dirs: [meson.current_build_dir()],
        vapi_dirs: [meson.current_build_dir()],
        install: true,
      )
    endif
  endif
  enabled_backends += ['gtk4']
endif

########
# Qt 5 #
########

have_cpp = add_languages(
  'cpp',
  required: get_option('backend-qt5'),
  native: false,
)
qt5_dep = dependency(
  'qt5',
  modules: ['Core', 'Gui', 'X11Extras', 'Widgets'],
  required: get_option('backend-qt5'),
)

if have_cpp and qt5_dep.found()
  qt5_headers = ['portal-qt5.h']
  qt5_sources = ['portal-qt5.cpp']

  install_headers(
    qt5_headers,
    subdir: 'libportal-qt5',
  )

  libportal_qt5 = library(
    'portal-qt5',
    qt5_sources,
    version: version,
    include_directories: [top_inc, libportal_inc],
    cpp_args: '-std=c++11',
    install: true,
    dependencies: [libportal_dep, qt5_dep],
    gnu_symbol_visibility: 'hidden',
  )

  pkgconfig.generate(
    libportal_qt5,
    description: 'Portal API wrappers (Qt 5)',
    name: 'libportal-qt5',
    requires: [qt5_dep, libportal],
  )

  libportal_qt5_dep = declare_dependency(
    dependencies: [libportal_dep, qt5_dep],
    link_with: libportal_qt5,
  )
  enabled_backends += ['qt5']
endif

########
# Qt 6 #
########

if meson.version().version_compare('>= 0.63.0')
  have_cpp = add_languages(
    'cpp',
    required: get_option('backend-qt6'),
    native: false,
  )
  qt6_dep = dependency(
    'qt6',
    modules: ['Core', 'Gui', 'Widgets'],
    private_headers: true,
    required: get_option('backend-qt6'),
  )

  if have_cpp and qt6_dep.found()
    qt6_headers = ['portal-qt6.h']
    qt6_sources = ['portal-qt6.cpp']

    install_headers(
      qt6_headers,
      subdir: 'libportal-qt6',
    )

    libportal_qt6 = library(
      'portal-qt6',
      qt6_sources,
      version: version,
      include_directories: [top_inc, libportal_inc],
      cpp_args: '-std=c++17',
      install: true,
      dependencies: [libportal_dep, qt6_dep],
      gnu_symbol_visibility: 'hidden',
    )

    pkgconfig.generate(
      libportal_qt6,
      description: 'Portal API wrappers (Qt 6)',
      name: 'libportal-qt6',
      requires: [qt6_dep, libportal],
    )

    libportal_qt6_dep = declare_dependency(
      dependencies: [libportal_dep, qt6_dep],
      link_with: libportal_qt6,
    )
    enabled_backends += ['qt6']
  endif
endif

if meson.version().version_compare('>= 0.54.0')
  summary(
    {
      'enabled backends': enabled_backends,
    },
    section: 'Backends',
    list_sep: ',',
  )
endif

meson.override_dependency('libportal', libportal_dep)
meson.override_dependency('libportal-gtk3', libportal_gtk3_dep)
meson.override_dependency('libportal-gtk4', libportal_gtk4_dep)
meson.override_dependency('libportal-qt5', libportal_qt5_dep)
meson.override_dependency('libportal-qt6', libportal_qt6_dep)
