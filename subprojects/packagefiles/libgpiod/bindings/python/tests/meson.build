# SPDX-License-Identifier: LGPL-2.1-or-later
# Copyright 2021 IBM Corp.

gpiomockuppy = python3.extension_module(
  'gpiomockup',
  'gpiomockupmodule.c',
  include_directories: gpiomockup_includes,
  dependencies: python3_dep,
  install: true,
)

install_data(
  'gpiod_py_test.py',
  install_dir: get_option('bindir'),
  install_mode: 'rwxr-xr-x',
)
