project('libsndfile', 'c',
  version : '1.1.0',
  default_options : 'warning_level=3',
)

cc = meson.get_compiler('c')

cdata = configuration_data()
cdata.set('CPACK_PACKAGE_VERSION_FULL', meson.project_version())
cdata.set('INLINE_CODE', '')
cdata.set('PACKAGE_NAME', meson.project_name())
cdata.set('PROJECT_VERSION', meson.project_version())
cdata.set('PACKAGE_URL', 'https://github.com/libsndfile/libsndfile')
cdata.set('PACKAGE_BUGREPORT', 'https://github.com/libsndfile/libsndfile/issues')
cdata.set10('COMPILER_IS_GCC', cc.get_argument_syntax() == 'gcc')
cdata.set10('WORDS_BIGENDIAN', host_machine.endian() == 'big')
cdata.set10('CPU_IS_BIG_ENDIAN', host_machine.endian() == 'big')
cdata.set10('CPU_IS_LITTLE_ENDIAN', host_machine.endian() == 'little')
cdata.set10('_MINIX', host_machine.system() == 'minix')
cdata.set10('OSX_DARWIN_VERSION', host_machine.system() == 'macos')
cdata.set10('OS_IS_OPENBSD', host_machine.system() == 'openbsd')
cdata.set10('OS_IS_WIN32', host_machine.system() == 'windows')
cdata.set10('USE_WINDOWS_API', host_machine.system() == 'windows')
cdata.set10('WIN32_TARGET_DLL', host_machine.system() == 'windows' and get_option('buildtype') != 'static')

# code errors if this is not 8
cdata.set('SIZEOF_SF_COUNT_T_CODE', '#define SIZEOF_SF_COUNT_T 8')

#cdata.set('INLINE_CODE', '')

libm_dep = cc.find_library('m', required: false)
cdata.set10('HAVE_LIBM', libm_dep.found())
mp3_dep = dependency('libmpg123', required: get_option('mpeg'))
mp3lame_dep = cc.find_library('mp3lame', required: get_option('mpeg'))
cdata.set10('HAVE_MPEG', mp3_dep.found() and mp3lame_dep.found())
ogg_dep = dependency('ogg', required: get_option('external_libs'))
flac_dep = dependency('flac', required: get_option('external_libs'))
vorbis_dep = dependency('vorbis', required: get_option('external_libs'))
vorbisenc_dep = dependency('vorbisenc', required: get_option('external_libs'))
opus_dep = dependency('opus', required: get_option('external_libs'))
sndio_dep = dependency('sndio', required: get_option('external_libs'))
cdata.set10('HAVE_SNDIO_H', sndio_dep.found())
cdata.set10('HAVE_EXTERNAL_XIPH_LIBS', flac_dep.found() and ogg_dep.found() and vorbis_dep.found() and vorbisenc_dep.found() and opus_dep.found())
cdata.set10('CPU_CLIPS_POSITIVE', get_option('cpu_clip'))
cdata.set10('CPU_CLIPS_NEGATIVE', get_option('cpu_clip'))
cdata.set10('ENABLE_EXPERIMENTAL_CODE', get_option('experimental'))
cdata.set10('HAVE_SQLITE3', get_option('regtest'))

cdata.set10('HAVE_DECL_S_IRGRP', cc.has_header_symbol('sys/stat.h', 'S_IRGRP'))
cdata.set10('HAVE_SSIZE_T', cc.has_header_symbol('sys/types.h', 'ssize_t'))
cdata.set('TYPEOF_SF_COUNT_T', 'int64_t')
cdata.set('SF_COUNT_MAX', 'INT64_MAX')

headers = [
  'alsa/asoundlib.h', 'byteswap.h', 'dlfcn.h', 'endian.h', 'immintrin.h', 'inttypes.h', 'locale.h', 'memory.h', 'stdbool.h', 'stdint.h',
  'stdlib.h', 'strings.h', 'string.h', 'sys/stat.h', 'sys/time.h', 'sys/types.h', 'sys/wait.h', 'unistd.h',
]

