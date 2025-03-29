project(
  'docopt.cpp',
  'cpp',
  version: '0.6.3',
  license: 'Boost',
  default_options: 'cpp_std=c++11',
)

cpp = meson.get_compiler('cpp')
if cpp.get_argument_syntax() == 'msvc' and get_option('buildtype') != 'static'
  add_project_arguments(
    '-DDOCOPT_DLL',
    '-DDOCOPT_EXPORTS',
    language: 'cpp',
  )
endif

# bug with missing dllexport. fixed in next version.
if cpp.get_argument_syntax() == 'msvc'
  doclib = static_library('docopt', 'docopt.cpp')
else
  doclib = library('docopt', 'docopt.cpp')
endif

executable(
  'docopt_example',
  'examples/naval_fate.cpp',
  link_with: doclib,
)
docopt_dep = declare_dependency(
  include_directories: include_directories('.'),
  link_with: doclib,
)
