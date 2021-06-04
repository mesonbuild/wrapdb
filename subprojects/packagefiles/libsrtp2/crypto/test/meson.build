tests = [
  [ 'env', [ 'env.c' ], [] ],
  [ 'cipher_driver', [ 'cipher_driver.c', '../../test/getopt_s.c' ], '-v'],
  [ 'datatypes_driver', [ 'datatypes_driver.c', '../../test/util.c' ], [] ],
  [ 'stat_driver', [ 'stat_driver.c' ], [] ],
  [ 'sha1_driver', [ 'sha1_driver.c', '../../test/util.c' ], [] ],
  [ 'kernel_driver', [ 'kernel_driver.c', '../../test/getopt_s.c' ], '-v'],
]

includedirs = include_directories(
  '../..',
  '../../include',
  '../../test',
  '../../crypto/include',
)

foreach t : tests
  test(t[0],
    executable(t[0], t[1],
      include_directories: includedirs,
      link_with: libsrtp2_static
    ),
    args: t[2]
  )
endforeach
