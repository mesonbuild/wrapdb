sources = ['bitwise.c', 'framing.c']

if get_option('shared_lib')
  libtype = 'shared_library'
else
  libtype = 'static_library'
endif

libogg = build_target('ogg',
  sources,
  include_directories : incdir,
  target_type : libtype
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
