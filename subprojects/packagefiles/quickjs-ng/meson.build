project('quickjs-ng', 'c', version: '0.8.0', default_options: ['c_std=c11'])

cc = meson.get_compiler('c')
dep_m = cc.find_library('m', required: false)
dep_threads = dependency('threads')
deps = [dep_m, dep_threads]

msvc_compat = cc.get_id() == 'msvc' or cc.get_id() == 'clang-cl'

add_project_arguments(
  cc.get_supported_arguments(
    '-Wno-implicit-fallthrough',
    '-Wno-sign-compare',
    '-Wno-missing-field-initializers',
    '-Wno-unused-parameter',
    '-Wno-unused-but-set-variable',
    '-Wno-array-bounds',
    '-Wno-format-truncation',
    '-funsigned-char',
  ),
  language: 'c',
)

if msvc_compat
  add_project_arguments(
    cc.get_supported_arguments(
      '-Wno-unsafe-buffer-usage',
      '-Wno-sign-conversion',
      '-Wno-nonportable-system-include-path',
      '-Wno-implicit-int-conversion',
      '-Wno-shorten-64-to-32',
      '-Wno-reserved-macro-identifier',
      '-Wno-reserved-identifier',
      '-Wdeprecated-declarations',
      '/experimental:c11atomics',
    ),
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

c_defines = ['-D_GNU_SOURCE', '-DCONFIG_BIGNUM']

if host_machine.system() == 'windows'
  c_defines += ['-DWIN32_LEAN_AND_MEAN', '-D_WIN32_WINNT=0x0602']
endif

add_project_arguments(c_defines, language: 'c')

quickjs_lib = library(
  'quickjs',
  lib_src,
  dependencies: deps,
  include_directories: include_directories('.'),
)

quickjs_ng_dep = declare_dependency(
  include_directories: include_directories('include'),
  link_with: quickjs_lib,
  dependencies: deps,
)

if not meson.is_subproject()
  pkg = import('pkgconfig')
  pkg.generate(
    quickjs_ng_dep,
    description: 'QuickJS, the Next Generation: a mighty JavaScript engine',
    url: 'https://github.com/quickjs-ng/quickjs',
    version: meson.project_version(),
  )
endif


test('ctest', executable('ctest', 'ctest.c', dependencies: [quickjs_ng_dep]))
