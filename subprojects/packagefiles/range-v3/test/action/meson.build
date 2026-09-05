action_test = {
  'act.concepts': files('cont_concepts.cpp'),
  'act.adjacent_remove_if': files('adjacent_remove_if.cpp'),
  'act.drop': files('drop.cpp'),
  'act.drop_while': files('drop_while.cpp'),
  'act.insert': files('insert.cpp'),
  'act.join': files('join.cpp'),
  'act.push_front': files('push_front.cpp'),
  'act.push_back': files('push_back.cpp'),
  'act.remove_if': files('remove_if.cpp'),
  'act.remove': files('remove.cpp'),
  'act.unstable_remove_if': files('unstable_remove_if.cpp'),
  'act.reverse': files('reverse.cpp'),
  'act.shuffle': files('shuffle.cpp'),
  'act.slice': files('slice.cpp'),
  'act.sort': files('sort.cpp'),
  'act.split': files('split.cpp'),
  'act.stable_sort': files('stable_sort.cpp'),
  'act.stride': files('stride.cpp'),
  'act.take': files('take.cpp'),
  'act.take_while': files('take_while.cpp'),
  'act.transform': files('transform.cpp'),
  'act.unique': files('unique.cpp'),
}

foreach name, sources : action_test
  exe = executable(
    'range.v3.test.@0@'.format(name),
    sources: sources,
    dependencies: range_dep,
  )
  test(name, exe)
endforeach
