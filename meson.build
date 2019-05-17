project('json-c', 'c',
  version: '0.13.1',
  license: 'MIT',
  meson_version: '>=0.37',
  default_options: ['c_std=gnu99'],
)

cc = meson.get_compiler('c')

add_project_arguments('-D_GNU_SOURCE', language: 'c')
if cc.has_argument('-Wno-unused')
  add_project_arguments('-Wno-unused', language: 'c')
endif

threads = dependency('threads', required: false)
math = cc.find_library('m', required: false)

subdir('config')
inc = include_directories('config')

json_config = configuration_data()
if conf.has('HAVE_INTTYPES_H')
  json_config.set10('JSON_C_HAVE_INTTYPES_H', true)
endif
json_config_h = configure_file(
  configuration: json_config,
  output: 'json_config.h',
)

public_headers = [
  json_config_h,
  'arraylist.h',
  'debug.h',
  'json_c_version.h',
  'json_inttypes.h',
  'json_object.h',
  'json_pointer.h',
  'json_tokener.h',
  'json_util.h',
  'linkhash.h',
  'printbuf.h',
]

sources = [
  'arraylist.c',
  'debug.c',
  'json_c_version.c',
  'json_object.c',
  'json_object_iterator.c',
  'json_pointer.c',
  'json_tokener.c',
  'json_util.c',
  'json_visit.c',
  'linkhash.c',
  'printbuf.c',
  'random_seed.c',
  'strerror_override.c',
]

libjson_c = library(meson.project_name(), json_config_h, config_h, sources,
  include_directories: inc,
  install: true,
)

json_c = declare_dependency(
  link_with: libjson_c,
  include_directories: include_directories('.'),
  dependencies: [math, threads],
  sources: json_config_h,
)

header_subdir = 'json-c'
install_headers(public_headers, subdir: header_subdir)

pkgconfig = import('pkgconfig')
pkgconfig.generate(
  description: 'A JSON implementation in C',
  libraries: libjson_c,
  version: meson.project_version(),
  filebase: meson.project_name(),
  name: meson.project_name(),
  subdirs: header_subdir,
)
