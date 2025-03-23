# SPDX-License-Identifier: LGPL-2.1-or-later
# Copyright 2021 IBM Corp.

catch2_dep = dependency('catch2')

gpiod_cxx_test = executable(
  'gpiod-cxx-test',
  'gpiod-cxx-test-main.cpp',
  'gpiod-cxx-test.cpp',
  'gpio-mockup.cpp',
  'gpio-mockup.hpp',
  'tests-chip.cpp',
  'tests-event.cpp',
  'tests-event.cpp',
  'tests-iter.cpp',
  'tests-line.cpp',
  dependencies: [gpiodcxx_dep, gpiomockup_dep, catch2_dep, threads_dep],
  install: true,
)
