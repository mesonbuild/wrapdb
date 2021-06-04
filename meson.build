project('openal-soft', 'cpp', 'c',
        version: '1.21.0',
        default_options: ['cpp_std=c++17', 'c_std=c11'])

if host_machine.system() != 'windows'
    error('Currently only Windows is supported by this wrap.')
endif

cpp = meson.get_compiler('cpp')

if cpp.get_id() != 'msvc'
    error('Currently only the VS compiler is supported.')
endif

mm_dep = cpp.find_library('winmm', required: false)

add_project_arguments('-DNOMINMAX', '-DRESTRICT=__restrict', language: 'cpp')

common_sources = files(
    'common/albyte.h',
    'common/alcomplex.cpp',
    'common/alcomplex.h',
    'common/alexcpt.cpp',
    'common/alexcpt.h',
    'common/alfstream.cpp',
    'common/alfstream.h',
    'common/almalloc.cpp',
    'common/almalloc.h',
    'common/alnumeric.h',
    'common/aloptional.h',
    'common/alspan.h',
    'common/alstring.cpp',
    'common/alstring.h',
    'common/atomic.h',
    'common/dynload.cpp',
    'common/dynload.h',
    'common/endiantest.h',
    'common/intrusive_ptr.h',
    'common/math_defs.h',
    'common/opthelpers.h',
    'common/polyphase_resampler.cpp',
    'common/polyphase_resampler.h',
    'common/pragmadefs.h',
    'common/strutils.cpp',
    'common/strutils.h',
    'common/threads.cpp',
    'common/threads.h',
    'common/vecmat.h',
    'common/vector.h',
)

openal_sources = files(
    'al/auxeffectslot.cpp',
    'al/auxeffectslot.h',
    'al/buffer.cpp',
    'al/buffer.h',
    'al/effect.cpp',
    'al/effect.h',
    'al/error.cpp',
    'al/event.cpp',
    'al/event.h',
    'al/extension.cpp',
    'al/filter.cpp',
    'al/filter.h',
    'al/listener.cpp',
    'al/listener.h',
    'al/source.cpp',
    'al/source.h',
    'al/state.cpp',
)

alc_sources = files(
    'alc/alc.cpp',
    'alc/alcmain.h',
    'alc/alu.cpp',
    'alc/alu.h',
    'alc/alconfig.cpp',
    'alc/alconfig.h',
    'alc/alcontext.h',
    'alc/ambdec.cpp',
    'alc/ambdec.h',
    'alc/ambidefs.h',
    'alc/bformatdec.cpp',
    'alc/bformatdec.h',
    'alc/bs2b.cpp',
    'alc/bs2b.h',
    'alc/bsinc_defs.h',
    'alc/bsinc_tables.cpp',
    'alc/bsinc_tables.h',
    'alc/bufferline.h',
    'alc/buffer_storage.cpp',
    'alc/buffer_storage.h',
    'alc/compat.h',
    'alc/converter.cpp',
    'alc/converter.h',
    'alc/cpu_caps.cpp',
    'alc/cpu_caps.h',
    'alc/devformat.h',
    'alc/effects/base.h',
    'alc/effects/autowah.cpp',
    'alc/effects/chorus.cpp',
    'alc/effects/compressor.cpp',
    'alc/effects/convolution.cpp',
    'alc/effects/dedicated.cpp',
    'alc/effects/distortion.cpp',
    'alc/effects/echo.cpp',
    'alc/effects/equalizer.cpp',
    'alc/effects/fshifter.cpp',
    'alc/effects/modulator.cpp',
    'alc/effects/null.cpp',
    'alc/effects/pshifter.cpp',
    'alc/effects/reverb.cpp',
    'alc/effects/vmorpher.cpp',
    'alc/filters/biquad.h',
    'alc/filters/biquad.cpp',
    'alc/filters/nfc.cpp',
    'alc/filters/nfc.h',
    'alc/filters/splitter.cpp',
    'alc/filters/splitter.h',
    'alc/fmt_traits.cpp',
    'alc/fmt_traits.h',
    'alc/fpu_ctrl.cpp',
    'alc/fpu_ctrl.h',
    'alc/front_stablizer.h',
    'alc/helpers.cpp',
    'alc/hrtf.cpp',
    'alc/hrtf.h',
    'alc/inprogext.h',
    'alc/logging.h',
    'alc/mastering.cpp',
    'alc/mastering.h',
    'alc/panning.cpp',
    'alc/ringbuffer.cpp',
    'alc/ringbuffer.h',
    'alc/uhjfilter.cpp',
    'alc/uhjfilter.h',
    'alc/uiddefs.cpp',
    'alc/voice.cpp',
    'alc/voice.h',
    'alc/mixer/defs.h',
    'alc/mixer/hrtfbase.h',
    'alc/mixer/mixer_c.cpp',
    'alc/mixer/mixer_sse.cpp',
    'alc/mixer/mixer_sse2.cpp',
    'alc/mixer/mixer_sse41.cpp',
    'alc/backends/wasapi.cpp',
    'alc/backends/dsound.cpp',
    'alc/backends/wave.cpp',
    'alc/backends/winmm.cpp',
)

alc_sources += files(
    'alc/backends/base.cpp',
    # Default backends, always available
    'alc/backends/loopback.cpp',
    'alc/backends/null.cpp',
)

hrtf_h = custom_target('hrtf-header',
    output: 'hrtf_default.h',
    input: 'hrtf/Default HRTF.mhr',
    command: [find_program('hexify.py'), '@INPUT@', '@OUTPUT@', 'hrtf_default'])

cdata = configuration_data()

cdata.set('AL_API', '__declspec(dllexport)')
cdata.set('ALC_API', '__declspec(dllexport)')

cdata.set('HAVE__ALIGNED_MALLOC', true)
cdata.set('ALSOFT_EMBED_HRTF_DATA', true)

cdata.set('HAVE_SSE', true)
cdata.set('HAVE_SSE2', true)
cdata.set('HAVE_SSE3', true)
cdata.set('HAVE_SSE4_1', true)

cdata.set('HAVE_WINMM', true)
cdata.set('HAVE_DSOUND', true)
cdata.set('HAVE_WASAPI', true)
cdata.set('HAVE_WAVE', true)

cdata.set('HAVE_MALLOC_H', true)
cdata.set('HAVE_INTRIN_H', true)
cdata.set('HAVE_GUIDDEF_H', true)
cdata.set('HAVE_CPUID_INTRINSIC', true)
cdata.set('HAVE_SSE_INTRINSICS', true)

cdata.set_quoted('ALSOFT_VERSION', meson.project_version())
cdata.set('ALSOFT_VERSION_NUM', '1,21,0,0')
cdata.set_quoted('ALSOFT_GIT_BRANCH', 'UNKNOWN')
cdata.set_quoted('ALSOFT_GIT_COMMIT_HASH', 'unknown')


configure_file(input: 'config.h.meson',
    output: 'config.h',
    configuration: cdata)

configure_file(input: 'version.h.meson',
    output: 'version.h',
    configuration: cdata)

openal_lib = shared_library('openal',
    common_sources,
    openal_sources,
    alc_sources,
    hrtf_h,
    cpp_args: ['-DAL_BUILD_LIBRARY', '-DAL_ALEXT_PROTOTYPES'],
    include_directories: ['include', 'common', 'alc'],
    dependencies: [mm_dep],
    )

openal_dep = declare_dependency(include_directories: 'include/AL', link_with: openal_lib)
