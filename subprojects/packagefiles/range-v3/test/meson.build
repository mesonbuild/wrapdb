subdir('action')
subdir('algorithm')
subdir('iterator')
subdir('functional')
subdir('numeric')
subdir('range')
subdir('utility')
subdir('view')
subdir('experimental')

general_test = {
  'config': files('config.cpp'),
  'constexpr_core': files('constexpr_core.cpp'),
  'multiple': files('multiple1.cpp', 'multiple2.cpp'),
  'bug474': files('bug474.cpp'),
  'bug566': files('bug566.cpp'),
  'bug1322': files('bug1322.cpp'),
  'bug1335': files('bug1335.cpp'),
  'bug1633': files('bug1633.cpp'),
}

foreach name, sources : general_test
  exe = executable(
    'range.v3.test.@0@'.format(name),
    sources: sources,
    dependencies: range_dep,
  )
  test(name, exe)
endforeach
