project('xla', 'cpp', default_options : ['default_library=shared'])

if not meson.is_subproject() 
  cc = meson.get_compiler('cpp')
endif

include = include_directories('.')

xla_dep = declare_dependency(
  include_directories : [include]
)
