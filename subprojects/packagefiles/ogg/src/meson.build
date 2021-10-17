sources = ['bitwise.c', 'framing.c']

libogg = library('ogg',
  sources,
  include_directories : incdir,
  vs_module_defs: '../win32/ogg.def',
  version: lib_version,
  soversion: cc.get_id() == 'msvc' ? '' : lib_soversion,
  install: true,
)

bw_test = executable('bitwise', 'bitwise.c',
  include_directories : incdir,
  c_args : '-D_V_SELFTEST'
)
framing_test = executable('framing', 'framing.c',
  include_directories : incdir,
  c_args : '-D_V_SELFTEST'
)

test('bitwise', bw_test)
test('framing', framing_test)

libogg_dep = declare_dependency(link_with : libogg,
  include_directories : incdir)

pkgconfig = import('pkgconfig')
pkgconfig.generate(libogg,
  description: 'ogg is a library for manipulating ogg bitstreams',
)
