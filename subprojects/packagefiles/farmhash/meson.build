project('farmhash', 'cpp', default_options : ['default_library=shared'])

if not meson.is_subproject() 
  cc = meson.get_compiler('cpp')
endif

add_project_arguments('-DFARMHASH_OPTIONAL_BUILTIN_EXPECT', language: 'cpp')

include = include_directories('src')

farmhash_sources = files(
  'src/farmhash.cc',
)

farmhash = library('farmhash',
  farmhash_sources,
  include_directories : [include],
  install : true,
  link_args : [],
)

farmhash_dep = declare_dependency(
  link_with : farmhash,
  include_directories : [include]
)
