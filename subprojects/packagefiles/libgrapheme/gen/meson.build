gendir = include_directories('.')
gen_headers_tgt = {
  'case': files(
    '../data/DerivedCoreProperties.txt',
    '../data/SpecialCasing.txt',
    '../data/UnicodeData.txt',
  ),
  'character': files(
    '../data/DerivedCoreProperties.txt',
    '../data/GraphemeBreakProperty.txt',
    '../data/emoji-data.txt',
  ),
  'character-test': files('../data/GraphemeBreakTest.txt'),
  'line': files(
    '../data/EastAsianWidth.txt',
    '../data/LineBreak.txt',
    '../data/emoji-data.txt',
  ),
  'line-test': files('../data/LineBreakTest.txt'),
  'sentence': files('../data/SentenceBreakProperty.txt'),
  'sentence-test': files('../data/SentenceBreakTest.txt'),
  'word': files('../data/WordBreakProperty.txt'),
  'word-test': files('../data/WordBreakTest.txt'),
}

chdir_wrapper = files('chdir_wrapper.py')
python_exe = find_program(
  'python',
  'python3',
  required: true,
  native: true,
  version: '>=3',
)
gen_headers = []
foreach exe_name, data_files : gen_headers_tgt
  src = exe_name + '.c'
  hdr = exe_name + '.h'
  exe = executable(
    'gen-' + exe_name,
    [src, 'util.c'],
    native: true,
  )
  gen = custom_target(
    hdr,
    output: hdr,
    depend_files: data_files,
    command: [python_exe, chdir_wrapper, exe],
    env: {
      'PROJECT_SOURCE_ROOT': meson.project_source_root(),
    },
    capture: true,
  )
  gen_headers += gen
endforeach
