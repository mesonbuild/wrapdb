project(
  'htslib',
  'c',
  version: '1.22',
  default_options: ['warning_level=0', 'c_std=c99', 'b_ndebug=if-release'],
  license: 'MIT',
  meson_version: '>= 0.50.0',
)

cc = meson.get_compiler('c')
if cc.get_argument_syntax() == 'msvc'
  error('MSVC is unsupported. Only MinGW.')
endif

# htslib uses
#   - usleep()
#   - strdup()
#   - M_LN10/M_LN2
add_project_arguments(
  '-D_XOPEN_SOURCE=600',
  language: 'c',
)

if meson.version().version_compare('>= 0.62')
  dl_dep = dependency('dl')
else
  dl_dep = cc.find_library('dl')
endif
libm_dep = cc.find_library(
  'm',
  required: false,
)
regex_dep = dependency(
  'regex',
  required: host_machine.system() == 'windows',
)
thread_dep = dependency('threads')
ws_dep = cc.find_library(
  'ws2_32',
  required: host_machine.system() == 'windows',
)
zlib_dep = dependency('zlib')

htslib_sources = files(
  'bcf_sr_sort.c',
  'bgzf.c',
  'cram/cram_codecs.c',
  'cram/cram_decode.c',
  'cram/cram_encode.c',
  'cram/cram_external.c',
  'cram/cram_index.c',
  'cram/cram_io.c',
  'cram/cram_stats.c',
  'cram/mFILE.c',
  'cram/open_trace_file.c',
  'cram/pooled_alloc.c',
  'cram/string_alloc.c',
  'errmod.c',
  'faidx.c',
  'header.c',
  'hfile.c',
  'hts.c',
  'hts_expr.c',
  'hts_os.c',
  'htscodecs/htscodecs/arith_dynamic.c',
  'htscodecs/htscodecs/fqzcomp_qual.c',
  'htscodecs/htscodecs/htscodecs.c',
  'htscodecs/htscodecs/pack.c',
  'htscodecs/htscodecs/rANS_static.c',
  'htscodecs/htscodecs/rANS_static32x16pr.c',
  'htscodecs/htscodecs/rANS_static4x16pr.c',
  'htscodecs/htscodecs/rle.c',
  'htscodecs/htscodecs/tokenise_name3.c',
  'htscodecs/htscodecs/utils.c',
  'kfunc.c',
  'kstring.c',
  'md5.c',
  'multipart.c',
  'plugin.c',
  'probaln.c',
  'realn.c',
  'regidx.c',
  'region.c',
  'sam.c',
  'sam_mods.c',
  'synced_bcf_reader.c',
  'tbx.c',
  'textutils.c',
  'thread_pool.c',
  'vcf.c',
  'vcf_sweep.c',
  'vcfutils.c',
)

if host_machine.cpu_family() in ['arm', 'aarch64'] and cc.get_define('__thumb__') != '1'
  htslib_sources += files('htscodecs/htscodecs/rANS_static32x16pr_neon.c')
endif

htslib_config_h_config = configuration_data()
htslib_config_h_config.set('HAVE_LIBZ', zlib_dep.found())
if host_machine.system() == 'cygwin'
  htslib_config_h_config.set_quoted('PLUGIN_EXT', '.cygdll')
elif host_machine.system() == 'darwin'
  htslib_config_h_config.set_quoted('PLUGIN_EXT', '.bundle')
elif host_machine.system() == 'windows'
  htslib_config_h_config.set_quoted('PLUGIN_EXT', '.dll')
else
  htslib_config_h_config.set_quoted('PLUGIN_EXT', '.so')
endif

configure_file(
  output: 'config.h',
  configuration: htslib_config_h_config,
)

htslib_config_vars_h_config = configuration_data()
htslib_config_vars_h_config.set('HTS_CC', '""')
htslib_config_vars_h_config.set('HTS_CFLAGS', '""')
htslib_config_vars_h_config.set('HTS_LDFLAGS', '""')
htslib_config_vars_h_config.set('HTS_CPPFLAGS', '""')
configure_file(
  output: 'config_vars.h',
  configuration: htslib_config_vars_h_config,
)

htslib_version_h_config = configuration_data()
htslib_version_h_config.set_quoted('HTS_VERSION_TEXT', meson.project_version())
configure_file(
  output: 'version.h',
  configuration: htslib_version_h_config,
)

# install library if
# - either running as a proper project
# - or linking to shared libraries
htslib_lib_install = (not meson.is_subproject()) or (get_option(
  'default_library',
) != 'static')

htslib_lib = library(
  'hts',
  htslib_sources,
  soversion: 3,
  version: meson.project_version(),
  install: htslib_lib_install,
  dependencies: [dl_dep, libm_dep, regex_dep, thread_dep, ws_dep, zlib_dep],
  gnu_symbol_visibility: 'hidden',
  override_options: ['warning_level=0', 'c_std=c99'],
)

###################
# dependency info #
###################

htslib_dep = declare_dependency(
  include_directories: '.',
  link_with: htslib_lib,
  version: meson.project_version(),
)

#########
# tests #
#########

if get_option('tests')
  htslib_source_root = meson.current_source_dir()
  subdir('test')
endif
