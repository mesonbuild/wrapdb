project(
    'nghttp2',
    'c',
    license: 'mit',
    version: '1.56.0',
)
hex = '0123456789abcdef'
project_version_num = '0x' \
    + hex[meson.project_version().split('.')[0].to_int() / 16] \
    + hex[meson.project_version().split('.')[0].to_int() % 16] \
    + hex[meson.project_version().split('.')[1].to_int() / 16] \
    + hex[meson.project_version().split('.')[1].to_int() % 16] \
    + hex[meson.project_version().split('.')[2].to_int() / 16] \
    + hex[meson.project_version().split('.')[2].to_int() % 16]
configuration = configuration_data()
configuration.set('PACKAGE_VERSION', meson.project_version())
configuration.set('PACKAGE_VERSION_NUM', project_version_num)
configuration.set('PROJECT_VERSION', meson.project_version())
configuration.set('PROJECT_VERSION_MAJOR', meson.project_version().split('.')[0])
configuration.set('PROJECT_VERSION_MINOR', meson.project_version().split('.')[1])
configuration.set('PROJECT_VERSION_PATCH', meson.project_version().split('.')[2])
configuration.set('VERSION', meson.project_version())
configuration.set('exec_prefix', get_option('prefix'))
configuration.set('includedir', get_option('includedir'))
configuration.set('libdir', get_option('libdir'))
configuration.set('prefix', get_option('prefix'))

subdir('lib')
