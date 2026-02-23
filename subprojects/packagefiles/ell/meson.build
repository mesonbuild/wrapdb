# SPDX-License-Identifier: LGPL-2.1-or-later
project(
  'ell',
  'c',
  version: '0.82',
  license: 'LGPL-2.1-or-later',
  default_options: ['default_library=shared'],
  meson_version: '>= 1.3.0',
)

cc = meson.get_compiler('c')
find_program(
  'awk',
  required: true,
)
config_h = configuration_data()

checked_funcs = ['explicit_bzero', 'rawmemchr']

foreach func : checked_funcs
  config_h.set('HAVE_' + func.to_upper(), cc.has_function(func))
endforeach

required_funcs = ['getrandom', 'signalfd', 'timerfd_create', 'epoll_create']

foreach func : required_funcs
  cc.has_function(
    func,
    required: true,
  )
endforeach

required_headers = ['linux/types.h', 'linux/if_alg.h']

foreach header : required_headers
  cc.has_header(
    header,
    required: true,
  )
endforeach

glib_dep = dependency(
  'glib-2.0',
  version: '>= 2.32',
  required: get_option('glib'),
)
openssl = find_program(
  'openssl',
  required: get_option('cert-tests'),
)
sh = find_program(
  'sh',
  required: get_option('cert-tests'),
)
xxd = find_program(
  'xxd',
  required: get_option('cert-tests'),
)

if openssl.found()
  r = run_command(
    openssl,
    'list',
    '-providers',
    check: false,
  )
  if r.returncode() == 0
    openssl_legacy = ['-provider', 'legacy', '-provider', 'default']
  else
    openssl_legacy = ''
  endif
endif

add_project_arguments(
  '-DHAVE_CONFIG_H',
  language: 'c',
)
configure_file(
  output: 'config.h',
  configuration: config_h,
)

subdir('ell')
subdir('tools')
subdir('unit')
subdir('examples')
