project(
    'taocpp-json',
    'cpp',
    version: '1.0.0-beta.14',
    license: 'MIT',
    default_options: [
        'cpp_std=c++17',
    ]
)

pegtl_dep = dependency('pegtl')

taocpp_json_inc = include_directories('include')
taocpp_json_dep = declare_dependency(include_directories: [taocpp_json_inc], dependencies: [pegtl_dep])

is_subproject = meson.is_subproject()

if get_option('tests').disable_auto_if(is_subproject).allowed()
  subdir('src/test/json')
endif

if get_option('examples').disable_auto_if(is_subproject).allowed()
  subdir('src/example/json')
endif

if get_option('perfs').disable_auto_if(is_subproject).allowed()
  subdir('src/perf/json')
endif
