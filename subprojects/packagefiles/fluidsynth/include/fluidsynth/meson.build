fluidsynth_versions = meson.project_version().split('.')

fluidsynth_versions_conf = {
  'FLUIDSYNTH_VERSION': '"@0@"'.format(meson.project_version()),
  'FLUIDSYNTH_VERSION_MAJOR': fluidsynth_versions[0].to_int(),
  'FLUIDSYNTH_VERSION_MINOR': fluidsynth_versions[1].to_int(),
  'FLUIDSYNTH_VERSION_MICRO': fluidsynth_versions[2].to_int(),
}

configure_file(
  input: 'version.h.in',
  output: 'version.h',
  configuration: fluidsynth_versions_conf,
)
