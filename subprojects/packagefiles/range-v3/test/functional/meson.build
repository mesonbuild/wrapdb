functional_test = {
  'fun.bind_back': files('bind_back.cpp'),
  'fun.on': files('on.cpp'),
}

foreach name, sources : functional_test
  exe = executable(
    'range.v3.test.@0@'.format(name),
    sources: sources,
    dependencies: range_dep,
  )
  test(name, exe)
endforeach
