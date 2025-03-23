project(
  'yaml-0.1',
  'c',
  license: 'MIT',
  meson_version: '>=0.49.2',
  version: '0.2.5',
)

pkg = import('pkgconfig')

add_project_arguments(
  '-DHAVE_CONFIG_H=1',
  language: 'c',
)
if get_option('default_library') == 'static'
  add_project_arguments(
    '-DYAML_DECLARE_STATIC=1',
    language: 'c',
  )
elif get_option('default_library') == 'shared'
  add_project_arguments(
    '-DYAML_DECLARE_EXPORT=1',
    language: 'c',
  )
endif

yaml_version = meson.project_version()
yaml_major_version = yaml_version.split('.')[0]
yaml_minor_version = yaml_version.split('.')[1]
yaml_patch_version = yaml_version.split('.')[2]
cdata = configuration_data(
  {
    'YAML_VERSION_MAJOR' : yaml_major_version,
    'YAML_VERSION_MINOR' : yaml_minor_version,
    'YAML_VERSION_PATCH' : yaml_patch_version,
  },
)
cdata.set_quoted('YAML_VERSION_STRING', meson.project_version())

config_h = configure_file(
  output: 'config.h',
  configuration: cdata,
)

inc = include_directories('include')

# this cannot avoid breaking the use of -lyaml due to strange libtool magic, but everything else works
yaml_lib = library(
  'yaml-0',
  'src/api.c',
  'src/dumper.c',
  'src/emitter.c',
  'src/loader.c',
  'src/parser.c',
  'src/reader.c',
  'src/scanner.c',
  'src/writer.c',
  version: '2.0.9',  # upstream specifies this in configure.ac
  include_directories: inc,
  install: true,
)

install_headers('include/yaml.h')

pkg.generate(
  yaml_lib,
  name: 'LibYAML',
  description: 'Library to parse and emit YAML',
  filebase: 'yaml-0.1',
)

yaml_dep = declare_dependency(
  link_with: yaml_lib,
  include_directories: inc,
)

subdir('tests')
