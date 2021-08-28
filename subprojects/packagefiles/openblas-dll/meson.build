project('openblas-dll', 'cpp',
    version:'0.3.7',
    license:'BSD-3-Clause')

openblas_dll_dep = []
openblas_dll_includes = [include_directories('include', is_system: true)]

if host_machine.system() == 'windows'
    cc = meson.get_compiler('cpp')
    prebuilt_openblas_dll = cc.find_library('openblas', dirs: [meson.current_source_dir() + '/bin'], required: false)

    mingw_dll_dep = dependency('gfortran-3')

    openblas_dll_dep = declare_dependency(include_directories: openblas_dll_includes,
                                          dependencies: [prebuilt_openblas_dll, mingw_dll_dep])

endif
