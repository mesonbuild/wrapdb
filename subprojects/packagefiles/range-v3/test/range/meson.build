range_test = {
  'range.access': files('access.cpp'),
  'range.conversion': files('conversion.cpp'),
  'range.index': files('index.cpp'),
  'range.operations': files('operations.cpp'),
}

foreach name, sources : range_test
  exe = executable(
    'range.v3.test.@0@'.format(name),
    sources: sources,
    dependencies: range_dep,
  )
  test(name, exe)
endforeach
