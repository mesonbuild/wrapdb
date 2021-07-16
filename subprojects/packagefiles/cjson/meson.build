project('cjson', 'c',
        version: '1.7.14',
        meson_version: '>=0.47.0',
        license: ['MIT'])

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
