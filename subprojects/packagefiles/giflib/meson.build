project(
  'giflib',
  'c',
  version: '5.2.2',
  default_options: [
    meson.version().version_compare('>=1.3.0') ? 'c_std=gnu99,c99' : 'c_std=gnu99',
  ],
  meson_version: '>=0.59.0',
)

cc = meson.get_compiler('c')
cc_is_msvc = cc.get_id() in ['clang-cl', 'msvc']
fs = import('fs')

enable_progs = get_option('progs').allowed()

enable_tests = get_option('tests')
sh = find_program(
  'sh',
  required: enable_tests,
)
enable_tests = enable_tests.require(sh.found())
foreach _name : ['cmp', 'diff', 'head']
  _prog = find_program(
    _name,
    required: enable_tests,
  ).found()
  enable_tests = enable_tests.require(_prog)
endforeach
enable_tests = enable_tests.allowed()

add_project_arguments(
  cc.get_supported_arguments('-Wno-format-truncation'),
  language: 'c',
)

foreach _hdr : ['limits.h', 'fcntl.h', 'stdint.h', 'stdarg.h']
  cc.has_header(
    _hdr,
    required: true,
  )
endforeach

# No `strtok_r` when building with MSVC, use `strtok_s` instead.
if (host_machine.system() == 'windows'
and not cc.has_header_symbol('string.h', 'strtok_r')
and cc.has_header_symbol('string.h', 'strtok_s')
)
  add_project_arguments(
    '-Dstrtok_r=strtok_s',
    language: 'c',
  )
endif

gif_lib = library(
  'gif',
  [
    'dgif_lib.c',
    'egif_lib.c',
    'gif_err.c',
    'gif_font.c',
    'gif_hash.c',
    'gifalloc.c',
    'openbsd-reallocarray.c',
    'quantize.c',
  ],
  install: true,
  version: '7.2.0',
  vs_module_defs: 'giflib.def',
)

gif_dep = declare_dependency(
  include_directories: include_directories('.'),
  link_with: gif_lib,
)

meson.override_dependency('giflib', gif_dep)

install_headers('gif_lib.h')

if enable_progs or enable_tests

  m_dep = cc.find_library(
    'm',
    required: false,
  )

  util_lib = static_library('util', ['getarg.c', 'qprintf.c', 'quantize.c'])

  # NOTE: `gifcolor` & `gifecho` are not built on Windows
  # when using Visual Studio because of an issue exporting
  # `GifAsciiTable8x8` (required) in the def file.
  _programs = [
    # name        build?                           install?
    ['gif2rgb'  , true, enable_progs],
    ['gifbg'    , enable_progs, false],
    ['gifbuild' , true, enable_progs],
    ['gifclrmp' , true, enable_progs],
    ['gifcolor' , enable_progs and not cc_is_msvc, false],
    ['gifecho'  , not cc_is_msvc, false],
    ['giffilter', true, false],
    ['giffix'   , true, enable_progs],
    ['gifhisto' , enable_progs, false],
    ['gifinto'  , true, false],
    ['gifsponge', true, false],
    ['giftext'  , true, enable_progs],
    ['gifwedge' , true, false],
  ]

  if cc.has_header('getopt.h')
    _programs += [['giftool', true, enable_progs]]
    giftool_tests = [
      [
        'copy'       ,
        ''      ,
        'pic/gifgrid.gif'            ,
        'tests/gifgrid.rgb',
      ],
      [
        'deinterlace',
        '-i on' ,
        'pic/treescap-interlaced.gif',
        'tests/treescap.rgb',
      ],
      [
        'interlace'  ,
        '-i off',
        'pic/treescap.gif'           ,
        'tests/treescap-interlaced.rgb',
      ],
    ]
  else
    giftool_tests = []
  endif

  foreach _spec : _programs
    _name = _spec[0]
    _build = _spec[1]
    _install = _spec[2]
    if _build
      _exe = executable(
        _name,
        _name + '.c',
        dependencies: [gif_dep, m_dep],
        install: _install,
        link_with: util_lib,
      )
      set_variable(_name, _exe)
    endif
  endforeach

endif

