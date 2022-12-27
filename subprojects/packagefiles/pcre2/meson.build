project(
  'pcre2',
  'c',
  license: 'BSD-3',
  meson_version: '>=0.49.0',
  version: '10.42',
)

cc = meson.get_compiler('c')

pcre2_h = configure_file(
  input: 'src/pcre2.h.generic',
  output: 'pcre2.h',
  copy: true,
)

chartables = configure_file(
  input: 'src/pcre2_chartables.c.dist',
  output: 'pcre2_chartables.c',
  copy: true,
)

sources = files(
  'src/pcre2_auto_possess.c',
  'src/pcre2_compile.c',
  'src/pcre2_config.c',
  'src/pcre2_context.c',
  'src/pcre2_convert.c',
  'src/pcre2_dfa_match.c',
  'src/pcre2_error.c',
  'src/pcre2_extuni.c',
  'src/pcre2_find_bracket.c',
  'src/pcre2_jit_compile.c',
  'src/pcre2_maketables.c',
  'src/pcre2_match.c',
  'src/pcre2_match_data.c',
  'src/pcre2_newline.c',
  'src/pcre2_ord2utf.c',
  'src/pcre2_pattern_info.c',
  'src/pcre2_script_run.c',
  'src/pcre2_serialize.c',
  'src/pcre2_string_utils.c',
  'src/pcre2_study.c',
  'src/pcre2_substitute.c',
  'src/pcre2_substring.c',
  'src/pcre2_tables.c',
  'src/pcre2_ucd.c',
  'src/pcre2_valid_utf.c',
  'src/pcre2_xclass.c',
)
sources += chartables

cdata = configuration_data()

check_headers = [
  'bzlib.h',
  'dirent.h',
  'dlfcn.h',
  'inttypes.h',
  'limits.h',
  'stdint.h',
  'stdio.h',
  'stdlib.h',
  'string.h',
  'strings.h',
  'sys/stat.h',
  'sys/types.h',
  'sys/wait.h',
  'wchar.h',
  'windows.h',
  'unistd.h',
  'zlib.h',
]

foreach h : check_headers
  if cc.has_header(h)
    cdata.set('HAVE_@0@'.format(h.underscorify().to_upper()), 1)
  endif
endforeach

check_funs = [
  'bcopy',
  'memfd_create',
  'memmove',
  'mkostemp',
  'realpath',
  'secure_getemv',
  'strerror',
]

foreach f : check_funs
  if cc.has_function(f)
    cdata.set('HAVE_@0@'.format(f.to_upper()), 1)
  endif
endforeach

if cc.compiles('char buf[128] __attribute__((uninitialized));')
  cdata.set('HAVE_ATTRIBUTE_UNINITIALIZED', 1)
endif

if cc.has_function_attribute('visibility')
  cdata.set('HAVE_VISIBILITY', 1)
endif

if cc.has_function_attribute('dllexport') and get_option('default_library') != 'static'
  export_define = '__declspec(dllexport) extern'
elif cc.has_argument('-fvisibility=hidden')
  export_define = 'extern __attribute__ ((visibility ("default")))'
else
  export_define = 'extern'
endif

cdata.set('PCRE2POSIX_EXP_DECL', export_define)
cdata.set('PCRE2_EXP_DECL', export_define)
cdata.set('PCRE2POSIX_EXP_DEFN', export_define)
cdata.set('PCRE2_EXP_DEFN', export_define)

cdata.set('HEAP_LIMIT', 20000000)
cdata.set('LINK_SIZE', 2)
cdata.set('MATCH_LIMIT', 10000000)
cdata.set('MATCH_LIMIT_DEPTH', 'MATCH_LIMIT')
cdata.set('MAX_NAME_COUNT', 10000)
cdata.set('MAX_NAME_SIZE', 32)
cdata.set('NEWLINE_DEFAULT', 2)
cdata.set('PARENS_NEST_LIMIT', 250)
cdata.set('PCRE2GREP_BUFSIZE', 20480)
cdata.set('PCRE2GREP_MAX_BUFSIZE', 1048576)

cdata.set('SUPPORT_PCRE2_8', '/**/')
cdata.set('SUPPORT_PCRE2_16', '/**/')
cdata.set('SUPPORT_PCRE2_32', '/**/')
cdata.set('SUPPORT_PCRE2GREP_CALLOUT', '/**/')
cdata.set('SUPPORT_PCRE2GREP_CALLOUT_FORK', '/**/')
cdata.set('SUPPORT_UNICODE', '/**/')

cdata.set_quoted('PACKAGE', meson.project_name())
cdata.set_quoted('PACKAGE_TARNAME', meson.project_name())
cdata.set_quoted('PACKAGE_NAME', meson.project_name().to_upper())
cdata.set_quoted('PACKAGE_VERSION', meson.project_version())
cdata.set_quoted('PACKAGE_STRING', '@0@ @1@'.format(meson.project_name().to_upper(), meson.project_version()))
cdata.set_quoted('PACKAGE_BUGREPORT', '')
cdata.set_quoted('PACKAGE_URL', '')
cdata.set_quoted('LT_OBJDIR', '.libs/')

