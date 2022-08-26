project('utf8proc', 'c',
    version : '2.7.0',
    license: 'MIT',
    default_options: ['c_std=c99']
)

if get_option('default_library') != 'static' and host_machine.system() == 'windows'
  add_project_arguments('-DUTF8PROC_EXPORTS', language: 'c')
endif

utf8proc_lib = library('utf8proc',
  'utf8proc.c',
)

utf8proc_dep = declare_dependency(
  include_directories: include_directories('.'),
  link_with: utf8proc_lib
)
