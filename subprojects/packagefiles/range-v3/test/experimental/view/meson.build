experimental_view_test = {
  'view.shared' : files('shared.cpp'),
}

foreach name, sources : experimental_view_test
  exe = executable(
    'range.v3.test.@0@'.format(name),
    sources: sources,
    dependencies: range_dep,
  )
  test(name, exe)
endforeach
