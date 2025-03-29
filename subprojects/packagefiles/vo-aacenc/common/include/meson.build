aacencinclude_headers = files(
  'cmnMemory.h',
  'voAAC.h',
  'voAMRWB.h',
  'voAudio.h',
  'voIndex.h',
  'voMem.h',
  'voType.h',
)

libvo_aacenc_includes += [include_directories('.')]

# MSVC defines intptr_t in stddef.h, but LLVM does in stdint.h
if cc.get_define('_MSC_VER') != '' and cc.get_define('__clang__') != ''
  libvo_aacenc_sources += [
    configure_file(
      input: 'stddef.h.in',
      output: 'stddef.h',
      copy: true,
    ),
  ]
endif
