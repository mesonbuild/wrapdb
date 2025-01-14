project(
    'MPark.Patterns',
    'cpp',
    default_options: ['cpp_std=c++17'],
    license: 'BSL-1.0',
    version: '0.3.0',
    meson_version: '>=1.6.1',
)

install_subdir(
    'include',
    install_dir: get_option('includedir'),
    strip_directory: true,
)

mpark_patterns_dep = declare_dependency(
    include_directories: include_directories('include'),
)

if get_option('tests').enabled()
    subdir('test')
endif
