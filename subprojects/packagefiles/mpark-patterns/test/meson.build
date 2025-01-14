gtest_dep = dependency('gtest_main')

tests = [
    'aggregate',
    'array',
    'as',
    'balance',
    'calc',
    'ds',
    'identifier',
    'intro',
    'let',
    'optional',
    'regex',
    'variadic',
    'when',
]

foreach f : tests
  test(f + '.test', executable(f + '.cpp', dependencies: gtest_dep)) 
endforeach
