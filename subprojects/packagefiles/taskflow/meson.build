project('taskflow', 'cpp',
    version: '3.4.0',
    license: 'MIT',
    default_options: [
      'cpp_std=c++17',
    ],
)

# Header-only library
taskflow_inc = include_directories('.')

taskflow_dep = declare_dependency(
    include_directories: taskflow_inc,
    dependencies: [
        dependency('threads'),
    ]
)

# Installations

# Copy all header files to ${prefix}/include/taskflow/
install_subdir(
    'taskflow',
    install_dir: 'include',
)

# Generate pkgconfig
pkgconfig = import('pkgconfig')
pkgconfig.generate(
    name: 'Taskflow',
    description: 'A General-purpose Parallel and Heterogeneous Task Programming System',
    url: 'https://taskflow.github.io/',
    subdirs: 'taskflow',
    libraries: dependency('threads'),
)

