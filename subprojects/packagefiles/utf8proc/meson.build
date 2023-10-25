project('utf8proc', 'c',
    version : '2.9.0',
    license: 'MIT',
    default_options: 'c_std=c99',
)

pkg = import('pkgconfig')

if get_option('default_library') == 'static'
  add_project_arguments('-DUTF8PROC_STATIC', language: 'c')
endif

add_project_arguments('-DUTF8PROC_EXPORTS', language: 'c')

utf8proc_lib = library('utf8proc',
  'utf8proc.c',
  install: true,
  version: '3.0.0',
)

utf8proc_dep = declare_dependency(
  include_directories: include_directories('.'),
  link_with: utf8proc_lib
)

pkg.generate(
  utf8proc_lib,
  description: 'UTF8 processing',
  extra_cflags: '-DUTF8PROC_EXPORTS',
  name: 'libutf8proc',
)

install_headers('utf8proc.h')
