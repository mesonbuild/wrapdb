project(
  're2',
  'cpp',
  version: '20230301',
  license: 'BSD-3-Clause',
  default_options: [
    'cpp_std=c++14',
  ],
)

threads_dep = dependency('threads')

cpp = meson.get_compiler('cpp')

if cpp.get_argument_syntax() == 'msvc'
  cpp_args = [
    '/wd4100',
    '/wd4201',
    '/wd4456',
    '/wd4457',
    '/wd4702',
    '/wd4815',
  ]
  cpp_args = cpp.get_supported_arguments(cpp_args)
  add_project_arguments(cpp_args, language: 'cpp')
endif

if host_machine.system() == 'windows'
  cpp_args = [
    '-DUNICODE',
    '-D_UNICODE',
    '-DSTRICT',
    '-DNOMINMAX',
    '-D_CRT_SECURE_NO_WARNINGS',
    '-D_SCL_SECURE_NO_WARNINGS',
    '-DWINVER=0x0600',
    '-D_WIN32_WINNT=0x0600',
  ]
  add_project_arguments(cpp_args, language: 'cpp')
endif

sym_path_gnu = meson.current_source_dir() / 'libre2.symbols'
sym_path_darwin = meson.current_source_dir() / 'libre2.symbols.darwin'
ldflag_gnu = '-Wl,--version-script=' + sym_path_gnu
ldflag_darwin = '-Wl,-exported_symbols_list,' + sym_path_darwin
if cpp.links('', name: '-Wl,--version-script', args: ['-shared', ldflag_gnu])
  link_args = [ldflag_gnu]
  link_depends = [sym_path_gnu]
elif host_machine.system() == 'darwin' and cpp.has_link_argument(ldflag_darwin)
  link_args = [ldflag_darwin]
  link_depends = [sym_path_darwin]
else
  link_args = []
  link_depends = []
endif

re2_sources = files(
  're2/bitmap256.cc',
  're2/bitstate.cc',
  're2/compile.cc',
  're2/dfa.cc',
  're2/filtered_re2.cc',
  're2/mimics_pcre.cc',
  're2/nfa.cc',
  're2/onepass.cc',
  're2/parse.cc',
  're2/perl_groups.cc',
  're2/prefilter.cc',
  're2/prefilter_tree.cc',
  're2/prog.cc',
  're2/re2.cc',
  're2/regexp.cc',
  're2/set.cc',
  're2/simplify.cc',
  're2/stringpiece.cc',
  're2/tostring.cc',
  're2/unicode_casefold.cc',
  're2/unicode_groups.cc',
  'util/rune.cc',
  'util/strutil.cc',
)

# static library required by the tests to access re2 internals
libre2_static = static_library(
  '_re2',
  re2_sources,
  pic: true,
  dependencies: threads_dep,
  install: false,
)

libre2 = library(
  're2',
  link_whole: libre2_static,
  link_args: link_args,
  link_depends: link_depends,
  install: (cpp.get_id() != 'msvc'), # does not generate .lib file, cmake version exports all symbols, can't do that here
  soversion: '9',
  dependencies: threads_dep,
)

headers = files(
  're2/filtered_re2.h',
  're2/re2.h',
  're2/set.h',
  're2/stringpiece.h',
)

install_headers(
  headers,
  subdir: 're2',
)

includes = include_directories('.')
re2_dep = declare_dependency(
  link_with: libre2,
  include_directories: includes,
)

re2testing_sources = files(
  're2/testing/backtrack.cc',
  're2/testing/dump.cc',
  're2/testing/exhaustive_tester.cc',
  're2/testing/null_walker.cc',
  're2/testing/regexp_generator.cc',
  're2/testing/string_generator.cc',
  're2/testing/tester.cc',
  'util/pcre.cc',
  'util/test.cc',
)

# static library for test support code
libtest_static = static_library(
  '_re2_testing',
  re2testing_sources,
  install: false,
)

tests = [
  'charclass_test',
  'compile_test',
  'filtered_re2_test',
  'mimics_pcre_test',
  'parse_test',
  'possible_match_test',
  're2_test',
  're2_arg_test',
  'regexp_test',
  'required_prefix_test',
  'search_test',
  'set_test',
  'simplify_test',
  'string_generator_test',
]

foreach test : tests
  t = executable(
    test,
    're2/testing/@0@.cc'.format(test),
    link_with: [libre2_static, libtest_static],
    dependencies: threads_dep,
  )

  test(test, t)
endforeach

bigtests = [
  'dfa_test',
  'exhaustive1_test',
  'exhaustive2_test',
  'exhaustive3_test',
  'exhaustive_test',
  'random_test',
]

if get_option('bigtests')
  foreach test : bigtests
    t = executable(
      test,
      're2/testing/@0@.cc'.format(test),
      link_with: [libre2_static, libtest_static],
      dependencies: threads_dep,
    )

    test(test, t, timeout: 1800)
  endforeach
endif