funcs = [
  'calloc', 'ceil', 'floor', 'fmod', 'free', 'fstat', 'fstat64', 'fsync', 'ftruncate', 'getpagesize', 'gettimeofday', 'gmtime', 'localtime', 'lrint',
  'lrintf', 'lround', 'lseek', 'lseek64', 'malloc', 'mmap', 'open', 'pipe', 'read', 'realloc', 'setlocale', 'snprintf', 'vsnprintf', 'waitpid', 'write'
]

sizes = [
  [ 'int64_t', 'stdint.h' ], [ 'long', '' ], [ 'long long', '' ], [ 'off_t', '' ], [ 'ssize_t', 'sys/types.h' ], [ 'wchar_t', 'wchar.h' ]
]

#completely unused by the code but meson demands definitions
cdata.set('SIZEOF_VOIDP_CODE', '#define VOIDP_CODE')
sizes += [
  [ 'double', '' ], [ 'float', '' ], [ 'int', '' ], [ 'loff_t', '' ], [ 'off64_t', '' ], [ 'short', '' ], [ 'size_t', '' ]
]

foreach f : funcs
  cdata.set10('HAVE_@0@'.format(f.underscorify().to_upper()), cc.has_function(f))
endforeach

cdata.set('HAVE_GMTIME_R', cc.has_function('gmtime_r'))
cdata.set('HAVE_LOCALTIME_R', cc.has_function('localtime_r'))

foreach h : headers
  cdata.set10('HAVE_@0@'.format(h.underscorify().to_upper()), cc.has_header(h))
endforeach

foreach s : sizes
  upper = s[0].underscorify().to_upper()
  cdata.set('SIZEOF_@0@_CODE'.format(upper), '#define @0@ @1@'.format('SIZEOF_@0@'.format(upper), cc.sizeof(s[0], prefix: s[1].contains('.h') ? '#include <@0@>'.format(s[1]) : '')))
endforeach

cfile = configure_file(
  input: 'src/config.h.cmake',
  output: 'config.h',
  format: 'cmake@',
  configuration: cdata,
)

snddata = configuration_data()
snddata.set('SF_COUNT_MAX', 'INT64_MAX')
snddata.set('TYPEOF_SF_COUNT_T', 'int64_t')
sndfile = configure_file(
  input: 'include/sndfile.h.in',
  output: 'sndfile.h',
  format: 'cmake@',
  configuration: snddata,
)

incdirs = include_directories('.', 'src')

