project('pcre', 'c')

cc = meson.get_compiler('c')

# put config.h in an internal directory so
# users don't include it by accident
subdir('internal')
conf_inc = include_directories('internal')

versiondata = configuration_data()
versiondata.set('PCRE_MAJOR', 8)
versiondata.set('PCRE_MINOR', 37)
versiondata.set('PCRE_PRERELEASE', '')
versiondata.set('PCRE_DATE', '2015-04-28')
configure_file(input : 'pcre.h.in',
  output : 'pcre.h',
  configuration : versiondata)


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

dftables = executable('dftables',
  'dftables.c',
  c_args : '-DHAVE_CONFIG_H',
  include_directories : conf_inc,
  # For cross-compilation this target needs to run on the build machine. It is
  # only used for the custom_target below. See:
  # http://mesonbuild.com/Cross-compilation.html#mixing-host-and-build-targets
  native : true,
)

char_tables = custom_target('chartables',
  output : 'pcre_chartables.c',
  command : [dftables, '@OUTPUT@'])

pcre8 = build_target('pcre',
  pcre8_sources, char_tables,
  c_args : '-DHAVE_CONFIG_H',
  target_type : libtype,
  include_directories : conf_inc)

pcre_posix = build_target('pcreposix',
  'pcreposix.c',
  c_args : '-DHAVE_CONFIG_H',
  target_type : libtype,
  include_directories : conf_inc)

pcretest = executable('pcretest',
  'pcretest.c', 'pcre_printint.c',
  c_args : '-DHAVE_CONFIG_H',
  link_with : [pcre8, pcre_posix],
  include_directories : conf_inc,
)
# Running test not added yet because it is
# complicated.

pcre_dep = declare_dependency(link_with : pcre8,
  include_directories : include_directories('.'),
)
