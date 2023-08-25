unibreak_lib = library(
  'unibreak',
  [
    'emojidef.c',
    'graphemebreak.c',
    'linebreak.c',
    'linebreakdata.c',
    'linebreakdef.c',
    'unibreakbase.c',
    'unibreakdef.c',
    'wordbreak.c',
  ],
  install: true,
  version: '5.0.1',
  vs_module_defs: 'unibreak.def',
)

unibreak_dep = declare_dependency(
  include_directories: include_directories('.'),
  link_with: unibreak_lib,
)

meson.override_dependency('libunibreak', unibreak_dep)

pkg.generate(
  unibreak_lib,
  description: 'Library to implement Unicode algorithms for line and word breaking',
  name: 'libunibreak',
)

install_headers(
  'graphemebreak.h',
  'linebreak.h',
  'linebreakdef.h',
  'unibreakbase.h',
  'unibreakdef.h',
  'wordbreak.h',
)

# Tests. {{{

curl = find_program('curl', required: get_option('tests'))

if get_option('tests').require(curl.found()).allowed()

  tests_exe = executable(
    'tests',
    'tests.c',
    dependencies: unibreak_dep,
  )

  foreach _test, _data : {
    'line'    : 'LineBreakTest.txt',
    'word'    : 'WordBreakTest.txt',
    'grapheme': 'GraphemeBreakTest.txt',
  }
    _data = custom_target(
      _data,
      command: [
        curl,
        '--continue-at', '-',
        '--output', '@OUTPUT@',
        'http://www.unicode.org/Public/UNIDATA/auxiliary/' + _data,
      ],
      console: true,
      output: _data,
    )
    test(
      _test,
      tests_exe,
      args: _test,
      depends: _data,
      workdir: meson.current_build_dir(),
    )
  endforeach

endif

# }}}
