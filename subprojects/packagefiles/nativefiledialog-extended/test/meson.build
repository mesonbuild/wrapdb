test_files = [
  'test_opendialog.c',
  'test_opendialog_cpp.cpp',
  'test_opendialogmultiple.c',
  'test_opendialogmultiple_cpp.cpp',
  'test_opendialogmultiple_enum.c',
  'test_pickfolder.c',
  'test_pickfolder_cpp.cpp',
  'test_savedialog.c',
]

add_languages(
  'c',
  native: false,
)

foreach test : test_files
  name = test.replace('.', '_')

  text_exe = executable(
    'test_' + name,
    test,
    dependencies: nfde_dep,
  )

  test('test_' + name, text_exe)
endforeach


