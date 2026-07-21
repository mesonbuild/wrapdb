vmaf_version_conf = configuration_data()
vmaf_version_conf.set('VCS_TAG', meson.project_version())
rev_target = configure_file(
  input: 'vcs_version.h.in',
  output: 'vcs_version.h',
  configuration: vmaf_version_conf,
)

subdir('libvmaf')
