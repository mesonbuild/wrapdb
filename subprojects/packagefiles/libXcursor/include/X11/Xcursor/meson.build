cdata = configuration_data()
ver = meson.project_version().split('.')
cdata.set('XCURSOR_LIB_MAJOR', ver[0])
cdata.set('XCURSOR_LIB_MINOR', ver[1])
cdata.set('XCURSOR_LIB_REVISION', ver[2])

xcursor_h = configure_file(
  input: 'Xcursor.h.in',
  output: 'Xcursor.h',
  configuration: cdata,
)
