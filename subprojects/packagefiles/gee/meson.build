project('libgee', 'c', 'vala', version: '0.20.6')
api_version = '0.8'

glib_minimal_version = '2.36'
glib_dep = dependency('glib-2.0', version: '>='+glib_minimal_version)
gobject_dep = dependency('gobject-2.0', version: '>='+glib_minimal_version)
gio_dep = dependency('gio-2.0', version: '>='+glib_minimal_version)
gio_dep_vala = meson.get_compiler('vala').find_library('gio-2.0')
m_dep = meson.get_compiler('c').find_library('m', required : false)

add_project_arguments([
        '--hide-internal',
        '--target-glib='+glib_minimal_version,
    ],
    language: 'vala'
)

if not get_option('internal-asserts')
    add_project_arguments('--define=DISABLE_INTERNAL_ASSERTS', language: 'vala')
endif

if get_option('consistency-check')
    add_project_arguments('--define=CONSISTENCY_CHECKS', language: 'vala')
endif

subdir('utils')
subdir('gee')
