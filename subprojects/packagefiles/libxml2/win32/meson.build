rcvdata = configuration_data()
rcvdata.set('LIBXML_MAJOR_VERSION', major)
rcvdata.set('LIBXML_MINOR_VERSION', minor)
rcvdata.set('LIBXML_MICRO_VERSION', micro)
rcvdata.set_quoted('LIBXML_DOTTED_VERSION', meson.project_version())
configure_file(
  output: 'rcVersion.h',
  configuration: rcvdata,
)

rcfile = configure_file(input: 'libxml2.rc', output: 'libxml2.rc', copy: true)
windows = import('windows')
sources += windows.compile_resources(rcfile)
