if get_option('samples') and get_option('tools')
  sample_conf = configuration_data()
  sample_file = configure_file(
    output: 'config_sample.h',
    configuration: sample_conf,
  )

  toolinc = include_directories('common')

  if get_option('client')
    executable(
      'tv_ctrlpt',
      'common/sample_util.c',
      'common/tv_ctrlpt.c',
      'linux/tv_ctrlpt_main.c',
      include_directories: toolinc,
      dependencies: [libupnp_dep, threads_dep],
      override_options: cstd,
      install: true,
    )
  endif

  if get_option('client') and get_option('device')
    executable(
      'tv_combo',
      'common/sample_util.c',
      'common/tv_ctrlpt.c',
      'common/tv_device.c',
      'linux/tv_combo_main.c',
      include_directories: toolinc,
      dependencies: [libupnp_dep, threads_dep],
      override_options: cstd,
      install: true,
    )
  endif

  if get_option('device')
    executable(
      'tv_device',
      'common/sample_util.c',
      'common/tv_device.c',
      'linux/tv_device_main.c',
      include_directories: toolinc,
      dependencies: [libupnp_dep, threads_dep],
      override_options: cstd,
      install: true,
    )

    install_subdir(
      'web',
      install_dir: 'share/upnp',
      strip_directory: true,
    )
  endif
endif