libsndfile_sources = files(
  'src/common.c',
  'src/file_io.c',
  'src/command.c',
  'src/pcm.c',
  'src/ulaw.c',
  'src/alaw.c',
  'src/float32.c',
  'src/double64.c',
  'src/ima_adpcm.c',
  'src/ms_adpcm.c',
  'src/gsm610.c',
  'src/dwvw.c',
  'src/vox_adpcm.c',
  'src/interleave.c',
  'src/strings.c',
  'src/dither.c',
  'src/cart.c',
  'src/broadcast.c',
  'src/audio_detect.c',
  'src/ima_oki_adpcm.c',
  'src/alac.c',
  'src/chunk.c',
  'src/ogg.c',
  'src/chanmap.c',
  'src/id3.c',
  'src/sndfile.c',
  'src/aiff.c',
  'src/au.c',
  'src/avr.c',
  'src/caf.c',
  'src/dwd.c',
  'src/flac.c',
  'src/g72x.c',
  'src/htk.c',
  'src/ircam.c',
  'src/macos.c',
  'src/mat4.c',
  'src/mat5.c',
  'src/nist.c',
  'src/paf.c',
  'src/pvf.c',
  'src/raw.c',
  'src/rx2.c',
  'src/sd2.c',
  'src/sds.c',
  'src/svx.c',
  'src/txw.c',
  'src/voc.c',
  'src/wve.c',
  'src/w64.c',
  'src/wavlike.c',
  'src/wav.c',
  'src/xi.c',
  'src/mpc2k.c',
  'src/rf64.c',
  'src/ogg_vorbis.c',
  'src/ogg_speex.c',
  'src/ogg_pcm.c',
  'src/ogg_opus.c',
  'src/ogg_vcomment.c',
  'src/nms_adpcm.c',
  'src/mpeg.c',
  'src/mpeg_decode.c',
  'src/mpeg_l3_encode.c',
  'src/GSM610/add.c',
  'src/GSM610/code.c',
  'src/GSM610/decode.c',
  'src/GSM610/gsm_create.c',
  'src/GSM610/gsm_decode.c',
  'src/GSM610/gsm_destroy.c',
  'src/GSM610/gsm_encode.c',
  'src/GSM610/gsm_option.c',
  'src/GSM610/long_term.c',
  'src/GSM610/lpc.c',
  'src/GSM610/preprocess.c',
  'src/GSM610/rpe.c',
  'src/GSM610/short_term.c',
  'src/GSM610/table.c',
  'src/G72x/g721.c',
  'src/G72x/g723_16.c',
  'src/G72x/g723_24.c',
  'src/G72x/g723_40.c',
  'src/G72x/g72x.c',
  'src/ALAC/ALACBitUtilities.c',
  'src/ALAC/ag_dec.c',
  'src/ALAC/ag_enc.c',
  'src/ALAC/dp_dec.c',
  'src/ALAC/dp_enc.c',
  'src/ALAC/matrix_dec.c',
  'src/ALAC/matrix_enc.c',
  'src/ALAC/alac_decoder.c',
  'src/ALAC/alac_encoder.c',
)

if host_machine.system() == 'windows'
  libsndfile_sources += 'src/windows.c'
endif

gnu_sym_path = 'src/Symbols.gnu-binutils'
gnu_sym_ldflag = '-Wl,--version-script=' + gnu_sym_path
darwin_sym_path = 'src/Symbols.darwin'
link_args = []
if get_option('buildtype') != 'static'
  if cc.links('', name: '-Wl,--version-script', args: ['-shared', gnu_sym_ldflag])
    link_args = [gnu_sym_ldflag]
  elif host_machine.system() == 'darwin' and cc.has_multi_link_arguments('-Wl,-exported_symbols_list', darwin_sym_path)
    link_args = ['-Wl,-exported_symbols_list', darwin_sym_path]
  endif
endif

libsndfile = library('sndfile',
  libsndfile_sources,
  include_directories: incdirs,
  version: meson.project_version(),
  vs_module_defs: 'src/libsndfile-1.def',
  link_args: link_args,
  dependencies: [ mp3_dep, mp3lame_dep, libm_dep, ogg_dep, flac_dep, vorbis_dep, vorbisenc_dep, opus_dep, sndio_dep ],
  install: true,
)

libsndfile_dep = declare_dependency(
  include_directories : incdirs,
  link_with : libsndfile,
)

pconf = import('pkgconfig')
pconf.generate(libsndfile,
  description: 'A library for reading and writing audio files',
)

install_headers(
  sndfile,
  'include/sndfile.hh',
)

install_man(
  'man/sndfile-cmp.1',
  'man/sndfile-concat.1',
  'man/sndfile-convert.1',
  'man/sndfile-info.1',
  'man/sndfile-interleave.1',
  'man/sndfile-metadata-get.1',
  'man/sndfile-play.1',
  'man/sndfile-salvage.1',
)

install_data(
  'docs/index.md',
  'docs/libsndfile.jpg',
  'docs/libsndfile.css',
  'docs/print.css',
  'docs/api.md',
  'docs/command.md',
  'docs/bugs.md',
  'docs/formats.md',
  'docs/sndfile_info.md',
  'docs/new_file_type_howto.md',
  'docs/win32.md',
  'docs/FAQ.md',
  'docs/lists.md',
  'docs/embedded_files.md',
  'docs/octave.md',
  'docs/tutorial.md',
  install_dir: get_option('datadir') / 'doc' / 'libsndfile',
)

subdir('examples')
subdir('programs')
