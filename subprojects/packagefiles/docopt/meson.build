project('docopt.cpp', 'cpp',
        version: '0.6.3',
        license: 'Boost',
        meson_version: '>=0.55.0',
        default_options: 'cpp_std=c++11')

doclib = library('docopt', 'docopt.cpp')
executable('docopt_example', 'examples/naval_fate.cpp', link_with: doclib)
docopt_dep = declare_dependency(include_directories: '.',
    link_with: doclib)
meson.override_dependency('docopt', docopt_dep)
