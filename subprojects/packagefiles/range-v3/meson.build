project(
  'range-v3',
  'cpp',
  version: '0.12.0',
  meson_version: '>=0.59.0',
  license: 'BSL-1.0 and NCSA and MIT and Stepanov McJones Elements of Programming and SGI STL',
)

if meson.get_compiler('cpp').get_argument_syntax() == 'msvc'
  add_project_arguments(
    '/permissive-',
    '-fno-delayed-template-parsing',
    language: 'cpp',
  )
endif

range_inc = include_directories('include')

range_dep = declare_dependency(
  include_directories: range_inc,
)
meson.override_dependency('range-v3', range_dep)

if get_option('tests').disable_auto_if(meson.is_subproject()).allowed()
  subdir('test')
endif
