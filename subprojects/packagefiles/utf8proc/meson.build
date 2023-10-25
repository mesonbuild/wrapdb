project('utf8proc', 'c',
    version : '2.9.0',
    license: 'MIT',
    default_options: 'c_std=c99',
)

if get_option('default_library') == 'static'
  add_project_arguments('-DUTF8PROC_STATIC', language: 'c')
endif

add_project_arguments('-DUTF8PROC_EXPORTS', language: 'c')

utf8proc_lib = library('utf8proc',
  'utf8proc.c',
)

utf8proc_dep = declare_dependency(
  include_directories: include_directories('.'),
  link_with: utf8proc_lib
)
