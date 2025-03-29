mt32emu_config_h_in = files('config.h.in')

common_headers = [
  'mt32emu.h',
  'globals.h',
  'internals.h',
  'Enumerations.h',
  'Types.h',
]
cpp_headers = [
  'Display.h',
  'File.h',
  'FileStream.h',
  'MidiStreamParser.h',
  'Part.h',
  'ROMInfo.h',
  'SampleRateConverter.h',
  'Structures.h',
  'Synth.h',
]
c_headers = ['c_interface.h', 'c_types.h', 'cpp_interface.h']

# These two maps exist only, so we can generate a new directory containing
# all the headers later on.
#
mt32emu_header_map = []
foreach header : common_headers + cpp_headers
  mt32emu_header_map += [[files(header), header]]
endforeach
mt32emu_c_header_map = []
foreach header : c_headers
  mt32emu_c_header_map += [[files('c_interface' / header), header]]
endforeach

mt32emu_sources = files(
  'Analog.cpp',
  'BReverbModel.cpp',
  'Display.cpp',
  'File.cpp',
  'FileStream.cpp',
  'LA32FloatWaveGenerator.cpp',
  'LA32Ramp.cpp',
  'LA32WaveGenerator.cpp',
  'MidiStreamParser.cpp',
  'Part.cpp',
  'Partial.cpp',
  'PartialManager.cpp',
  'Poly.cpp',
  'ROMInfo.cpp',
  'SampleRateConverter.cpp',
  'Synth.cpp',
  'TVA.cpp',
  'TVF.cpp',
  'TVP.cpp',
  'Tables.cpp',
  'VersionTagging.cpp',
  'c_interface/c_interface.cpp',
  'sha1/sha1.cpp',
  'srchelper/InternalResampler.cpp',
  'srchelper/srctools/src/FIRResampler.cpp',
  'srchelper/srctools/src/IIR2xResampler.cpp',
  'srchelper/srctools/src/LinearResampler.cpp',
  'srchelper/srctools/src/ResamplerModel.cpp',
  'srchelper/srctools/src/SincResampler.cpp',
)
