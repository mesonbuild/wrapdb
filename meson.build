project(
  'QuaZip',
  ['c', 'cpp'],
  version: '0.7.3',
  license: 'LGPL-2.1 with static linking exception'
)

qt5 = import('qt5')
qt5_dep = dependency('qt5', modules: 'Core')
zlib_dep = dependency('zlib', fallback: ['zlib', 'zlib_dep'])

subdir('quazip')
