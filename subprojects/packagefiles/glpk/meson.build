project(
  'glpk',
  'c',
  license: 'GPL-3.0-or-later',
  version: '5.0',
  meson_version: '>=0.50.0',
)

override_opts = ['c_std=c89']

cc = meson.get_compiler('c')

deps = []
libm_dep = cc.find_library(
  'm',
  required: false,
)
deps += libm_dep

gmp_dep = dependency(
  'gmp',
  required: get_option('with-gmp'),
)
deps += gmp_dep

enable_dl = get_option('enable-dl')

if enable_dl == 'ltdl'
  ltdl_dep = cc.find_library(
    'ltdl',
    has_headers: 'ltdl.h',
    required: true,
  )
  deps += ltdl_dep
endif

cdata = configuration_data()
cdata.set('HAVE_SYS_TIME_H', cc.check_header('sys/time.h'))
cdata.set(
  'HAVE_GETTIMEOFDAY',
  host_machine.system() != 'windows' and cc.has_function('gettimeofday'),
)
cdata.set('HAVE_GMP', gmp_dep.found())
cdata.set('HAVE_LTDL', enable_dl == 'ltdl' and ltdl_dep.found())
cdata.set('HAVE_DLFCN', enable_dl == 'dlfcn' and cc.check_header('dlfcn.h'))

if host_machine.system() == 'windows'
  cdata.set('TLS', '__declspec(thread)')
else
  foreach f : ['_Thread_local', '__thread', '__declspec(thread)']
    if cc.compiles(
      '#include <stdlib.h> void func() { static ' + f + ' int bar; exit(1);}',
    )
      cdata.set('TLS', f)
      break
    endif
  endforeach
endif
configure_file(
  output: 'config.h',
  configuration: cdata,
)

add_project_arguments(
  '-DHAVE_CONFIG_H',
  language: 'c',
)

if host_machine.system() == 'windows'
  add_project_arguments(
    '-D__WOE__=1',
    language: 'c',
  )
endif

subdir('src')
subdir('examples')
