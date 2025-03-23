numeric_test = {
  'num.accumulate': files('accumulate.cpp'),
  'num.adjacent_difference': files('adjacent_difference.cpp'),
  'num.inner_product': files('inner_product.cpp'),
  'num.iota': files('iota.cpp'),
  'num.partial_sum': files('partial_sum.cpp'),
}

foreach name, sources : numeric_test
  exe = executable(
    'range.v3.test.@0@'.format(name),
    sources: sources,
    dependencies: range_dep,
  )
  test(name, exe)
endforeach
