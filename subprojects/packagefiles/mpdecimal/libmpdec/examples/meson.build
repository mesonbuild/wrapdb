examples = [
  'compare',
  'div',
  'divmod',
  'multiply',
  'pow',
  'powmod',
  'shift',
  'sqrt',
]

foreach example : examples
  executable(
    example,
    '@0@.c'.format(example),
    dependencies: mpdec_dep,
  )
endforeach
