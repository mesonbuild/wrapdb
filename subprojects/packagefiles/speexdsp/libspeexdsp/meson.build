sources = [
  'buffer.c',
  'fftwrap.c',
  'filterbank.c',
  'jitter.c',
  'kiss_fft.c',
  'kiss_fftr.c',
  'mdf.c',
  'preprocess.c',
  'resample.c',
  'scal.c',
  'smallft.c',
]

m_dep = cc.find_library(
  'm',
  required: false,
)

speexdsp = library(
  'speexdsp',
  sources,
  dependencies: m_dep,
  include_directories: incdir,
  gnu_symbol_visibility: 'hidden',
  vs_module_defs: '../win32/libspeexdsp.def',
  version: lib_version,
  soversion: host_machine.system() == 'windows' ? '' : lib_soversion,
  install: true,
)

speexdsp_dep = declare_dependency(
  link_with: speexdsp,
  include_directories: incdir,
  dependencies: m_dep,
)

pkgconfig = import('pkgconfig')
pkgconfig.generate(
  speexdsp,
  description: 'SpeexDSP is a patent-free, Open Source/Free Software DSP library',
)
