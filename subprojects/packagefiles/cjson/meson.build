project('cjson', 'c',
        version: '1.7.15',
        meson_version: '>=0.49.0',
        license: ['MIT'])

cc = meson.get_compiler('c')
if cc.get_id() == 'msvc'
  if get_option('buildtype') != 'static'
    add_project_arguments('-DCJSON_EXPORT_SYMBOLS', language : 'c')
  else
    add_project_arguments('-DCJSON_IMPORT_SYMBOLS', language : 'c')
  endif
endif

if host_machine.system() == 'windows' and cc.get_argument_syntax() == 'gcc'
  add_project_arguments('-DUNITY_WEAK_ATTRIBUTE=__attribute__((weak))', language: 'c')
endif

headers = files('cJSON.h', 'cJSON_Utils.h')

subdir('include-workaround-meson/cjson')

libcjson = library('cjson',
                   ['cJSON.c', 'cJSON_Utils.c'],
                   include_directories: ['.'],
                   install: true)

libcjson_dep = declare_dependency(include_directories: ['include-workaround-meson'],
                                  link_with: libcjson)

if meson.version().version_compare('>=0.54.0')
    meson.override_dependency('libcjson', libcjson_dep)
endif

# the tests do not work on MSVC. Missing unity_setup.c
if get_option('tests')
    e = executable('root-test', 'test.c', dependencies: libcjson_dep)
    test('root-test', e)

    subdir('tests')
endif
