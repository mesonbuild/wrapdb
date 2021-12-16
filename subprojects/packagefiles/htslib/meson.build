project(
  'htslib',
  'c',
  version : '1.14',
  default_options : [
    'buildtype=release',
    # -Wall produces way
    # too many warnings
    'warning_level=0',
    'c_std=c99',
    'b_ndebug=if-release'],
  license : 'MIT',
  meson_version : '>= 0.48.0')

# htslib uses
#   - usleep()
#   - strdup()
#   - M_LN10/M_LN2
add_project_arguments(
  '-D_XOPEN_SOURCE=600',
  language : 'c')

# libm (glibc)
cc = meson.get_compiler('c')
libm_dep = cc.find_library('m', required : false)

# pthreads
thread_dep = dependency('threads', required : false)

# zlib
zlib_dep = dependency('zlib', required : true, fallback : ['zlib', 'zlib_dep'])

htslib_incdir = include_directories('.', is_system : true)

htslib_sources = files([
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
  'htscodecs/htscodecs/arith_dynamic.c',
  'htscodecs/htscodecs/fqzcomp_qual.c',
  'htscodecs/htscodecs/htscodecs.c',
  'htscodecs/htscodecs/pack.c',
  'htscodecs/htscodecs/rANS_static4x16pr.c',
  'htscodecs/htscodecs/rANS_static.c',
  'htscodecs/htscodecs/rle.c',
  'htscodecs/htscodecs/tokenise_name3.c',
  'bcf_sr_sort.c',
  'bgzf.c',
  'errmod.c',
  'faidx.c',
  'header.c',
  'hfile.c',
  'hts.c',
  'hts_expr.c',
  'hts_os.c',
  'kfunc.c',
  'kstring.c',
  'md5.c',
  'multipart.c',
  'probaln.c',
  'realn.c',
  'regidx.c',
  'region.c',
  'sam.c',
  'synced_bcf_reader.c',
  'tbx.c',
  'textutils.c',
  'thread_pool.c',
  'vcf.c',
  'vcf_sweep.c',
  'vcfutils.c',
])

htslib_config_h_config = configuration_data()
htslib_config_h_config.set('HAVE_LIBZ', 1)
htslib_config_h = configure_file(
  output : 'config.h',
  configuration : htslib_config_h_config)

htslib_config_vars_h_config = configuration_data()
htslib_config_vars_h_config.set('HTS_CC', '""')
htslib_config_vars_h_config.set('HTS_CFLAGS', '""')
htslib_config_vars_h_config.set('HTS_LDFLAGS', '""')
htslib_config_vars_h_config.set('HTS_CPPFLAGS', '""')
htslib_config_vars_h = configure_file(
  output : 'config_vars.h',
  configuration : htslib_config_vars_h_config)

htslib_version_h_config = configuration_data()
htslib_version_h_config.set_quoted('HTS_VERSION_TEXT', meson.project_version())
htslib_version_h = configure_file(
  output : 'version.h',
  configuration : htslib_version_h_config)

# install library if
# - either running as a proper project
# - or linking to shared libraries
htslib_lib_install = (not meson.is_subproject()) or (get_option('default_library') != 'static')

htslib_lib = library(
  'hts', [
    htslib_config_h,
    htslib_config_vars_h,
    htslib_version_h,
    htslib_sources],
  soversion : 3,
  version : meson.project_version(),
  install : htslib_lib_install,
  dependencies : [
    libm_dep,
    thread_dep,
    zlib_dep],
  gnu_symbol_visibility : 'hidden',
  override_options : [
    'warning_level=0',
    'c_std=c99'])

###################
# dependency info #
###################

htslib_dep = declare_dependency(
  include_directories : htslib_incdir,
  link_with : htslib_lib,
  version : meson.project_version())

#########
# tests #
#########

if get_option('tests')
  htslib_source_root = meson.current_source_dir()
  subdir('test')
endif
