project(
  'QuaZip',
  ['c', 'cpp'],
  version: '1.4',
  license: 'LGPL-2.1 with static linking exception',
)

qt_dep = dependency(
  'qt6',
  modules: ['Core', 'Core5Compat'],
  required: false,
)
if qt_dep.found()
  qt = import('qt6')
else
  qt_dep = dependency(
    'qt5',
    modules: 'Core',
  )
  qt = import('qt5')
endif
zlib_dep = dependency(
  'zlib',
  fallback: ['zlib', 'zlib_dep'],
)

subdir('quazip')
