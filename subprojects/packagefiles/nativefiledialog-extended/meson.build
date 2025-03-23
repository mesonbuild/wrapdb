project(
  'nativefiledialog-extended',
  'cpp',
  version: '1.2.1',
  license: 'Zlib',
  meson_version: '>=1.2.0',
  default_options: {
    'cpp_std': ['c++14'],
  },
)

subdir('src')

if get_option('tests')
  subdir('test')
endif
