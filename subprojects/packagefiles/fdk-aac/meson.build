project(
  'fdk-aac',
  'cpp',
  'c',
  version: '2.0.3',
)

fdk_aac_inc = [
  include_directories(
    'libAACdec/include',
    'libAACenc/include',
    'libSYS/include',
    'libArithCoding/include',
    'libDRCdec/include',
    'libSACdec/include',
    'libSACenc/include',
    'libSBRdec/include',
    'libSBRenc/include',
    'libMpegTPDec/include',
    'libMpegTPEnc/include',
    'libFDK/include',
    'libPCMutils/include',
    '.',
  ),
]

fdk_aac_src = files(
  'libAACdec/src/FDK_delay.cpp',
  'libAACdec/src/FDK_delay.h',
  'libAACdec/src/aac_ram.cpp',
  'libAACdec/src/aac_ram.h',
  'libAACdec/src/aac_rom.cpp',
  'libAACdec/src/aac_rom.h',
  'libAACdec/src/aacdec_drc.cpp',
  'libAACdec/src/aacdec_drc.h',
  'libAACdec/src/aacdec_drc_types.h',
  'libAACdec/src/aacdec_hcr.cpp',
  'libAACdec/src/aacdec_hcr.h',
  'libAACdec/src/aacdec_hcr_bit.cpp',
  'libAACdec/src/aacdec_hcr_bit.h',
  'libAACdec/src/aacdec_hcr_types.h',
  'libAACdec/src/aacdec_hcrs.cpp',
  'libAACdec/src/aacdec_hcrs.h',
  'libAACdec/src/aacdec_pns.cpp',
  'libAACdec/src/aacdec_pns.h',
  'libAACdec/src/aacdec_tns.cpp',
  'libAACdec/src/aacdec_tns.h',
  'libAACdec/src/aacdecoder.cpp',
  'libAACdec/src/aacdecoder.h',
  'libAACdec/src/aacdecoder_lib.cpp',
  'libAACdec/src/block.cpp',
  'libAACdec/src/block.h',
  'libAACdec/src/channel.cpp',
  'libAACdec/src/channel.h',
  'libAACdec/src/channelinfo.cpp',
  'libAACdec/src/channelinfo.h',
  'libAACdec/src/conceal.cpp',
  'libAACdec/src/conceal.h',
  'libAACdec/src/conceal_types.h',
  'libAACdec/src/ldfiltbank.cpp',
  'libAACdec/src/ldfiltbank.h',
  'libAACdec/src/overlapadd.h',
  'libAACdec/src/pulsedata.cpp',
  'libAACdec/src/pulsedata.h',
  'libAACdec/src/rvlc.cpp',
  'libAACdec/src/rvlc.h',
  'libAACdec/src/rvlc_info.h',
  'libAACdec/src/rvlcbit.cpp',
  'libAACdec/src/rvlcbit.h',
  'libAACdec/src/rvlcconceal.cpp',
  'libAACdec/src/rvlcconceal.h',
  'libAACdec/src/stereo.cpp',
  'libAACdec/src/stereo.h',
  'libAACdec/src/usacdec_ace_d4t64.cpp',
  'libAACdec/src/usacdec_ace_d4t64.h',
  'libAACdec/src/usacdec_ace_ltp.cpp',
  'libAACdec/src/usacdec_ace_ltp.h',
  'libAACdec/src/usacdec_acelp.cpp',
  'libAACdec/src/usacdec_acelp.h',
  'libAACdec/src/usacdec_const.h',
  'libAACdec/src/usacdec_fac.cpp',
  'libAACdec/src/usacdec_fac.h',
  'libAACdec/src/usacdec_lpc.cpp',
  'libAACdec/src/usacdec_lpc.h',
  'libAACdec/src/usacdec_lpd.cpp',
  'libAACdec/src/usacdec_lpd.h',
  'libAACdec/src/usacdec_rom.cpp',
  'libAACdec/src/usacdec_rom.h',
  'libAACenc/src/aacEnc_ram.cpp',
  'libAACenc/src/aacEnc_ram.h',
  'libAACenc/src/aacEnc_rom.cpp',
  'libAACenc/src/aacEnc_rom.h',
  'libAACenc/src/aacenc.cpp',
  'libAACenc/src/aacenc.h',
  'libAACenc/src/aacenc_lib.cpp',
  'libAACenc/src/aacenc_pns.cpp',
  'libAACenc/src/aacenc_pns.h',
  'libAACenc/src/aacenc_tns.cpp',
  'libAACenc/src/aacenc_tns.h',
  'libAACenc/src/adj_thr.cpp',
  'libAACenc/src/adj_thr.h',
  'libAACenc/src/adj_thr_data.h',
  'libAACenc/src/band_nrg.cpp',
  'libAACenc/src/band_nrg.h',
  'libAACenc/src/bandwidth.cpp',
  'libAACenc/src/bandwidth.h',
  'libAACenc/src/bit_cnt.cpp',
  'libAACenc/src/bit_cnt.h',
  'libAACenc/src/bitenc.cpp',
  'libAACenc/src/bitenc.h',
  'libAACenc/src/block_switch.cpp',
  'libAACenc/src/block_switch.h',
  'libAACenc/src/channel_map.cpp',
  'libAACenc/src/channel_map.h',
  'libAACenc/src/chaosmeasure.cpp',
  'libAACenc/src/chaosmeasure.h',
  'libAACenc/src/dyn_bits.cpp',
  'libAACenc/src/dyn_bits.h',
  'libAACenc/src/grp_data.cpp',
  'libAACenc/src/grp_data.h',
  'libAACenc/src/intensity.cpp',
  'libAACenc/src/intensity.h',
  'libAACenc/src/interface.h',
  'libAACenc/src/line_pe.cpp',
  'libAACenc/src/line_pe.h',
  'libAACenc/src/metadata_compressor.cpp',
  'libAACenc/src/metadata_compressor.h',
  'libAACenc/src/metadata_main.cpp',
  'libAACenc/src/metadata_main.h',
  'libAACenc/src/mps_main.cpp',
  'libAACenc/src/mps_main.h',
  'libAACenc/src/ms_stereo.cpp',
  'libAACenc/src/ms_stereo.h',
  'libAACenc/src/noisedet.cpp',
  'libAACenc/src/noisedet.h',
  'libAACenc/src/pns_func.h',
  'libAACenc/src/pnsparam.cpp',
  'libAACenc/src/pnsparam.h',
  'libAACenc/src/pre_echo_control.cpp',
  'libAACenc/src/pre_echo_control.h',
  'libAACenc/src/psy_configuration.cpp',
  'libAACenc/src/psy_configuration.h',
  'libAACenc/src/psy_const.h',
  'libAACenc/src/psy_data.h',
  'libAACenc/src/psy_main.cpp',
  'libAACenc/src/psy_main.h',
  'libAACenc/src/qc_data.h',
  'libAACenc/src/qc_main.cpp',
  'libAACenc/src/qc_main.h',
  'libAACenc/src/quantize.cpp',
  'libAACenc/src/quantize.h',
  'libAACenc/src/sf_estim.cpp',
  'libAACenc/src/sf_estim.h',
  'libAACenc/src/spreading.cpp',
  'libAACenc/src/spreading.h',
  'libAACenc/src/tns_func.h',
  'libAACenc/src/tonality.cpp',
  'libAACenc/src/tonality.h',
  'libAACenc/src/transform.cpp',
  'libAACenc/src/transform.h',
  'libArithCoding/src/ac_arith_coder.cpp',
  'libDRCdec/src/FDK_drcDecLib.cpp',
  'libDRCdec/src/drcDec_gainDecoder.cpp',
  'libDRCdec/src/drcDec_gainDecoder.h',
  'libDRCdec/src/drcDec_reader.cpp',
  'libDRCdec/src/drcDec_reader.h',
  'libDRCdec/src/drcDec_rom.cpp',
  'libDRCdec/src/drcDec_rom.h',
  'libDRCdec/src/drcDec_selectionProcess.cpp',
  'libDRCdec/src/drcDec_selectionProcess.h',
  'libDRCdec/src/drcDec_tools.cpp',
  'libDRCdec/src/drcDec_tools.h',
  'libDRCdec/src/drcDec_types.h',
  'libDRCdec/src/drcDecoder.h',
  'libDRCdec/src/drcGainDec_init.cpp',
  'libDRCdec/src/drcGainDec_init.h',
  'libDRCdec/src/drcGainDec_preprocess.cpp',
  'libDRCdec/src/drcGainDec_preprocess.h',
  'libDRCdec/src/drcGainDec_process.cpp',
  'libDRCdec/src/drcGainDec_process.h',
  'libFDK/src/FDK_bitbuffer.cpp',
  'libFDK/src/FDK_core.cpp',
  'libFDK/src/FDK_crc.cpp',
  'libFDK/src/FDK_decorrelate.cpp',
  'libFDK/src/FDK_hybrid.cpp',
  'libFDK/src/FDK_lpc.cpp',
  'libFDK/src/FDK_matrixCalloc.cpp',
  'libFDK/src/FDK_qmf_domain.cpp',
  'libFDK/src/FDK_tools_rom.cpp',
  'libFDK/src/FDK_trigFcts.cpp',
  'libFDK/src/autocorr2nd.cpp',
  'libFDK/src/dct.cpp',
  'libFDK/src/fft.cpp',
  'libFDK/src/fft_rad2.cpp',
  'libFDK/src/fixpoint_math.cpp',
  'libFDK/src/huff_nodes.cpp',
  'libFDK/src/mdct.cpp',
  'libFDK/src/nlc_dec.cpp',
  'libFDK/src/qmf.cpp',
  'libFDK/src/scale.cpp',
  'libMpegTPDec/src/tp_version.h',
  'libMpegTPDec/src/tpdec_adif.cpp',
  'libMpegTPDec/src/tpdec_adif.h',
  'libMpegTPDec/src/tpdec_adts.cpp',
  'libMpegTPDec/src/tpdec_adts.h',
  'libMpegTPDec/src/tpdec_asc.cpp',
  'libMpegTPDec/src/tpdec_drm.cpp',
  'libMpegTPDec/src/tpdec_drm.h',
  'libMpegTPDec/src/tpdec_latm.cpp',
  'libMpegTPDec/src/tpdec_latm.h',
  'libMpegTPDec/src/tpdec_lib.cpp',
  'libMpegTPEnc/src/tp_version.h',
  'libMpegTPEnc/src/tpenc_adif.cpp',
  'libMpegTPEnc/src/tpenc_adif.h',
  'libMpegTPEnc/src/tpenc_adts.cpp',
  'libMpegTPEnc/src/tpenc_adts.h',
  'libMpegTPEnc/src/tpenc_asc.cpp',
  'libMpegTPEnc/src/tpenc_asc.h',
  'libMpegTPEnc/src/tpenc_latm.cpp',
  'libMpegTPEnc/src/tpenc_latm.h',
  'libMpegTPEnc/src/tpenc_lib.cpp',
  'libPCMutils/src/limiter.cpp',
  'libPCMutils/src/pcm_utils.cpp',
  'libPCMutils/src/pcmdmx_lib.cpp',
  'libPCMutils/src/version.h'
,
  'libSACdec/src/sac_bitdec.cpp',
  'libSACdec/src/sac_bitdec.h',
  'libSACdec/src/sac_calcM1andM2.cpp',
  'libSACdec/src/sac_calcM1andM2.h',
  'libSACdec/src/sac_dec.cpp',
  'libSACdec/src/sac_dec.h',
  'libSACdec/src/sac_dec_conceal.cpp',
  'libSACdec/src/sac_dec_conceal.h',
  'libSACdec/src/sac_dec_interface.h',
  'libSACdec/src/sac_dec_lib.cpp',
  'libSACdec/src/sac_dec_ssc_struct.h',
  'libSACdec/src/sac_process.cpp',
  'libSACdec/src/sac_process.h',
  'libSACdec/src/sac_qmf.cpp',
  'libSACdec/src/sac_qmf.h',
  'libSACdec/src/sac_reshapeBBEnv.cpp',
  'libSACdec/src/sac_reshapeBBEnv.h',
  'libSACdec/src/sac_rom.cpp',
  'libSACdec/src/sac_rom.h',
  'libSACdec/src/sac_smoothing.cpp',
  'libSACdec/src/sac_smoothing.h',
  'libSACdec/src/sac_stp.cpp',
  'libSACdec/src/sac_stp.h',
  'libSACdec/src/sac_tsd.cpp',
  'libSACdec/src/sac_tsd.h',
  'libSACenc/src/sacenc_bitstream.cpp',
  'libSACenc/src/sacenc_bitstream.h',
  'libSACenc/src/sacenc_const.h',
  'libSACenc/src/sacenc_delay.cpp',
  'libSACenc/src/sacenc_delay.h',
  'libSACenc/src/sacenc_dmx_tdom_enh.cpp',
  'libSACenc/src/sacenc_dmx_tdom_enh.h',
  'libSACenc/src/sacenc_filter.cpp',
  'libSACenc/src/sacenc_filter.h',
  'libSACenc/src/sacenc_framewindowing.cpp',
  'libSACenc/src/sacenc_framewindowing.h',
  'libSACenc/src/sacenc_huff_tab.cpp',
  'libSACenc/src/sacenc_huff_tab.h',
  'libSACenc/src/sacenc_lib.cpp',
  'libSACenc/src/sacenc_nlc_enc.cpp',
  'libSACenc/src/sacenc_nlc_enc.h',
  'libSACenc/src/sacenc_onsetdetect.cpp',
  'libSACenc/src/sacenc_onsetdetect.h',
  'libSACenc/src/sacenc_paramextract.cpp',
  'libSACenc/src/sacenc_paramextract.h',
  'libSACenc/src/sacenc_staticgain.cpp',
  'libSACenc/src/sacenc_staticgain.h',
  'libSACenc/src/sacenc_tree.cpp',
  'libSACenc/src/sacenc_tree.h',
  'libSACenc/src/sacenc_vectorfunctions.cpp',
  'libSACenc/src/sacenc_vectorfunctions.h',
  'libSBRdec/src/HFgen_preFlat.cpp',
  'libSBRdec/src/HFgen_preFlat.h',
  'libSBRdec/src/env_calc.cpp',
  'libSBRdec/src/env_calc.h',
  'libSBRdec/src/env_dec.cpp',
  'libSBRdec/src/env_dec.h',
  'libSBRdec/src/env_extr.cpp',
  'libSBRdec/src/env_extr.h',
  'libSBRdec/src/hbe.cpp',
  'libSBRdec/src/hbe.h',
  'libSBRdec/src/huff_dec.cpp',
  'libSBRdec/src/huff_dec.h',
  'libSBRdec/src/lpp_tran.cpp',
  'libSBRdec/src/lpp_tran.h',
  'libSBRdec/src/psbitdec.cpp',
  'libSBRdec/src/psbitdec.h',
  'libSBRdec/src/psdec.cpp',
  'libSBRdec/src/psdec.h',
  'libSBRdec/src/psdec_drm.cpp',
  'libSBRdec/src/psdec_drm.h',
  'libSBRdec/src/psdecrom_drm.cpp',
  'libSBRdec/src/pvc_dec.cpp',
  'libSBRdec/src/pvc_dec.h',
  'libSBRdec/src/sbr_deb.cpp',
  'libSBRdec/src/sbr_deb.h',
  'libSBRdec/src/sbr_dec.cpp',
  'libSBRdec/src/sbr_dec.h',
  'libSBRdec/src/sbr_ram.cpp',
  'libSBRdec/src/sbr_ram.h',
  'libSBRdec/src/sbr_rom.cpp',
  'libSBRdec/src/sbr_rom.h',
  'libSBRdec/src/sbrdec_drc.cpp',
  'libSBRdec/src/sbrdec_drc.h',
  'libSBRdec/src/sbrdec_freq_sca.cpp',
  'libSBRdec/src/sbrdec_freq_sca.h',
  'libSBRdec/src/sbrdecoder.cpp',
  'libSBRdec/src/transcendent.h',
  'libSBRenc/src/bit_sbr.cpp',
  'libSBRenc/src/bit_sbr.h',
  'libSBRenc/src/cmondata.h',
  'libSBRenc/src/code_env.cpp',
  'libSBRenc/src/code_env.h',
  'libSBRenc/src/env_bit.cpp',
  'libSBRenc/src/env_bit.h',
  'libSBRenc/src/env_est.cpp',
  'libSBRenc/src/env_est.h',
  'libSBRenc/src/fram_gen.cpp',
  'libSBRenc/src/fram_gen.h',
  'libSBRenc/src/invf_est.cpp',
  'libSBRenc/src/invf_est.h',
  'libSBRenc/src/mh_det.cpp',
  'libSBRenc/src/mh_det.h',
  'libSBRenc/src/nf_est.cpp',
  'libSBRenc/src/nf_est.h',
  'libSBRenc/src/ps_bitenc.cpp',
  'libSBRenc/src/ps_bitenc.h',
  'libSBRenc/src/ps_const.h',
  'libSBRenc/src/ps_encode.cpp',
  'libSBRenc/src/ps_encode.h',
  'libSBRenc/src/ps_main.cpp',
  'libSBRenc/src/ps_main.h',
  'libSBRenc/src/resampler.cpp',
  'libSBRenc/src/resampler.h',
  'libSBRenc/src/sbr.h',
  'libSBRenc/src/sbr_def.h',
  'libSBRenc/src/sbr_encoder.cpp',
  'libSBRenc/src/sbr_misc.cpp',
  'libSBRenc/src/sbr_misc.h',
  'libSBRenc/src/sbrenc_freq_sca.cpp',
  'libSBRenc/src/sbrenc_freq_sca.h',
  'libSBRenc/src/sbrenc_ram.cpp',
  'libSBRenc/src/sbrenc_ram.h',
  'libSBRenc/src/sbrenc_rom.cpp',
  'libSBRenc/src/sbrenc_rom.h',
  'libSBRenc/src/ton_corr.cpp',
  'libSBRenc/src/ton_corr.h',
  'libSBRenc/src/tran_det.cpp',
  'libSBRenc/src/tran_det.h',
  'libSYS/src/genericStds.cpp',
  'libSYS/src/syslib_channelMapDescr.cpp',
)

