project('docopt.cpp', 'cpp',
        version: '0.6.3',
        license: 'Boost',
        default_options: 'cpp_std=c++11')

doclib = library('docopt', 'docopt.cpp')
executable('docopt_example', 'examples/naval_fate.cpp', link_with: doclib)
docopt_dep = declare_dependency(include_directories: include_directories('.'),
    link_with: doclib)
