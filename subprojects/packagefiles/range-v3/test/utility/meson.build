utility_test = {
  'utility.box': files('box.cpp'),
  'utility.concepts': files('concepts.cpp'),
  'utility.common_type': files('common_type.cpp'),
  'utility.compare': files('compare.cpp'),
  'utility.functional': files('functional.cpp'),
  'utility.swap': files('swap.cpp'),
  'utility.variant': files('variant.cpp'),
  'utility.meta': files('meta.cpp'),
  'utility.scope_exit': files('scope_exit.cpp'),
  'utility.semiregular_box': files('semiregular_box.cpp'),
}

foreach name, sources : utility_test
  exe = executable(
    'range.v3.test.@0@'.format(name),
    sources: sources,
    dependencies: range_dep,
  )
  test(name, exe)
endforeach