fdk_aac_headers = [
  'libAACdec/include/aacdecoder_lib.h',
  'libAACenc/include/aacenc_lib.h',
  'libSYS/include/FDK_audio.h',
  'libSYS/include/genericStds.h',
  'libSYS/include/machine_type.h',
  'libSYS/include/syslib_channelMapDescr.h',
]

if host_machine.system() == 'windows'
  fdk_aac_src += files('win32/getopt.h')
  fdk_aac_inc += include_directories('win32')
endif

install_headers(
  files(fdk_aac_headers),
  subdir: 'fdk-aac',
)

# Make using fdk-aac as a subproject behave the same as when used installed.
subdir('fdk-aac')

cc = meson.get_compiler('c')
m_dep = cc.find_library(
  'm',
  required: false,
)

extra_args = ['-Dfdk_aac_EXPORTS']
if get_option('remove-date')
  extra_args += '-DSUPPRESS_BUILD_DATE_INFO'
endif

fdk_aac = library(
  'fdk_aac',
  fdk_aac_src,
  dependencies: m_dep,
  include_directories: fdk_aac_inc,
  install: true,
  cpp_args: cc.get_supported_arguments('-fno-exceptions', '-fno-rtti') + extra_args,
  c_args: extra_args,
  vs_module_defs: 'fdk-aac.def',
)

fdk_aac_dep = declare_dependency(
  link_with: fdk_aac,
  dependencies: m_dep,
  include_directories: fdk_aac_inc,
)

pkgc = import('pkgconfig')
pkgc.generate(
  fdk_aac,
  name: 'fdk-aac',
  description: 'AAC codec library',
)

if not get_option('build-programs').disabled()
  executable(
    'aac-enc',
    files('aac-enc.c', 'wavreader.c'),
    dependencies: fdk_aac_dep,
  )
endif
