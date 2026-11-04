version_conf = configuration_data()
version_conf.set('VERSION_INFO_MAJOR_VERSION', version_parts[0])
version_conf.set('VERSION_INFO_MINOR_VERSION', version_parts[1])
version_conf.set('VERSION_INFO_MAINT_VERSION', version_parts[2])
version_conf.set(
  'VOLK_VERSION_DECIMAL',
  version_parts[0].to_int() * 10000 + version_parts[1].to_int() * 100 + version_parts[2].to_int(),
)

volk_version_h = configure_file(
  input: 'volk_version.h.in',
  output: 'volk_version.h',
  configuration: version_conf,
  install_dir: get_option('includedir') / 'volk',
)

volk_gen_headers = []
foreach name : ['volk', 'volk_cpu', 'volk_config_fixed', 'volk_typedefs']
  volk_gen_headers += custom_target(
    input: meson.project_source_root() / 'tmpl' / (name + '.tmpl.h'),
    output: name + '.h',
    command: tmpl_command,
    depend_files: tmpl_depends,
    install: true,
    install_dir: get_option('includedir') / 'volk',
  )
endforeach

install_headers(
  'constants.h',
  'saturation_arithmetic.h',
  'volk_alloc.hh',
  'volk_avx2_fma_intrinsics.h',
  'volk_avx2_intrinsics.h',
  'volk_avx512_intrinsics.h',
  'volk_avx_intrinsics.h',
  'volk_common.h',
  'volk_complex.h',
  'volk_malloc.h',
  'volk_neon_intrinsics.h',
  'volk_prefs.h',
  'volk_sse3_intrinsics.h',
  'volk_sse_intrinsics.h',
  kernel_headers,
  subdir: 'volk',
)
