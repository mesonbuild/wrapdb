soundtouch_sources = files(
    'AAFilter.cpp',
    'BPMDetect.cpp',
    'cpu_detect_x86.cpp',
    'FIFOSampleBuffer.cpp',
    'FIRFilter.cpp',
    'InterpolateCubic.cpp',
    'InterpolateLinear.cpp',
    'InterpolateShannon.cpp',
    'mmx_optimized.cpp',
    'PeakFinder.cpp',
    'RateTransposer.cpp',
    'SoundTouch.cpp',
    'sse_optimized.cpp',
    'TDStretch.cpp',
)

# This library requires WINDOWS_EXPORT_ALL_SYMBOLS to export all the relevant
# classes. That's beyond mindbending to do for C++, see how it's done:
# https://github.com/Kitware/CMake/blob/master/Source/bindexplib.cxx#L237
if system in ['windows', 'cygwin']
    soundtouch_lib = static_library(
        'SoundTouch',
        soundtouch_sources,
        cpp_args: soundtouch_args,
        include_directories: soundtouch_includes,
        install: true
    )
else
    soundtouch_lib = library(
        'SoundTouch',
        soundtouch_sources,
        cpp_args: soundtouch_args,
        include_directories: soundtouch_includes,
        version: meson.project_version(),
        # DO NOT CHANGE THIS, SEE ABOVE!
        # Also the Android.mk file was designed for GCC, not Clang (API 17+)
        gnu_symbol_visibility: 'default',
        install: true
    )
endif

soundtouch_dep = declare_dependency(
    link_with: soundtouch_lib,
    include_directories: soundtouch_includes,
)
