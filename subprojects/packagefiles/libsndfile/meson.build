project(
  'libsndfile',
  'c',
  license: 'LGPL-2.1-or-later',
  version: '1.2.2',
  meson_version: '>=0.54.1',
)

#needed for time_r functions
if host_machine.system() == 'windows'
  add_project_arguments(
    '-D_POSIX_C_SOURCE',
    language: 'c',
  )
endif

cc = meson.get_compiler('c')

if cc.get_argument_syntax() == 'msvc'
  add_project_arguments(
    '-D_CRT_SECURE_NO_WARNINGS',
    cc.get_supported_arguments('-Wno-deprecated-declarations'),
    language: 'c',
  )
endif

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
cdata.set10(
  'WIN32_TARGET_DLL',
  host_machine.system() == 'windows' and get_option('buildtype') != 'static',
)

# code errors if this is not 8
cdata.set('SIZEOF_SF_COUNT_T_CODE', '#define SIZEOF_SF_COUNT_T 8')

libm_dep = cc.find_library(
  'm',
  required: false,
)
cdata.set10('HAVE_LIBM', libm_dep.found())
mp3_dep = dependency(
  'libmpg123',
  required: get_option('mpeg'),
)
mp3lame_dep = cc.find_library(
  'mp3lame',
  required: get_option('mpeg'),
)
cdata.set10('HAVE_MPEG', mp3_dep.found() and mp3lame_dep.found())
ogg_dep = dependency(
  'ogg',
  required: get_option('external_libs'),
)
flac_dep = dependency(
  'flac',
  required: get_option('external_libs'),
)
vorbis_dep = dependency(
  'vorbis',
  required: get_option('external_libs'),
)
vorbisenc_dep = dependency(
  'vorbisenc',
  required: get_option('external_libs'),
)
opus_dep = dependency(
  'opus',
  required: get_option('external_libs'),
)
if host_machine.system() == 'openbsd'
  sndio_dep = dependency(
    'sndio',
    required: get_option('sndio'),
  )
else
  sndio_dep = dependency(
    '',
    required: false,
  )
endif
cdata.set10('HAVE_SNDIO_H', sndio_dep.found())
cdata.set10(
  'HAVE_EXTERNAL_XIPH_LIBS',
  flac_dep.found() and ogg_dep.found() and vorbis_dep.found() and vorbisenc_dep.found() and opus_dep.found(),
)
cdata.set10('CPU_CLIPS_POSITIVE', get_option('cpu_clip'))
cdata.set10('CPU_CLIPS_NEGATIVE', get_option('cpu_clip'))
cdata.set10('ENABLE_EXPERIMENTAL_CODE', get_option('experimental'))
cdata.set10('HAVE_SQLITE3', get_option('regtest'))

cdata.set10('HAVE_DECL_S_IRGRP', cc.has_header_symbol('sys/stat.h', 'S_IRGRP'))
cdata.set10('HAVE_FSTAT64', cc.has_header_symbol('sys/stat.h', 'fstat64'))
cdata.set10('HAVE_SSIZE_T', cc.has_header_symbol('sys/types.h', 'ssize_t'))
cdata.set('TYPEOF_SF_COUNT_T', 'int64_t')
cdata.set('SF_COUNT_MAX', 'INT64_MAX')

headers = [
  'alsa/asoundlib.h',
  'byteswap.h',
  'direct.h',
  'dlfcn.h',
  'endian.h',
  'immintrin.h',
  'inttypes.h',
  'io.h',
  'locale.h',
  'memory.h',
  'stdbool.h',
  'stdint.h',
  'stdlib.h',
  'strings.h',
  'string.h',
  'sys/stat.h',
  'sys/time.h',
  'sys/types.h',
  'sys/wait.h',
  'unistd.h',
]

funcs = [
  'calloc',
  'ceil',
  'floor',
  'fmod',
  'free',
  'fstat',
  'fsync',
  'ftruncate',
  'getpagesize',
  'gettimeofday',
  'gmtime',
  'gmtime_r',
  'localtime',
  'localtime_r',
  'lrint',
  'lrintf',
  'lround',
  'lseek',
  'lseek64',
  'malloc',
  'mmap',
  'open',
  'pipe',
  'read',
  'realloc',
  'setlocale',
  'snprintf',
  'vsnprintf',
  'waitpid',
  'write',
]

sizes = {
  'int64_t': 'stdint.h',
  'long': '',
  'long long': '',
  'off_t': '',
  'ssize_t': 'sys/types.h',
  'wchar_t': 'wchar.h',
}

#completely unused by the code but meson demands definitions
cdata.set('SIZEOF_VOIDP_CODE', '#define VOIDP_CODE')
sizes += {
  'double': '',
  'float': '',
  'int': '',
  'loff_t': '',
  'off64_t': '',
  'short': '',
  'size_t': '',
}

foreach f : funcs
  if cc.has_function(f)
    cdata.set('HAVE_@0@'.format(f.underscorify().to_upper()), 1)
  endif
