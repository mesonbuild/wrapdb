# SPDX-License-Identifier: LGPL-2.1-or-later
# Copyright 2021 IBM Corp.

if get_option('docs')
  help2man_prog = find_program('help2man')
  tools = [
    'gpiodetect',
    'gpioinfo',
    'gpioget',
    'gpioset',
    'gpiofind',
    'gpiomon',
  ]
  mandir = join_paths(get_option('prefix'), get_option('mandir'))
  man1 = join_paths(mandir, 'man1')
  manpages = []
  foreach t : tools
    custom_target(
      '@0@.1'.format(t),
      input: get_variable(t),
      output: '@BASENAME@.1',
      depend_files: 'template',
      command: [
        help2man_prog,
        '@INPUT@',
        '--include=@CURRENT_SOURCE_DIR@/template',
        '--output=@OUTPUT@',
        '--no-info',
      ],
      install: true,
      install_dir: man1,
    )
  endforeach
endif
