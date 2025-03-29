project('pcre', 'c')

libedit_dep = dependency(
  'libedit',
  required: get_option('libedit'),
)
readline_dep = dependency(
  'readline',
  required: get_option('libreadline'),
)

cc = meson.get_compiler('c')
native_cc = meson.get_compiler(
  'c',
  native: true,
)

compile_args = ['-DHAVE_CONFIG_H']
if cc.get_id() == 'msvc'
  compile_args += ['-D_CRT_SECURE_NO_WARNINGS']
  compile_args += cc.get_supported_arguments(
    [
      '/wd4244',  # 'conversion' conversion from 'type1' to 'type2', possible loss of data
      '/wd4267',  # 'var' : conversion from 'size_t' to 'type', possible loss of data
      '/wd4701',  # Potentially uninitialized local variable 'name' used
      '/wd4703',  # Potentially uninitialized local pointer variable 'name' used
    ],
  )
else
  compile_args += cc.get_supported_arguments(
    [
      '-Wno-int-in-bool-context',
      '-Wno-implicit-fallthrough',
      '-Wno-array-bounds',
    ],
  )
endif

native_compile_args = ['-DHAVE_CONFIG_H']
if native_cc.get_id() == 'msvc'
  native_compile_args += ['-D_CRT_SECURE_NO_WARNINGS']
  native_compile_args += native_cc.get_supported_arguments(
    [
      '/wd4244',  # 'conversion' conversion from 'type1' to 'type2', possible loss of data
    ],
  )
endif

cdata = configuration_data()

check_headers = [
  'dirent.h',
  'inttypes.h',
  'stdint.h',
  'sys/stat.h',
  'sys/types.h',
  'unistd.h',
  'windows.h',
]

foreach h : check_headers
  cdata.set('HAVE_@0@'.format(h.underscorify().to_upper()), cc.has_header(h))
endforeach

check_functions = [
  'bcopy',
  'memmove',
  'strerror',
  'strtoimax',
  'strtoll',
  'strtoq',
  '_strtoi64',
]

foreach f : check_functions
  cdata.set('HAVE_@0@'.format(f.underscorify().to_upper()), cc.has_function(f))
endforeach

foreach t : ['long long', 'unsigned long long']
  cdata.set('HAVE_@0@'.format(t.underscorify().to_upper()), cc.has_type(t))
endforeach

if cc.get_argument_syntax() == 'msvc'
  # FIXME: Build of DLL is currently broken
  libtype = 'static_library'
  pcre_static = true
else
  libtype = 'library'
  pcre_static = get_option('default_library') == 'static'
endif

cdata.set('NEWLINE', 10)  # Currently unix only.
cdata.set('PCREGREP_BUFSIZE', 20480)
cdata.set('PCRE_LINK_SIZE', 2)
cdata.set('PCRE_MATCH_LIMIT', 10000000)
cdata.set('PCRE_MATCH_LIMIT_RECURSION', 'MATCH_LIMIT')
cdata.set('PCRE_PARENS_NEST_LIMIT', 250)
cdata.set('PCRE_POSIX_MALLOC_THRESHOLD', 10)
cdata.set('PCRE_STATIC', pcre_static)

cdata.set('SUPPORT_PCRE8', true)
cdata.set('SUPPORT_PCRE16', false)
cdata.set('SUPPORT_PCRE32', false)
cdata.set('SUPPORT_JIT', true)
cdata.set('SUPPORT_PCREGREP_JIT', true)
cdata.set('SUPPORT_UTF', true)
cdata.set('SUPPORT_UCP', true)
cdata.set('EBCDIC', false)
cdata.set('EBCDIC_NL25', false)
cdata.set('BSR_ANYCRLF', false)
cdata.set('NO_RECURSE', false)

cdata.set('SUPPORT_LIBBZ2', false)
cdata.set('SUPPORT_LIBZ', false)
cdata.set('SUPPORT_LIBEDIT', libedit_dep.found())
cdata.set('SUPPORT_LIBREADLINE', readline_dep.found())

cdata.set('SUPPORT_VALGRIND', false)
cdata.set('SUPPORT_GCOV', false)

cfile = configure_file(
  input: 'config-cmake.h.in',
  output: 'config.h',
  format: 'cmake@',
  configuration: cdata,
)

versiondata = configuration_data()
versiondata.set('PCRE_MAJOR', 8)
versiondata.set('PCRE_MINOR', 37)
versiondata.set('PCRE_PRERELEASE', '')
versiondata.set('PCRE_DATE', '2015-04-28')
configure_file(
  input: 'pcre.h.in',
  output: 'pcre.h',
  configuration: versiondata,
)

if libedit_dep.found()
  add_project_arguments(
    '-DHAVE_EDITLINE_READLINE_H',
    language: 'c',
  )
endif

pcre8_sources = [
  'pcre_byte_order.c',
  'pcre_compile.c',
  'pcre_config.c',
  'pcre_dfa_exec.c',
  'pcre_exec.c',
  'pcre_fullinfo.c',
  'pcre_get.c',
  'pcre_globals.c',
  'pcre_jit_compile.c',
  'pcre_maketables.c',
  'pcre_newline.c',
  'pcre_ord2utf8.c',
  'pcre_refcount.c',
  'pcre_string_utils.c',
  'pcre_study.c',
  'pcre_tables.c',
  'pcre_ucd.c',
  'pcre_valid_utf8.c',
  'pcre_version.c',
  'pcre_xclass.c',
]

dftables = executable(
  'dftables',
  'dftables.c',
  c_args: native_compile_args,
  # For cross-compilation this target needs to run on the build machine. It is
  # only used for the custom_target below. See:
  # http://mesonbuild.com/Cross-compilation.html#mixing-host-and-build-targets
  native: true,
)

char_tables = custom_target(
  'chartables',
  output: 'pcre_chartables.c',
  command: [dftables, '@OUTPUT@'],
)

pcre8 = build_target(
  'pcre',
  pcre8_sources,
  char_tables,
  target_type: libtype,
  c_args: compile_args,
)

pcre_posix = build_target(
  'pcreposix',
  'pcreposix.c',
  c_args: compile_args,
  target_type: libtype,
  link_with: pcre8,
)

pcretest = executable(
  'pcretest',
  'pcretest.c',
  'pcre_printint.c',
  c_args: compile_args,
  dependencies: [libedit_dep, readline_dep],
  link_with: [pcre8, pcre_posix],
)
# Running test not added yet because it is
# complicated.

pcre_dep = declare_dependency(
  link_with: pcre8,
  include_directories: include_directories('.'),
)