if enable_tests

  gifs = [
    'fire.gif',
    'gifgrid.gif',
    'porsche.gif',
    'solid2.gif',
    'treescap-interlaced.gif',
    'treescap.gif',
    'welcome2.gif',
    'x-trans.gif',
  ]

  # Test gif2rgb.
  foreach _gif : gifs
    _stem = _gif.substring(0, -4)
    test(
      _gif,
      sh,
      args: [
        '-xc',
        '"$1" -1 -o "$2" "$3" && cmp "$4" "$2"',
        '--',
        gif2rgb,
        'gif2rgb-@0@.regress'.format(_stem),
        files('pic' / _gif),
        files('tests' / (_stem + '.rgb')),
      ],
      suite: 'gif2rgb',
    )
  endforeach

  # Test gifbuild.
  test(
    'basic',
    sh,
    args: [
      '-xc',
      ' && '.join(
        '"$1" -d <"$2" >"$3"',
        'diff --strip-trailing-cr --unified "$4" "$3"',
      ),
      '--',
      gifbuild,
      files('pic/treescap.gif'),
      'gifbuild-treescap.ico',
      files('tests/treescap.ico'),
    ],
    suite: 'gifbuild',
  )
  test(
    'idempotency-icon',
    sh,
    args: [
      '-xc',
      ' && '.join(
        '"$1" <"$2" | "$1" -d >"$3"',
        '"$1" <"$3" | "$1" -d >"$4"',
        'diff --strip-trailing-cr --unified "$3" "$4"',
      ),
      '--',
      gifbuild,
      files('pic/sample.ico'),
      'gifbuild-sample1.ico',
      'gifbuild-sample2.ico',
    ],
    suite: 'gifbuild',
  )
  test(
    'idempotency-animation',
    sh,
    args: [
      '-xc',
      ' && '.join(
        '"$1" -d <"$2" >"$3"',
        '"$1" <"$3" >"$4"',
        '"$1" -d <"$4" >"$5"',
        'diff --strip-trailing-cr --unified "$3" "$5"',
      ),
      '--',
      gifbuild,
      files('pic/fire.gif'),
      'gifbuild-fire1.ico',
      'gifbuild-fire2.gif',
      'gifbuild-fire3.ico',
    ],
    suite: 'gifbuild',
  )

  # Test gifclrmp, giftext.
  foreach _suite, _ext : {
    'gifclrmp': '.map',
    'giftext' : '.dmp',
  }
    _prog = get_variable(_suite)
    foreach _gif : gifs
      _stem = _gif.substring(0, -4)
      test(
        _gif,
        sh,
        args: [
          '-xc',
          ' && '.join(
            '"$1" <"$2" >"$3"',
            'diff --strip-trailing-cr --unified "$4" "$3"',
          ),
          '--',
          _prog,
          files('pic' / _gif),
          '@0@-@1@.regress'.format(_suite, _stem),
          files('tests' / (_stem + _ext)),
        ],
        suite: _suite,
      )
    endforeach
  endforeach

  # Test giffilter, gifsponge.
  foreach _suite : ['giffilter', 'gifsponge']
    _prog = get_variable(_suite)
    foreach _gif : gifs
      _stem = _gif.substring(0, -4)
      test(
        _gif,
        sh,
        args: [
          '-xc',
          '"$1" <"$2" | "$3" >"$4" && cmp "$5" "$4"',
          '--',
          _prog,
          files('pic' / _gif),
          gif2rgb,
          '@0@-@1@.regress'.format(_suite, _stem),
          files('tests' / (_stem + '.rgb')),
        ],
        suite: _suite,
      )
    endforeach
  endforeach

  # Test gifecho.
  if not cc_is_msvc
    test(
      'regress',
      sh,
      args: [
        '-xc',
        ' && '.join(
          '"$1" -t foobar | "$2" -d >"$3"',
          'diff --strip-trailing-cr --unified "$4" "$3"',
        ),
        '--',
        gifecho,
        gifbuild,
        'gifecho-foobar.ico',
        files('tests/foobar.ico'),
      ],
      suite: 'gifecho',
    )
  endif

  # Test giffix.
  test(
    'regress',
    sh,
    args: [
      '-xc',
      ' && '.join(
        'head -c "$1" <"$2" | "$3" | "$4" -d >"$5"',
        'diff --strip-trailing-cr --unified "$6" "$5"',
      ),
      '--',
      (fs.size('pic/treescap.gif') - 20).to_string(),
      files('pic/treescap.gif'),
      giffix,
      gifbuild,
      'giffix-giffixed.ico',
      files('tests/giffixed.ico'),
    ],
    suite: 'giffix',
  )

  # Test gifinto.
  test(
    'regress',
    sh,
    args: [
      '-xc',
      ' && '.join(
        'rm -f gifinto.tmp',
        # Should create `gifinto.tmp`.
        '"$1" <"$2" gifinto.tmp',
        '[ -f gifinto.tmp ]',
        'rm -f gifinto.tmp',
        # Should not create `gifinto.tmp`.
        'echo 0123456789 | "$1" gifinto.tmp',
        '! [ -f gifinto.tmp ]',
      ),
      '--',
      gifinto,
      files('pic/porsche.gif'),
      files('tests/giffixed.ico'),
    ],
    suite: 'gifinto',
  )

  # Test giftool.
  foreach _spec : giftool_tests
    _name = _spec[0]
    _input_flags = _spec[1]
    _input_file = _spec[2]
    _expected_output = _spec[3]
    test(
      _name,
      sh,
      args: [
        '-xc',
        '"$1" $2 <"$3" | "$4" | cmp "$5" -',
        '--',
        giftool,
        _input_flags,
        files(_input_file),
        gif2rgb,
        files(_expected_output),
      ],
      suite: 'giftool',
    )
  endforeach

  # Test gifwedge.
  test(
    'regress',
    sh,
    args: ['-xc', '"$1" | cmp "$2" -', '--', gifwedge, files('tests/wedge.gif')],
    suite: 'gifwedge',
  )

endif
