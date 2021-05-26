if host_machine.system() == 'windows'
    system_sources = files('windows_unicode_filenames.c')
else
    system_sources = []
endif

if get_option('default_library') == 'shared'
    extra_args = ['-DFLAC_API_EXPORTS', '-DFLAC__USE_VISIBILITY_ATTR']
else
    extra_args = ['-DFLAC__NO_DLL']
endif

flac_lib = library('FLAC',
    'bitmath.c',
    'bitreader.c',
    'bitwriter.c',
    'cpu.c',
    'crc.c',
    'fixed.c',
    'fixed_intrin_sse2.c',
    'fixed_intrin_ssse3.c',
    'float.c',
    'format.c',
    'lpc.c',
    'lpc_intrin_sse.c',
    'lpc_intrin_sse2.c',
    'lpc_intrin_sse41.c',
    'lpc_intrin_avx2.c',
    'lpc_intrin_vsx.c',
    'md5.c',
    'memory.c',
    'metadata_iterators.c',
    'metadata_object.c',
    'stream_decoder.c',
    'stream_encoder.c',
    'stream_encoder_intrin_sse2.c',
    'stream_encoder_intrin_ssse3.c',
    'stream_encoder_intrin_avx2.c',
    'stream_encoder_framing.c',
    'window.c',
    'ogg_decoder_aspect.c',
    'ogg_encoder_aspect.c',
    'ogg_helper.c',
    'ogg_mapping.c',
    system_sources,
    include_directories: [main_inc, 'include'],
    c_args: extra_args,
    version: '8.3.0',
    soversion: '8',
    dependencies: [ogg_dep, m_dep],
)
