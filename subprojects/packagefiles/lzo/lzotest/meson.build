t = executable('lzotest', 'lzotest.c', dependencies: lzo2_dep)

test('basic lzotest', t, args: ['-mlzo', '-n2', '-q', files('../COPYING')], suite: 'basic')
test('exhaustive lzotest', t, args: ['-mavail', '-n10', '-q', files('../COPYING')])
check = find_program('../util/check.sh', required: false)
if check.found()
    test('lzotest directory check', check,
      args: [topdir],
      timeout: 150,
      workdir: meson.current_build_dir()
    )
endif
