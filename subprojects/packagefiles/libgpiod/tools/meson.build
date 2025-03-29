# SPDX-License-Identifier: LGPL-2.1-or-later
# Copyright 2021 IBM Corp.

tools_common_dep = declare_dependency(
  sources: ['tools-common.c', 'tools-common.h'],
)

tools_deps = [gpiod_dep, tools_common_dep]

gpiodetect = executable(
  'gpiodetect',
  'gpiodetect.c',
  dependencies: tools_deps,
  install: true,
)

gpioinfo = executable(
  'gpioinfo',
  'gpioinfo.c',
  dependencies: tools_deps,
  install: true,
)

gpioget = executable(
  'gpioget',
  'gpioget.c',
  dependencies: tools_deps,
  install: true,
)

gpioset = executable(
  'gpioset',
  'gpioset.c',
  dependencies: tools_deps,
  install: true,
)

gpiomon = executable(
  'gpiomon',
  'gpiomon.c',
  dependencies: tools_deps,
  install: true,
)

gpiofind = executable(
  'gpiofind',
  'gpiofind.c',
  dependencies: tools_deps,
  install: true,
)

if get_option('tests')
  # This seems like a hack?
  install_data(
    'gpio-tools-test',
    install_dir: get_option('bindir'),
    install_mode: 'rwxr-xr-x',
  )

  install_data(
    'gpio-tools-test.bats',
    install_dir: get_option('bindir'),
    install_mode: 'rwxr-xr-x',
  )
endif
