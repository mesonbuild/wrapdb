add_languages(
  'cpp',
  required: true,
  native: false,
)

qt5_dep = dependency(
  'qt5',
  modules: ['Core', 'Test'],
)

src = [
  'test.cpp',
  'test.h',
]

prep = qt5.preprocess(
  moc_headers: 'test.h',
  moc_extra_arguments: ['-DMAKES_MY_MOC_HEADER_COMPILE'],
  dependencies: qt5_dep,
)

exe = executable(
  'qt5-test',
  [src, prep],
  include_directories: [top_inc, libportal_inc],
  dependencies: [qt5_dep, libportal_qt5_dep],
  cpp_args: '-std=c++11',
)

test('Qt 5 unit test', exe)
