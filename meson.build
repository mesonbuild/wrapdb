project(
  'htslib',
  'c',
  version : '1.11',
  default_options : [
    'buildtype=release',
    # -Wall produces way
    # too many warnings
    'warning_level=0',
    'c_std=c99',
    'b_ndebug=if-release'],
  license : 'MIT',
  meson_version : '>= 0.46.0')

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
  'cram/cram_samtools.c',
  'cram/cram_stats.c',
  'cram/mFILE.c',
  'cram/open_trace_file.c',
  'cram/pooled_alloc.c',
  'cram/rANS_static.c',
  'cram/string_alloc.c',
  'bcf_sr_sort.c',
  'bgzf.c',
  'errmod.c',
  'faidx.c',
  'hfile.c',
  'header.c',
  'hfile_net.c',
  'hts.c',
  'hts_os.c',
  'kfunc.c',
  'knetfile.c',
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
    htslib_version_h,
    htslib_sources],
  soversion : 3,
  version : meson.project_version(),
  install : htslib_lib_install,
  dependencies : [
    libm_dep,
    thread_dep,
    zlib_dep],
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
