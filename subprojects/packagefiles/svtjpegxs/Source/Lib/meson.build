install_headers(
  '../API/SvtJpegxs.h',
  '../API/SvtJpegxsEnc.h',
  '../API/SvtJpegxsDec.h',
  '../API/SvtJpegxsDec.h',
  '../API/SvtJpegxsImageBufferTools.h',
)

api_incdirs = include_directories('../API')

msvc = cc.get_argument_syntax() == 'msvc'
mavx2 = cc.get_supported_arguments(msvc ? ['/arch:AVX2'] : ['-mavx2'])
mavx512 = cc.get_supported_arguments(
  msvc ? ['/arch:AVX512'] : [
    '-mavx512f',
    '-mavx512bw',
    '-mavx512cd',
    '-mavx512dq',
    '-mavx512vl',
  ],
)
msse2 = cc.get_supported_arguments(['-msse2'])
msse4_1 = cc.get_supported_arguments(['-msse4.1'])

libcommon_avx2 = static_library(
  'common_avx2',
  'Common/ASM_AVX2/empty.c',
  c_args: mavx2,
)

libcommon_sse2 = static_library(
  'common_sse2',
  'Common/ASM_SSE2/empty.c',
  'Common/ASM_SSE2/PictureOperators_SSE2.asm',
  include_directories: 'Common/ASM_SSE2',
  c_args: msse2,
)

common_dep = declare_dependency(
  sources: [
    'Common/Codec/common_dsp_rtcd.c',
    'Common/Codec/SvtUtility.c',
    'Common/Codec/Threads/SystemResourceManager.c',
    'Common/Codec/Threads/SvtMalloc.c',
    'Common/Codec/Threads/SvtThreads.c',
    'Common/Codec/Pi.c',
    'Common/Codec/EncDec.c',
    'Common/Codec/ImageBuffer.c',
    'Common/Codec/SvtLog.c',
  ],
  include_directories: [api_incdirs, 'Common/Codec'],
  dependencies: cpuinfo_dep,
  link_with: [libcommon_avx2, libcommon_sse2],
)

libencoder_sse2 = static_library(
  'encoder_sse2',
  'Encoder/ASM_SSE2/empty.c',
  'Encoder/ASM_SSE2/ASM_SSE2.asm',
  include_directories: ['Common/ASM_SSE2'],
  dependencies: common_dep,
  c_args: msse2,
)

libencoder_sse4_1 = static_library(
  'encoder_sse4_1',
  'Encoder/ASM_SSE4_1/Quant_sse4_1.c',
  'Encoder/ASM_SSE4_1/group_coding_sse4_1.c',
  include_directories: ['Encoder/Codec'],
  dependencies: common_dep,
  c_args: msse4_1,
)

libencoder_avx2 = static_library(
  'encoder_avx2',
  'Encoder/ASM_AVX2/Dwt_AVX2.c',
  'Encoder/ASM_AVX2/NltEnc_avx2.c',
  'Encoder/ASM_AVX2/RateControl_avx2.c',
  'Encoder/ASM_AVX2/Quant_avx2.c',
  include_directories: ['Encoder/Codec', 'Encoder/ASM_SSE4_1'],
  dependencies: common_dep,
  c_args: mavx2,
)

libencoder_avx512 = static_library(
  'encoder_avx512',
  'Encoder/ASM_AVX512/Pack_avx512.c',
  'Encoder/ASM_AVX512/Enc_avx512.c',
  include_directories: [
    'Encoder/Codec',
    'Encoder/ASM_SSE4_1',
    'Encoder/ASM_AVX2',
  ],
  dependencies: common_dep,
  c_args: mavx512,
)

