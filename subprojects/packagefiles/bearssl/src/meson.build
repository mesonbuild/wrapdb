src_lib = files('settings.c')

subdir('aead')
subdir('codec')
subdir('ec')
subdir('hash')
subdir('int')
subdir('kdf')
subdir('mac')
subdir('rand')
subdir('rsa')
subdir('ssl')
subdir('symcipher')
subdir('x509')

# Fix for clang-cl on Windows
cc = meson.get_compiler('c')

c_args = []
if cc.get_argument_syntax() == 'msvc'
  c_args += ['-D_CRT_SECURE_NO_WARNINGS']
endif

host_cpu = host_machine.cpu_family()
is_x86 = host_cpu in ['x86', 'x86_64']

vs_module_defs = 'bearssl-x64.def'

if cc.get_argument_syntax() == 'msvc'
  if host_cpu == 'x86_64'
    vs_module_defs = 'bearssl-x64.def'
  elif host_cpu == 'x86'
    vs_module_defs = 'bearssl-x86.def'
  endif
endif

bearssl_lib = library(
  'bearssl',
  src_lib,
  include_directories: inc,
  dependencies: m_dep,
  c_args: c_args,
  vs_module_defs: vs_module_defs,
  install: true,
)

bearssl_dep = declare_dependency(
  link_with: bearssl_lib,
  include_directories: inc_export,
)

meson.override_dependency('bearssl', bearssl_dep)
