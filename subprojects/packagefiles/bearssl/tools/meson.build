src_brssl = files(
  'brssl.c',
  'certs.c',
  'chain.c',
  'client.c',
  'errors.c',
  'files.c',
  'impl.c',
  'keys.c',
  'names.c',
  'server.c',
  'skey.c',
  'sslio.c',
  'ta.c',
  'twrch.c',
  'vector.c',
  'verify.c',
  'xmem.c',
)

ws2_dep = cc.find_library(
  'ws2_32',
  required: host_machine.system() == 'windows',
)

executable(
  'brssl',
  src_brssl,
  include_directories: inc,
  link_with: bearssl_lib,
  dependencies: [m_dep, ws2_dep],
  build_by_default: false,
)
