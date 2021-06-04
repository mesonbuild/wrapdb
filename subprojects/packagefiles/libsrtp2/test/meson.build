tests = [
  [ 'test_srtp', [ 'test_srtp.c' ], [] ],
  [ 'rdbx_driver', [ 'rdbx_driver.c', 'getopt_s.c' ], '-v' ],
  [ 'srtp_driver', [ 'srtp_driver.c', 'util.c', 'getopt_s.c' ], '-v' ],
  [ 'roc_driver', [ 'roc_driver.c' ], [] ],
  [ 'replay_driver', [ 'replay_driver.c' ], [] ],
  [ 'dtls_srtp_driver', [ 'dtls_srtp_driver.c', 'getopt_s.c' ], [] ],
]

includedirs = include_directories(
  '..',
  '../include',
  '../crypto/include',
)

foreach t : tests
  test(t[0],
    executable(t[0], t[1],
      include_directories: includedirs,
      link_with: libsrtp2_static,
      c_args: host_machine.system() == 'windows' ? '-DWIN32_LEAN_AND_MEAN' : [],
    ),
    args: t[2],
  )
endforeach
