project('libsass', 'c', 'cpp',
        version: '3.6.4',
        meson_version : '>= 0.48.0',
        default_options: [
            'c_std=c99',
            'cpp_std=c++11',
            'buildtype=debugoptimized',
        ])

add_project_arguments(
  '-DLIBSASS_VERSION="@0@"'.format(meson.project_version()),
  language: ['cpp'])

cpp = meson.get_compiler('cpp')
if cpp.get_id() != 'msvc'
  add_project_arguments(
    cpp.get_supported_arguments(['-Wno-non-virtual-dtor']),
    language: ['cpp'])
endif

inc = include_directories('include')
winres_path = files(join_paths('res', 'resource.rc'))

subdir('include')
subdir('src')
