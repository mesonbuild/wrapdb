tests = [
  'badparam',
  'butterworth',
  'chebyshev1',
  'chebyshev2',
  'custom',
  'rbj',
  'state',
]

foreach t : tests
  exe = executable(
    t,
    t + '.cpp',
    dependencies: libiir_dep,
  )
  test(t, exe)
endforeach
