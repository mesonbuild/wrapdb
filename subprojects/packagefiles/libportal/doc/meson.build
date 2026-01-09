toml_data = configuration_data()
toml_data.set('VERSION', meson.project_version())

libportal_toml = configure_file(
  input: 'libportal.toml.in',
  output: 'libportal.toml',
  configuration: toml_data,
)

dependency(
  'gi-docgen',
  version: '>= 2021.1',
  fallback: ['gi-docgen', 'dummy_dep'],
  native: true,
  required: get_option('docs'),
)

gidocgen = find_program('gi-docgen')

docs_dir = get_option('datadir') / 'doc'

gidocgen_opts = [
  '--quiet',
  '--add-include-path=@0@'.format(meson.current_build_dir() / '../../libportal'),
  '--no-namespace-dir',
  '--content-dir=@0@'.format(meson.current_source_dir()),
]
if get_option('werror')
  gidocgen_opts += ['--fatal-warnings']
endif

custom_target(
  'libportal-doc',
  input: [libportal_toml, libportal_gir[0]],
  output: 'libportal-1',
  command: [
    gidocgen,
    'generate',
    gidocgen_opts,
    '--config=@INPUT0@',
    '--output-dir=@OUTPUT@',
    '@INPUT1@',
  ],
  build_by_default: true,
  install: true,
  install_dir: docs_dir,
)
