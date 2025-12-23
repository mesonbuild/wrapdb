version_splits = meson.project_version().split('.')

cdata = configuration_data()
cdata.set('cpr_VERSION', meson.project_version())
cdata.set('cpr_VERSION_MAJOR', version_splits[0])
cdata.set('cpr_VERSION_MINOR', version_splits[1])
cdata.set('cpr_VERSION_PATCH', version_splits[2])
# Should be in hex (two digits each), but since Meson cannot output to hex do math manually
cdata.set(
  'cpr_VERSION_NUM',
  version_splits[0].to_int() * 65536 + version_splits[1].to_int() * 256 + version_splits[2].to_int(),
)

configure_file(
  input: meson.project_source_root() / 'cmake' / 'cprver.h.in',
  output: 'cprver.h',
  format: 'cmake',
  configuration: cdata,
  install: true,
  install_dir: get_option('includedir') / 'cpr',
  install_tag: 'devel',
)
