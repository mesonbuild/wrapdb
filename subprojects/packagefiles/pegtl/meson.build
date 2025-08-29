project(
  'pegtl',
  'cpp',
  version: '3.2.8',
  license: 'MIT',
  meson_version: '>=1.2.0',
  default_options: {
    'cpp_std': 'c++17',
  },
)

pegtl_dep = declare_dependency(
  include_directories: include_directories('include'),
)

meson.override_dependency('pegtl', pegtl_dep)

is_subproject = meson.is_subproject()

if get_option('tests').disable_auto_if(is_subproject).allowed()
  subdir('src/test/pegtl')
endif

if get_option('examples').disable_auto_if(is_subproject).allowed()
  subdir('src/example/pegtl')
endif
