# SPDX-License-Identifier: LGPL-2.1-or-later
# Copyright 2021 IBM Corp.

python = import('python')
python3 = python.find_installation('python3')
python3_dep = python3.dependency()

gpiodpy = python3.extension_module(
  'gpiod',
  'gpiodmodule.c',
  dependencies: [gpiod_dep, python3_dep],
  install: true,
)

if get_option('tests')
  subdir('tests')
endif
