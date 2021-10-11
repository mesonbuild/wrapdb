project('xtensor-python', 'cpp',
        version:'0.24.1',
        license:'BSD-3-Clause',
        default_options : ['warning_level=3', 'cpp_std=c++14'])

pybind_dep = dependency('pybind11',
    version: ['>=2.4.3', '<3.0.0'])

xtensor_dep = dependency('xtensor',
    version: ['>=0.21.2', '<1.0.0'])

python = import('python').find_installation('python3')

npy_incstr = run_command(
    [python, '-c', 'import numpy; print(numpy.get_include())'],
    check: false).stdout().strip()

if (npy_incstr == '')
    warning('Unable to find numpy (Looking for it using ' + python.path() +
        '), disabling python bindings.')
endif

extra_cflags = ['-I' + npy_incstr]

xtensor_python_dep = declare_dependency(
    include_directories: [include_directories('include', is_system: true),
        include_directories(npy_incstr, is_system: true)],
    dependencies:[xtensor_dep, pybind_dep])

# Workaround from issue: https://github.com/mesonbuild/meson/issues/2550
if meson.is_subproject()
    install_dir = get_option('subproj_includedir')
    extra_cflags += '-I' + get_option('prefix') / install_dir
else
    install_dir = get_option('includedir')
endif

install_subdir('include/xtensor-python', install_dir: install_dir)

pkgconfig = import('pkgconfig')
pkgconfig.generate(name: meson.project_name(),
    version: meson.project_version(),
    description: 'Python bindings for the xtensor C++ multi-dimensional array library.',
    requires: ['xtensor', 'pybind11'],
    extra_cflags: extra_cflags)