encoder_dep = declare_dependency(
  sources: [
    'Encoder/Codec/InitStageProcess.c',
    'Encoder/Codec/PreRcStageProcess.c',
    'Encoder/Codec/EncHandle.c',
    'Encoder/Codec/PackOut.c',
    'Encoder/Codec/encoder_dsp_rtcd.c',
    'Encoder/Codec/QuantStageProcess.c',
    'Encoder/Codec/DwtStageProcess.c',
    'Encoder/Codec/FinalStageProcess.c',
    'Encoder/Codec/GcStageProcess.c',
    'Encoder/Codec/PictureControlSet.c',
    'Encoder/Codec/PackHeaders.c',
    'Encoder/Codec/PrecinctEnc.c',
    'Encoder/Codec/Quant.c',
    'Encoder/Codec/DwtInput.c',
    'Encoder/Codec/Dwt.c',
    'Encoder/Codec/PackStageProcess.c',
    'Encoder/Codec/NltEnc.c',
    'Encoder/Codec/WeightTable.c',
    'Encoder/Codec/RateControl.c',
    'Encoder/Codec/BitstreamWriter.c',
    'Encoder/Codec/PiEnc.c',
    'Encoder/Codec/BinarySearch.c',
    'Encoder/Codec/PackIn.c',
    'Encoder/Codec/PackPrecinct.c',
  ],
  include_directories: [
    'Encoder/Codec',
    'Encoder/ASM_AVX512',
    'Encoder/ASM_SSE4_1',
    'Encoder/ASM_AVX2',
  ],
  dependencies: common_dep,
  link_with: [
    libencoder_avx2,
    libencoder_avx512,
    libencoder_sse2,
    libencoder_sse4_1,
  ],
)

libdecoder_avx512 = static_library(
  'decoder_avx512',
  'Decoder/ASM_AVX512/NltDec_avx512.c',
  'Decoder/ASM_AVX512/Dequant_avx512.c',
  'Decoder/ASM_AVX512/idwt-avx512.c',
  include_directories: ['Decoder/Codec'],
  dependencies: common_dep,
  c_args: mavx512,
)

libdecoder_avx2 = static_library(
  'decoder_avx2',
  'Decoder/ASM_AVX2/Dwt53Decoder_AVX2.c',
  'Decoder/ASM_AVX2/UnPack_avx2.c',
  'Decoder/ASM_AVX2/NltDec_AVX2.c',
  include_directories: ['Decoder/Codec'],
  dependencies: common_dep,
  c_args: mavx2,
)

libdecoder_sse4 = static_library(
  'decoder_sse4',
  'Decoder/ASM_SSE4_1/Dequant_SSE4.c',
  include_directories: ['Decoder/Codec'],
  dependencies: common_dep,
  c_args: msse4_1,
)

decoder_dep = declare_dependency(
  sources: [
    'Decoder/Codec/DecThreadInit.c',
    'Decoder/Codec/DecThreads.c',
    'Decoder/Codec/DecThreadFinal.c',
    'Decoder/Codec/ParseHeader.c',
    'Decoder/Codec/Dequant.c',
    'Decoder/Codec/DwtDecoder.c',
    'Decoder/Codec/DecThreadSlice.c',
    'Decoder/Codec/Mct.c',
    'Decoder/Codec/DecHandle.c',
    'Decoder/Codec/Packing.c',
    'Decoder/Codec/NltDec.c',
    'Decoder/Codec/Idwt.c',
    'Decoder/Codec/Precinct.c',
    'Decoder/Codec/Mct.c',
    'Decoder/Codec/DecHandle.c',
    'Decoder/Codec/Decoder.c',
    'Decoder/Codec/NltDec.c',
    'Decoder/Codec/Packing.c',
    'Decoder/Codec/Idwt.c',
    'Decoder/Codec/BitstreamReader.c',
    'Decoder/Codec/DecThreadInit.c',
    'Decoder/Codec/Precinct.c',
    'Decoder/Codec/ParseHeader.c',
    'Decoder/Codec/decoder_dsp_rtcd.c',
    'Decoder/Codec/DecThreadFinal.c',
  ],
  include_directories: [
    'Decoder/Codec',
    'Decoder/ASM_AVX2',
    'Decoder/ASM_SSE4_1',
    'Decoder/ASM_AVX512',
  ],
  dependencies: common_dep,
  link_with: [libdecoder_avx2, libdecoder_avx512, libdecoder_sse4],
)

libsvtjpegxs = library(
  'svtjpegxs',
  dependencies: [encoder_dep, decoder_dep],
  install: true,
)

cflags = []
if build_shared
  cflags += ['-DDEF_DLL']
endif

svtjpegxs_dep = declare_dependency(
  include_directories: api_incdirs,
  link_with: libsvtjpegxs,
  compile_args: cflags,
)

meson.override_dependency('SvtJpegxs', svtjpegxs_dep)

pkg = import('pkgconfig')
pkg.generate(
  libsvtjpegxs,
  name: 'SvtJpegxs',
  description: 'SVT (Scalable Video Technology) for JPEG XS library',
  extra_cflags: cflags,
)
