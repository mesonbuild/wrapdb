cc = meson.get_compiler('c')
cxx = meson.get_compiler('cpp')

common_c_src = 'common/scpi-def.c'
common_cxx_src = 'common-cxx/scpi-def.cpp'

c_args = []
cpp_args = []

test_interactive_exe = executable('test-interactive',
  common_c_src,
  'test-interactive/main.c',
  c_args : c_args,
  dependencies : libscpi_dep,
)

test_interactive_cxx_exe = executable('test-interactive-cxx',
  common_cxx_src,
  'test-interactive-cxx/main.cpp',
  cpp_args : cpp_args,
  dependencies : libscpi_dep,
)

test_parser_exe = executable('test-parser',
  common_c_src,
  'test-parser/main.c',
  c_args : c_args,
  dependencies : libscpi_dep,
)

if cc.has_header('netinet/tcp.h')
  test_tcp_exe = executable('test-tcp',
    common_c_src,
    'test-tcp/main.c',
    c_args : c_args,
    dependencies : libscpi_dep,
  )

  test_tcp_srq_exe = executable('test-tcp-srq',
    common_c_src,
    'test-tcp-srq/main.c',
    c_args : c_args,
    dependencies : libscpi_dep,
  )
endif
