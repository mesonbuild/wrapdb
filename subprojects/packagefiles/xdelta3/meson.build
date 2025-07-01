project(
  'xdelta3',
  'c',
  version: '3.1.0',
  license: 'GPL-2.0-or-later',
  meson_version: '>=0.63.0',
  default_options: ['c_std=c99'],
)

cc = meson.get_compiler('c')
add_project_arguments(
  '-DHAVE_CONFIG_H',
  cc.get_supported_arguments(
    '-Wno-format-truncation',
    '-Wno-switch-unreachable',
    '-Wno-unused-function',
  ),
  language: 'c',
)
if host_machine.system() == 'windows'
  add_project_arguments(
    '-D_CRT_NONSTDC_NO_DEPRECATE',
    '-D_CRT_SECURE_NO_WARNINGS',
    language: 'c',
  )
endif

cdata = configuration_data()
cdata.set('HAVE_ALIGNED_ACCESS_REQUIRED', 1)
cdata.set('REGRESSION_TEST', 1)
cdata.set('SECONDARY_DJW', 1)
cdata.set('SECONDARY_FGK', 1)
cdata.set('XD3_MAIN', 1)
cdata.set('XD3_DEBUG', 0)
if host_machine.system() == 'windows'
  cdata.set('XD3_WIN32', 1)
  cdata.set('EXTERNAL_COMPRESSION', 0)
  cdata.set('SHELL_TESTS', 0)
endif

foreach type : ['unsigned int', 'unsigned long', 'unsigned long long', 'size_t']
  cdata.set('SIZEOF_' + type.underscorify().to_upper(), cc.sizeof(type))
endforeach
if not cc.has_type(
  'pid_t',
  prefix: '#include <sys/types.h>',
)
  cdata.set('pid_t', 'int')
endif
if not cc.has_function_attribute('format')
  cdata.set('PRINTF_ATTRIBUTE(x,y)', '')
endif

m_dep = cc.find_library(
  'm',
  required: false,
)

liblzma_dep = dependency(
  'liblzma',
  required: get_option('lzma'),
)
if liblzma_dep.found()
  cdata.set('HAVE_LZMA_H', 1)
endif

configure_file(
  configuration: cdata,
  output: 'config-generated.h',
)

configure_file(
  input: 'config.h.meson',
  output: 'config.h',
  copy: true,
)

xdelta3 = executable(
  'xdelta3',
  'xdelta3.c',
  dependencies: [m_dep, liblzma_dep],
)
meson.override_find_program('xdelta3', xdelta3)

test(
  'xdelta3',
  xdelta3,
  args: 'test',
  timeout: 500,
)
