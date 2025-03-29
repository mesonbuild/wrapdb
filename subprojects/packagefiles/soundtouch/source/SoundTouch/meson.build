soundtouch_sources = files(
  'AAFilter.cpp',
  'BPMDetect.cpp',
  'FIFOSampleBuffer.cpp',
  'FIRFilter.cpp',
  'InterpolateCubic.cpp',
  'InterpolateLinear.cpp',
  'InterpolateShannon.cpp',
  'PeakFinder.cpp',
  'RateTransposer.cpp',
  'SoundTouch.cpp',
  'TDStretch.cpp',
  'cpu_detect_x86.cpp',
  'mmx_optimized.cpp',
  'sse_optimized.cpp',
)

# This library requires WINDOWS_EXPORT_ALL_SYMBOLS to export all the relevant
# classes under MSVC. That's beyond mindbending to do for C++, see how it's done:
# https://github.com/Kitware/CMake/blob/master/Source/bindexplib.cxx#L237
if cpp.get_linker_id() in ['link', 'lld-link']  # MSVC relies on __declspec
  soundtouch_lib = static_library(
    'SoundTouch',
    soundtouch_sources,
    cpp_args: soundtouch_args,
    dependencies: deps,
    include_directories: soundtouch_includes,
    install: true,
  )
else  # GCC and Clang etc. do not
  soundtouch_lib = library(
    'SoundTouch',
    soundtouch_sources,
    cpp_args: soundtouch_args,
    dependencies: deps,
    include_directories: soundtouch_includes,
    version: meson.project_version(),
    # DO NOT CHANGE THIS, SEE ABOVE!
    # Also the Android.mk file was designed for GCC, not Clang (API 17+)
    gnu_symbol_visibility: 'default',
    install: true,
  )
endif

soundtouch_dep = declare_dependency(
  link_with: soundtouch_lib,
  include_directories: soundtouch_includes,
)
