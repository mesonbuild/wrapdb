project(
  'htslib',
  'c',
  version: '1.22.1',
  license: 'MIT',
  meson_version: '>= 0.54.0',
)

cc = meson.get_compiler('c')
if cc.get_argument_syntax() == 'msvc'
  error('MSVC is unsupported. Only MinGW.')
endif

thread_dep = dependency('threads')
zlib_dep = dependency('zlib')

if meson.version().version_compare('>= 0.62')
  dl_dep = dependency('dl')
else
  dl_dep = cc.find_library('dl')
endif

if cc.links('#include <math.h>\nint main(){log(0);}')
  libm_dep = declare_dependency()
else
  libm_dep = cc.find_library('m')
endif

if cc.links('#include <regex.h>\nint main(){regfree(0);}')
  regex_dep = declare_dependency()
else
  regex_dep = dependency('regex')
endif

if host_machine.system() == 'windows'
  ws_dep = cc.find_library('ws2_32')
else
  if cc.has_function('recv')
    ws_dep = declare_dependency()
  else
    ws_dep = cc.find_library('socket')
  endif
endif

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

htslib_lib = library(
  'hts',
  htslib_sources,
  c_args: '-D_XOPEN_SOURCE=600',
  soversion: 3,
  version: meson.project_version(),
  install: true,
  dependencies: [dl_dep, libm_dep, regex_dep, thread_dep, ws_dep, zlib_dep],
  gnu_symbol_visibility: 'hidden',
  override_options: 'c_std=c99',
)

pc = import('pkgconfig')
pc.generate(
  htslib_lib,
  name: 'htslib',
  description: 'C library for high-throughput sequencing data format',
)

###################
# dependency info #
###################

htslib_dep = declare_dependency(
  include_directories: '.',
  link_with: htslib_lib,
)

meson.override_dependency('htslib', htslib_dep)

subdir('htslib')

foreach e : ['annot-tsv', 'bgzip', 'htsfile', 'tabix']
  executable(
    e,
    '@0@.c'.format(e),
    dependencies: htslib_dep,
    install: true,
  )
endforeach

subdir('ref_cache')

#mangix/usr/local/bin/ref-cache

#########
# tests #
#########

htslib_source_root = meson.current_source_dir()
subdir('test')
