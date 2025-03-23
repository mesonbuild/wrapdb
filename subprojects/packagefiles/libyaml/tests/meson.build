tests = ['test-reader', 'test-version']

foreach name : tests
  exe = executable(
    name,
    sources: [name + '.c'],
    include_directories: [inc, include_directories('..')],
    link_with: yaml_lib,
  )
  test(name, exe)
endforeach