config_h = configure_file(
  input: 'config.h.meson',
  output: 'config.h',
  configuration: cdata,
)

includes = include_directories('.', 'src')

pcre2_8_lib = library(
  'pcre2-8',
  sources,
  gnu_symbol_visibility: 'hidden',
  include_directories: includes,
  c_args: ['-DHAVE_CONFIG_H', '-DPCRE2_CODE_UNIT_WIDTH=8'],
  install: true,
)

libpcre2_8 = declare_dependency(
  link_with: pcre2_8_lib,
  include_directories: includes,
  compile_args: get_option('default_library') == 'static' ? '-DPCRE2_STATIC' : [],
)

pcre2_posix_lib = library(
  'pcre2-posix',
  'src/pcre2posix.c',
  gnu_symbol_visibility: 'hidden',
  dependencies: libpcre2_8,
  c_args: ['-DHAVE_CONFIG_H', '-DPCRE2_CODE_UNIT_WIDTH=8'],
  install: true,
)

libpcre2_posix = declare_dependency(
  link_with: pcre2_posix_lib,
  include_directories: includes,
  compile_args: get_option('default_library') == 'static' ? '-DPCRE2_STATIC' : [],
)

pcre2_16_lib = library(
  'pcre2-16',
  sources,
  gnu_symbol_visibility: 'hidden',
  include_directories: includes,
  c_args: ['-DHAVE_CONFIG_H', '-DPCRE2_CODE_UNIT_WIDTH=16'],
  install: true,
)

libpcre2_16 = declare_dependency(
  link_with: pcre2_16_lib,
  include_directories: includes,
  compile_args: get_option('default_library') == 'static' ? '-DPCRE2_STATIC' : [],
)

pcre2_32_lib = library(
  'pcre2-32',
  sources,
  gnu_symbol_visibility: 'hidden',
  include_directories: includes,
  c_args: ['-DHAVE_CONFIG_H', '-DPCRE2_CODE_UNIT_WIDTH=32'],
  install: true,
)

libpcre2_32 = declare_dependency(
  link_with: pcre2_32_lib,
  include_directories: includes,
  compile_args: get_option('default_library') == 'static' ? '-DPCRE2_STATIC' : [],
)

if get_option('grep')
  pcre2grep = executable(
    'pcre2grep',
    'src/pcre2grep.c',
    dependencies: libpcre2_8,
    c_args: '-DHAVE_CONFIG_H',
    install: true,
  )
endif

install_headers(pcre2_h, 'src/pcre2posix.h')

########### pkg-config #############

pkg = import('pkgconfig')

pkg.generate(
  pcre2_8_lib,
  name: 'libpcre2-8',
  description: 'PCRE2 - Perl compatible regular expressions C library (2nd API) with 8 bit character support',
  version: meson.project_version(),
)

pkg.generate(
  pcre2_16_lib,
  name: 'libpcre2-16',
  description: 'PCRE2 - Perl compatible regular expressions C library (2nd API) with 16 bit character support',
  version: meson.project_version(),
)

pkg.generate(
  pcre2_32_lib,
  name: 'libpcre2-32',
  description: 'PCRE2 - Perl compatible regular expressions C library (2nd API) with 32 bit character support',
  version: meson.project_version(),
)

#### tests

if (
  get_option('test')
  and not meson.is_cross_build() # wine wrappers are not bat-friendly, this would need better testing
)
  link_args = []
  if cc.get_argument_syntax() == 'msvc'
    link_args += '/STACK:2500000'
  endif

  pcre2test = executable(
    'pcre2test',
    'src/pcre2test.c',
    dependencies: [libpcre2_8, libpcre2_posix, libpcre2_16, libpcre2_32],
    c_args: '-DHAVE_CONFIG_H',
    link_args: link_args,
  )

  if cc.get_argument_syntax() == 'msvc'
    runtest = find_program('RunTest.bat')
    rungreptest = find_program('RunGrepTest.bat')
  else
    runtest = find_program('RunTest')
    rungreptest = find_program('RunGrepTest')
  endif

  test(
    'RunTest',
    runtest,
    should_fail: host_machine.system() == 'windows' and cc.get_argument_syntax() != 'msvc',
    env: 'srcdir=@0@'.format(meson.current_source_dir()),
    workdir: meson.current_build_dir(),
  )

  test(
    'RunGrepTest',
    rungreptest,
    should_fail: host_machine.system() == 'windows',
    env: 'srcdir=@0@'.format(meson.current_source_dir()),
    workdir: meson.current_build_dir(),
  )
endif
