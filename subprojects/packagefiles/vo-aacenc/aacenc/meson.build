libvo_aacenc_sources = files(
  'basic_op/basicop2.c',
  'basic_op/oper_32b.c',
  'src/aac_rom.c',
  'src/aacenc.c',
  'src/aacenc_core.c',
  'src/adj_thr.c',
  'src/band_nrg.c',
  'src/bit_cnt.c',
  'src/bitbuffer.c',
  'src/bitenc.c',
  'src/block_switch.c',
  'src/channel_map.c',
  'src/dyn_bits.c',
  'src/grp_data.c',
  'src/interface.c',
  'src/line_pe.c',
  'src/memalign.c',
  'src/ms_stereo.c',
  'src/pre_echo_control.c',
  'src/psy_configuration.c',
  'src/psy_main.c',
  'src/qc_main.c',
  'src/quantize.c',
  'src/sf_estim.c',
  'src/spreading.c',
  'src/stat_bits.c',
  'src/tns.c',
  'src/transform.c',
)

if armv7neon
  libvo_aacenc_sources += files(
    'src/asm/ARMV5E/AutoCorrelation_v5.s',
    'src/asm/ARMV5E/CalcWindowEnergy_v5.s',
    'src/asm/ARMV5E/band_nrg_v5.s',
    'src/asm/ARMV7/PrePostMDCT_v7.s',
    'src/asm/ARMV7/R4R8First_v7.s',
    'src/asm/ARMV7/Radix4FFT_v7.s',
  )
elif armv5e
  libvo_aacenc_sources += files(
    'src/asm/ARMV5E/AutoCorrelation_v5.s',
    'src/asm/ARMV5E/CalcWindowEnergy_v5.s',
    'src/asm/ARMV5E/PrePostMDCT_v5.s',
    'src/asm/ARMV5E/R4R8First_v5.s',
    'src/asm/ARMV5E/Radix4FFT_v5.s',
    'src/asm/ARMV5E/band_nrg_v5.s',
  )
endif

libvo_aacenc_includes += [
  include_directories('basic_op'),
  include_directories('inc'),
]
