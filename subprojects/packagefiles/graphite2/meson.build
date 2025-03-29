project(
  'graphite2',
  'cpp',
  version: '1.3.14',
  default_options: ['cpp_std=c++17'],
)

if get_option('default_library') == 'static'
  extra_args = ['-DGRAPHITE2_STATIC']
else
  extra_args = ['-DGRAPHITE2_EXPORTING']
endif

graphite2_lib = library(
  'graphite2',
  'src/CmapCache.cpp',
  'src/Code.cpp',
  'src/Collider.cpp',
  'src/Decompressor.cpp',
  'src/Face.cpp',
  'src/FeatureMap.cpp',
  'src/FileFace.cpp',
  'src/Font.cpp',
  'src/GlyphCache.cpp',
  'src/GlyphFace.cpp',
  'src/Intervals.cpp',
  'src/Justifier.cpp',
  'src/NameTable.cpp',
  'src/Pass.cpp',
  'src/Position.cpp',
  'src/Segment.cpp',
  'src/Silf.cpp',
  'src/Slot.cpp',
  'src/Sparse.cpp',
  'src/TtfUtil.cpp',
  'src/UtfCodec.cpp',
  'src/call_machine.cpp',
  #  'src/direct_machine.cpp',
  'src/gr_char_info.cpp',
  'src/gr_face.cpp',
  'src/gr_features.cpp',
  'src/gr_font.cpp',
  'src/gr_logging.cpp',
  'src/gr_segment.cpp',
  'src/gr_slot.cpp',
  'src/json.cpp',
  include_directories: ['include', 'src'],
  cpp_args: extra_args,
  gnu_symbol_visibility: 'hidden',
)

graphite2_dep = declare_dependency(
  include_directories: 'include',
  link_with: graphite2_lib,
)
