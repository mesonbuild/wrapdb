gendir = include_directories('.')
gen_headers_tgt = {
  'bidirectional': files(
    '../data/BidiBrackets.txt',
    '../data/BidiMirroring.txt',
    '../data/DerivedBidiClass.txt',
    '../data/UnicodeData.txt',
  ),
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
  'line': files(
    '../data/EastAsianWidth.txt',
    '../data/LineBreak.txt',
    '../data/emoji-data.txt',
  ),
  'sentence': files('../data/SentenceBreakProperty.txt'),
  'word': files('../data/WordBreakProperty.txt'),
}

if get_option('test') or get_option('benchmark')
  gen_headers_tgt = gen_headers_tgt + {
    'bidirectional-test': files(
      '../data/BidiCharacterTest.txt',
      '../data/BidiTest.txt',
    ),
    'character-test': files('../data/GraphemeBreakTest.txt'),
    'line-test': files('../data/LineBreakTest.txt'),
    'sentence-test': files('../data/SentenceBreakTest.txt'),
    'word-test': files('../data/WordBreakTest.txt'),
  }
endif

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
    command: [chdir_wrapper, exe],
    env: {
      'PROJECT_SOURCE_ROOT': meson.project_source_root(),
    },
    capture: true,
  )
  gen_headers += gen
endforeach
