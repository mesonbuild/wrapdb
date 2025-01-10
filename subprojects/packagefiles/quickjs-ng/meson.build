project('quickjs-ng', 'c', version: '0.8.0', default_options: ['c_std=c11'])

cc = meson.get_compiler('c')
dep_m = cc.find_library('m', required: false)
dep_threads = dependency('threads')
deps = [dep_m, dep_threads, dependency('dl')]

add_project_arguments(
  cc.get_supported_arguments('-Wall', '-D_CRT_SECURE_NO_WARNINGS'),
  language: 'c',
)


if cc.get_id() != 'msvc'
  add_project_arguments(
    cc.get_supported_arguments('-Wall', '-Wextra'),
    language: 'c',
  )
endif

add_project_arguments(
  cc.get_supported_arguments('-Wno-implicit-fallthrough'),
  language: 'c',
)
add_project_arguments(
  cc.get_supported_arguments('-Wno-sign-compare'),
  language: 'c',
)
add_project_arguments(
  cc.get_supported_arguments('-Wno-missing-field-initializers'),
  language: 'c',
)
add_project_arguments(
  cc.get_supported_arguments('-Wno-unused-parameter'),
  language: 'c',
)
add_project_arguments(
  cc.get_supported_arguments('-Wno-unused-but-set-variable'),
  language: 'c',
)
add_project_arguments(
  cc.get_supported_arguments('-Wno-array-bounds'),
  language: 'c',
)
add_project_arguments(
  cc.get_supported_arguments('-Wno-format-truncation'),
  language: 'c',
)
add_project_arguments(
  cc.get_supported_arguments('-funsigned-char'),
  language: 'c',
)

if cc.get_id() == 'msvc'
  add_project_arguments(
    cc.get_supported_arguments('-Wno-unsafe-buffer-usage'),
    language: 'c',
  )
  add_project_arguments(
    cc.get_supported_arguments('-Wno-sign-conversion'),
    language: 'c',
  )
  add_project_arguments(
    cc.get_supported_arguments('-Wno-nonportable-system-include-path'),
    language: 'c',
  )
  add_project_arguments(
    cc.get_supported_arguments('-Wno-implicit-int-conversion'),
    language: 'c',
  )
  add_project_arguments(
    cc.get_supported_arguments('-Wno-shorten-64-to-32'),
    language: 'c',
  )
  add_project_arguments(
    cc.get_supported_arguments('-Wno-reserved-macro-identifier'),
    language: 'c',
  )
  add_project_arguments(
    cc.get_supported_arguments('-Wno-reserved-identifier'),
    language: 'c',
  )
  add_project_arguments(
    cc.get_supported_arguments('-Wdeprecated-declarations'),
    language: 'c',
  )
  add_project_arguments(
    cc.get_supported_arguments('/experimental:c11atomics'),
    language: 'c',
  )
  add_project_arguments(
    cc.get_supported_arguments(
      '/wd4018',  # -Wno-sign-conversion
      '/wd4061',  # -Wno-implicit-fallthrough
      '/wd4100',  # -Wno-unused-parameter
      '/wd4200',  # -Wno-zero-length-array
      '/wd4242',  # -Wno-shorten-64-to-32
      '/wd4244',  # -Wno-shorten-64-to-32
      '/wd4245',  # -Wno-sign-compare
      '/wd4267',  # -Wno-shorten-64-to-32
      '/wd4388',  # -Wno-sign-compare
      '/wd4389',  # -Wno-sign-compare
      '/wd4710',  # Function not inlined
      '/wd4711',  # Function was inlined
      '/wd4820',  # Padding added after construct
      '/wd4996',  # -Wdeprecated-declarations
      '/wd5045',  # Compiler will insert Spectre mitigation for memory load if /Qspectre switch specified
    ),
    language: 'c',
  )

endif

if get_option('buildtype') == 'debug'
  add_project_arguments(
    cc.get_supported_arguments('-ggdb', '-fno-omit-frame-pointer'),
    language: 'c',
  )
endif

lib_src = files(
  'cutils.c',
  'libbf.c',
  'libregexp.c',
  'libunicode.c',
  'quickjs-libc.c',
  'quickjs.c',
)

# TODO: support shared libs
c_defines = ['-funsigned-char', '-D_GNU_SOURCE', '-DCONFIG_BIGNUM']

if host_machine.system() == 'windows'
  c_defines += ['-DWIN32_LEAN_AND_MEAN', '-D_WIN32_WINNT=0x0602']
endif

add_project_arguments(c_defines, language: 'c')

qjsc = executable('qjsc', 'qjsc.c', lib_src, dependencies: deps)

repl_c = custom_target(
  'repl_c',
  input: 'repl.js',
  output: 'repl.c',
  command: [qjsc, '-c', '-o', '@OUTPUT@', '-m', '@INPUT@'],
)

quickjs_lib = static_library('quickjs', lib_src, dependencies: deps)

qjs = executable(
  'qjs',
  'qjs.c',
  'gen/standalone.c',
  repl_c,
  link_with: [quickjs_lib],
  dependencies: deps,
)



quickjs_ng_dep = declare_dependency(
  include_directories: include_directories('.'),
  link_with: quickjs_lib,
  dependencies: deps,
)


# TODO: run tests
