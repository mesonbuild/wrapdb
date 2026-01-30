add_languages(
  'cpp',
  required: true,
  native: false,
)

qt6_dep = dependency(
  'qt6',
  modules: ['Core', 'Test'],
)

src = [
  'test.cpp',
  'test.h',
]

prep = qt6.preprocess(
  moc_headers: 'test.h',
  moc_extra_arguments: ['-DMAKES_MY_MOC_HEADER_COMPILE'],
  dependencies: qt6_dep,
)

exe = executable(
  'qt6-test',
  [src, prep],
  include_directories: [top_inc, libportal_inc],
  dependencies: [qt6_dep, libportal_qt6_dep],
  cpp_args: '-std=c++17',
)

test('Qt 6 unit test', exe)
