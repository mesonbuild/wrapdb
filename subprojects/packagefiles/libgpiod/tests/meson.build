# SPDX-License-Identifier: LGPL-2.1-or-later
# Copyright 2021 IBM Corp.

subdir('mockup')

glib_dep = dependency(
  'glib-2.0',
  version: '>=2.50',
  required: true,
)

gpiod_test = executable(
  'gpiod-test',
  'gpiod-test.c',
  'gpiod-test.h',
  'tests-chip.c',
  'tests-ctxless.c',
  'tests-event.c',
  'tests-iter.c',
  'tests-line.c',
  'tests-misc.c',
  c_args: '-DG_LOG_DOMAIN="gpiod-test"',
  dependencies: [gpiod_dep, gpiomockup_dep, glib_dep, threads_dep],
  install: true,
)
