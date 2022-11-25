project(
  'theora',
  'c',
  'cpp',
  version: '1.1.1',
  meson_version: '>= 0.49.0',
  license: 'BSD-3-Clause',
  default_options: ['c_std=c11'],
)

conf = configuration_data()

compile_args = []

cc = meson.get_compiler('c')

if cc.get_argument_syntax() != 'msvc'
  compile_args += cc.get_supported_arguments(
    '-Wno-parentheses',
    '-Wno-shift-op-parentheses',
    '-Wno-shift-negative-value',
  )
endif

m_dep = cc.find_library('m', required: false)

if get_option('collect-metrics')
  add_project_arguments('-DOC_COLLECT_METRICS', language: 'c')
endif

ogg_dep = dependency('ogg', version: '>= 1.1', required: true)

asm = not get_option('asm').disabled()
if asm
  if host_machine.cpu_family() == 'x86_64'
    conf.set('CPU_x86_64', true)
    if cc.get_id() != 'msvc'
      conf.set('OC_X86_ASM', true)
      conf.set('OC_X86_64_ASM', true)
    endif
  elif host_machine.cpu_family() == 'x86'
    conf.set('OC_X86_ASM', true)
  endif
endif

config_h = configure_file(configuration: conf, output: 'config.h')

config_dep = declare_dependency(sources: config_h)

add_project_arguments('-DHAVE_CONFIG_H', language: 'c')

pkg = import('pkgconfig')
windows = import('windows')

subdir('include')

subdir('lib')