endforeach

foreach h : headers
  if cc.has_header(h)
    cdata.set('HAVE_@0@'.format(h.underscorify().to_upper()), 1)
  endif
endforeach

foreach s, h : sizes
  upper = s.underscorify().to_upper()
  cdata.set(
    'SIZEOF_@0@_CODE'.format(upper),
    '#define @0@ @1@'.format(
      'SIZEOF_@0@'.format(upper),
      cc.sizeof(
        s,
        prefix: h.contains('.h') ? '#include <@0@>'.format(h) : '',
      ),
    ),
  )
endforeach

cfile = configure_file(
  input: 'src/config.h.cmake',
  output: 'config.h',
  format: 'cmake@',
  configuration: cdata,
)

incdirs = include_directories('.', 'include', 'src')

libsndfile_sources = files(
  'src/ALAC/ALACBitUtilities.c',
  'src/ALAC/ag_dec.c',
  'src/ALAC/ag_enc.c',
  'src/ALAC/alac_decoder.c',
  'src/ALAC/alac_encoder.c',
  'src/ALAC/dp_dec.c',
  'src/ALAC/dp_enc.c',
  'src/ALAC/matrix_dec.c',
  'src/ALAC/matrix_enc.c',
  'src/G72x/g721.c',
  'src/G72x/g723_16.c',
  'src/G72x/g723_24.c',
  'src/G72x/g723_40.c',
  'src/G72x/g72x.c',
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
  'src/aiff.c',
  'src/alac.c',
  'src/alaw.c',
  'src/au.c',
  'src/audio_detect.c',
  'src/avr.c',
  'src/broadcast.c',
  'src/caf.c',
  'src/cart.c',
  'src/chanmap.c',
  'src/chunk.c',
  'src/command.c',
  'src/common.c',
  'src/dither.c',
  'src/double64.c',
  'src/dwd.c',
  'src/dwvw.c',
  'src/file_io.c',
  'src/flac.c',
  'src/float32.c',
  'src/g72x.c',
  'src/gsm610.c',
  'src/htk.c',
  'src/id3.c',
  'src/ima_adpcm.c',
  'src/ima_oki_adpcm.c',
  'src/interleave.c',
  'src/ircam.c',
  'src/macos.c',
  'src/mat4.c',
  'src/mat5.c',
  'src/mpc2k.c',
  'src/mpeg.c',
  'src/mpeg_decode.c',
  'src/mpeg_l3_encode.c',
  'src/ms_adpcm.c',
  'src/nist.c',
  'src/nms_adpcm.c',
  'src/ogg.c',
  'src/ogg_opus.c',
  'src/ogg_pcm.c',
  'src/ogg_speex.c',
  'src/ogg_vcomment.c',
  'src/ogg_vorbis.c',
  'src/paf.c',
  'src/pcm.c',
  'src/pvf.c',
  'src/raw.c',
  'src/rf64.c',
  'src/rx2.c',
  'src/sd2.c',
  'src/sds.c',
  'src/sndfile.c',
  'src/strings.c',
  'src/svx.c',
  'src/txw.c',
  'src/ulaw.c',
  'src/voc.c',
  'src/vox_adpcm.c',
  'src/w64.c',
  'src/wav.c',
  'src/wavlike.c',
  'src/wve.c',
  'src/xi.c',
)

if host_machine.system() == 'windows'
  libsndfile_sources += 'src/windows.c'
endif

gnu_sym_ldflag = '-Wl,--version-script,@0@/src/Symbols.gnu-binutils'.format(
  meson.current_source_dir(),
)
darwin_sym_ldflag = '-Wl,-exported_symbols_list,@0@/src/Symbols.darwin'.format(
  meson.current_source_dir(),
)
link_args = []
if get_option('default_library') != 'static'
  if cc.links(
    '',
    name: '-Wl,--version-script',
    args: ['-shared', gnu_sym_ldflag],
  )
    link_args += gnu_sym_ldflag
  elif cc.links(
    '',
    name: '-Wl,-exported_symbols_list',
    args: ['-shared', darwin_sym_ldflag],
  )
    link_args += darwin_sym_ldflag
  endif
endif

libsndfile = library(
  'sndfile',
  libsndfile_sources,
  include_directories: incdirs,
  version: meson.project_version(),
  vs_module_defs: 'src/libsndfile-1.def',
  link_args: link_args,
  dependencies: [
    mp3_dep,
    mp3lame_dep,
    libm_dep,
    ogg_dep,
    flac_dep,
    vorbis_dep,
    vorbisenc_dep,
    opus_dep,
    sndio_dep,
  ],
  install: true,
)

libsndfile_dep = declare_dependency(
  include_directories: incdirs,
  link_with: libsndfile,
)

pconf = import('pkgconfig')
pconf.generate(
  libsndfile,
  description: 'A library for reading and writing audio files',
)

install_headers('include/sndfile.h', 'include/sndfile.hh')

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
