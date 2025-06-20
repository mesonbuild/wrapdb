# SPDX-License-Identifier: LGPL-2.1-or-later
# Copyright 2021 IBM Corp.

project(
  'libgpiod',
  'c',
  default_options: ['warning_level=2', 'c_std=gnu99', 'cpp_std=gnu++11'],
  version: '1.6.5',
  license: 'LGPL-2.1-or-later',
  meson_version: '>=0.56.0',
)

host_system = host_machine.system()
if host_system != 'linux'
  msgfmt = '@0@ is not supported on @1@'
  error(msgfmt.format(meson.project_name(), host_system))
endif

add_project_arguments(
  '-D_GNU_SOURCE',
  language: 'c',
)

pkg = import('pkgconfig')

cc = meson.get_compiler('c')

err_not_found_lib = '@0@ not found (needed to build the library)'

lib_header_deps = [
  'getopt.h',
  'dirent.h',
  'sys/poll.h',
  'sys/sysmacros.h',
  'linux/gpio.h',
  'linux/version.h',
]
foreach h : lib_header_deps
  if not cc.has_header(h)
    error(err_not_found_lib.format(h))
  endif
endforeach

lib_function_deps = [
  ['ioctl', '#include <sys/ioctl.h>'],
  ['asprintf', '#include <stdio.h>'],
  ['scandir', '#include <dirent.h>'],
  ['alphasort', '#include <dirent.h>'],
  ['ppoll', '#include <poll.h>'],
  ['realpath', '#include <stdlib.h>'],
]
foreach fd : lib_function_deps
  if not cc.has_function(
    fd[0],
    prefix: fd[1],
    args: '-D_GNU_SOURCE',
  )
    error(err_not_found_lib.format(fd[0]))
  endif
endforeach

linux_headers_4_8_0 = '''#include <linux/version.h>
#if LINUX_VERSION_CODE < KERNEL_VERSION(4, 8, 0)
#error
#endif'''
if not cc.compiles(
  linux_headers_4_8_0,
  name: 'linux headers v4.8.0 check',
)
  error('libgpiod needs linux headers version >= 4.8.0')
endif

linux_headers_5_5_0 = '''#include <linux/version.h>
#if LINUX_VERSION_CODE < KERNEL_VERSION(5, 5, 0)
#error
#endif'''
kernel_pre_5_5 = not cc.compiles(
  linux_headers_5_5_0,
  name: 'linux headers v5.5.0 check',
)

gpiod_config = configuration_data()
gpiod_config.set_quoted('GPIOD_VERSION_STR', meson.project_version())
gpiod_config.set('KERNEL_PRE_5_5', kernel_pre_5_5)
configure_file(
  configuration: gpiod_config,
  output: 'config.h',
)
gpiod_includes = include_directories('include')

subdir('include')
subdir('lib')

if get_option('tools')
  err_not_found_tools = '@0@ not found (needed to build the tools)'

  # Check headers
  if not cc.has_header('sys/signalfd.h')
    error(err_not_found_tools.format('sys/signalfd.h header'))
  endif

  tool_function_deps = [
    ['basename', '#include <libgen.h>'],
    ['daemon', '#include <unistd.h>'],
    ['signalfd', '#include <sys/signalfd.h>'],
    ['setlinebuf', '#include <stdio.h>'],
  ]
  foreach fd : tool_function_deps
    if not cc.has_function(
      fd[0],
      prefix: fd[1],
      args: '-D_GNU_SOURCE',
    )
      error(err_not_found_tools.format(fd[0]))
    endif
  endforeach

  subdir('tools')
  subdir('man')
endif

if get_option('tests')
  err_not_found_tests = '@0@ not found (need to build the tests)'

  if not cc.has_function(
    'qsort',
    prefix: '#include <stdlib.h>',
    args: '-D_GNU_SOURCE',
  )
    error(err_not_found_tests.format('qsort'))
  endif

  threads_dep = dependency('threads')

  subdir('tests')
endif

subdir('bindings')

if get_option('docs')
  doxygen_prog = find_program('doxygen')

  if doxygen_prog.found()
    # Discussion:
    # https://github.com/mesonbuild/wrapdb/pull/130#pullrequestreview-729526961
    warning(
      'The supplied Doxyfile uses a fixed output path, skipping generation of library documentation and manpages',
    )
  endif
endif
