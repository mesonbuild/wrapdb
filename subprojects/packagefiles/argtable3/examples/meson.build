if not get_option('examples')
  subdir_done()
endif

examples = [
  'echo',
  'ls',
  'multisyntax',
  'mv',
  'myprog',
  'myprog_C89',
  'testargtable3',
  'uname',
]

foreach e : examples
  executable(
    e,
    '@0@.c'.format(e),
    dependencies: argtable3_dep,
  )
endforeach

subdir('multicmd')
