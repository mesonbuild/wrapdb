gendir = include_directories('.')
gen_headers_tgt = {
  'case.h': files(
    '../data/DerivedCoreProperties.txt',
    '../data/SpecialCasing.txt',
    '../data/UnicodeData.txt',
  ),
  'character.h': files(
    '../data/DerivedCoreProperties.txt',
    '../data/GraphemeBreakProperty.txt',
    '../data/emoji-data.txt',
  ),
  'character-test.h': files('../data/GraphemeBreakTest.txt'),
  'line.h': files(
    '../data/EastAsianWidth.txt',
    '../data/LineBreak.txt',
    '../data/emoji-data.txt',
  ),
  'line-test.h': files('../data/LineBreakTest.txt'),
  'sentence.h': files('../data/SentenceBreakProperty.txt'),
  'sentence-test.h': files('../data/SentenceBreakTest.txt'),
  'word.h': files('../data/WordBreakProperty.txt'),
  'word-test.h': files('../data/WordBreakTest.txt'),
}

gen_headers = []
foreach header, data_files : gen_headers_tgt
  exe_name = header.replace('.h', '')
  exe = executable(
    exe_name,
    [exe_name + '.c', 'util.c'],
    native: true,
    install: false,
  )
  gen = custom_target(
    header,
    output: header,
    depend_files: data_files,
    command: ['sh', '-c', 'cd $PROJECT_SOURCE_ROOT && exec "$@"', '-', exe],
    env: {
      'PROJECT_SOURCE_ROOT': meson.project_source_root(),
    },
    capture: true,
  )
  gen_headers += gen
endforeach
