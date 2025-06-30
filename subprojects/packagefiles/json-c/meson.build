project(
  'json-c',
  'c',
  version: '0.18',
  license: 'MIT',
  meson_version: '>=0.49',
  default_options: [
    meson.version().version_compare('>=1.3.0') ? 'c_std=gnu99,c99' : 'c_std=gnu99',
  ],
)

cc = meson.get_compiler('c')

if cc.get_argument_syntax() == 'msvc'
  add_project_arguments(
    '/D_CRT_SECURE_NO_WARNINGS',
    '/wd4996',
    language: 'c',
  )
else
  add_project_arguments(
    '-D_GNU_SOURCE',
    language: 'c',
  )
endif

if get_option('default_library') != 'static'
  add_project_arguments(
    '-DJSON_C_DLL',
    language: 'c',
  )
endif

add_project_arguments(
  cc.get_supported_arguments('-Wno-deprecated-declarations'),
  language: 'c',
)

subdir('config')
inc = include_directories('config')

json_config = configuration_data()
if conf.has('HAVE_INTTYPES_H')
  json_config.set('JSON_C_HAVE_INTTYPES_H', 1)
endif
json_config_h = configure_file(
  configuration: json_config,
  output: 'json_config.h',
)

jconf = configuration_data()
jconf.set('JSON_H_JSON_POINTER', '#include "json_pointer.h"')
jconf.set('JSON_H_JSON_PATCH', '#include "json_patch.h"')

json_h = configure_file(
  input: 'json.h.cmakein',
  output: 'json.h',
  format: 'cmake@',
  configuration: jconf,
)

public_headers = [
  json_config_h,
  json_h,
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

sources = files(
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
)

libjson_c = library(
  'json-c',
  sources,
  include_directories: inc,
  install: true,
  version: '5.4.0',
)

json_c_dep = declare_dependency(
  link_with: libjson_c,
  include_directories: include_directories('.'),
  sources: json_config_h,
)

install_headers(
  public_headers,
  subdir: 'json-c',
)

pkgconfig = import('pkgconfig')
pkgconfig.generate(
  libjson_c,
  description: 'A JSON implementation in C',
  version: meson.project_version(),
  filebase: meson.project_name(),
  name: meson.project_name(),
  subdirs: 'json-c',
)
