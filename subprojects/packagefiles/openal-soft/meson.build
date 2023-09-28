project(
  'openal-soft',
  'cpp',
  version: '1.23.1',
  meson_version: '>=0.58',
  default_options: ['cpp_std=c++14', 'c_std=c11'],
)

cpp = meson.get_compiler('cpp')
dl_dep = cpp.find_library('dl', required: false)
thread_dep = dependency('threads')
alsa_dep = dependency('alsa', required: get_option('alsa'))
apple_dep = dependency('appleframeworks', modules: ['AudioToolbox', 'CoreAudio', 'CoreFoundation'], required: host_machine.system() == 'darwin')
jack_dep = dependency('jack', required: get_option('jack'))
mm_dep = cpp.find_library('winmm', required: get_option('winmm'))
opensl_dep = dependency('opensl', required: get_option('opensl'))
oss_dep = dependency('oss', required: get_option('oss'))
pipewire_dep = dependency('libpipewire-0.3', required: get_option('pipewire'))
portaudio_dep = dependency('portaudio', required: get_option('portaudio'))
pulseaudio_dep = dependency('libpulse', required: get_option('pulseaudio'))
rtkit_dep = dependency('dbus-1', required: get_option('rtkit'))
sdl2_dep = dependency('sdl2', required: get_option('sdl2'))
sndio_dep = dependency('sndio', required: get_option('sndio'))
solaris_dep = dependency('audioio', required: get_option('solaris'))

if host_machine.system() == 'windows'
  add_project_arguments('-DNOMINMAX', language: 'cpp')
  if cpp.get_argument_syntax() == 'msvc'
    add_project_arguments('-D_CRT_SECURE_NO_WARNINGS', language: 'cpp')
    add_project_arguments('/wd5051', language: 'cpp')
  endif
endif

add_project_arguments('-DRESTRICT=__restrict', language: 'cpp')

openal_args = []
api = ''
if get_option('default_library') != 'static'
  if cpp.has_function_attribute('dllexport')
    api = '__declspec(dllexport)'
  elif cpp.has_function_attribute('visibility:protected') and host_machine.system() != 'darwin'
    api = '__attribute__((visibility("protected")))'
  elif cpp.has_function_attribute('visibility:default')
    api = '__attribute__((visibility("default")))'
  endif
else
  openal_args += '-DAL_LIBTYPE_STATIC'
endif

openal_args += ['-DAL_BUILD_LIBRARY', '-DAL_ALEXT_PROTOTYPES']
openal_args += '-DAL_API=@0@'.format(api)
openal_args += '-DALC_API=@0@'.format(api)

common_sources = files(
  'common/alcomplex.cpp',
  'common/alfstream.cpp',
  'common/almalloc.cpp',
  'common/alstring.cpp',
  'common/dynload.cpp',
  'common/polyphase_resampler.cpp',
  'common/ringbuffer.cpp',
  'common/strutils.cpp',
  'common/threads.cpp',
)

core_sources = files(
  'core/ambdec.cpp',
  'core/ambidefs.cpp',
  'core/bformatdec.cpp',
  'core/bs2b.cpp',
  'core/bsinc_tables.cpp',
  'core/buffer_storage.cpp',
  'core/context.cpp',
  'core/converter.cpp',
  'core/cpu_caps.cpp',
  'core/cubic_tables.cpp',
  'core/devformat.cpp',
  'core/device.cpp',
  'core/effectslot.cpp',
  'core/except.cpp',
  'core/filters/biquad.cpp',
  'core/filters/nfc.cpp',
  'core/filters/splitter.cpp',
  'core/fmt_traits.cpp',
  'core/fpu_ctrl.cpp',
  'core/helpers.cpp',
  'core/hrtf.cpp',
  'core/logging.cpp',
  'core/mastering.cpp',
  'core/mixer.cpp',
  'core/mixer/mixer_c.cpp',
  'core/uhjfilter.cpp',
  'core/uiddefs.cpp',
  'core/voice.cpp',
)

openal_sources = files(
  'al/auxeffectslot.cpp',
  'al/buffer.cpp',
  'al/effect.cpp',
  'al/effects/autowah.cpp',
  'al/effects/chorus.cpp',
  'al/effects/compressor.cpp',
  'al/effects/convolution.cpp',
  'al/effects/dedicated.cpp',
  'al/effects/distortion.cpp',
  'al/effects/echo.cpp',
  'al/effects/effects.cpp',
  'al/effects/equalizer.cpp',
  'al/effects/fshifter.cpp',
  'al/effects/modulator.cpp',
  'al/effects/null.cpp',
  'al/effects/pshifter.cpp',
  'al/effects/reverb.cpp',
  'al/effects/vmorpher.cpp',
  'al/error.cpp',
  'al/event.cpp',
  'al/extension.cpp',
  'al/filter.cpp',
  'al/listener.cpp',
  'al/source.cpp',
  'al/state.cpp',
)

alc_sources = files(
  'alc/alc.cpp',
  'alc/alconfig.cpp',
  'alc/alu.cpp',
  'alc/context.cpp',
  'alc/device.cpp',
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
  'alc/panning.cpp',
)

alc_sources += files(
  'alc/backends/base.cpp',
  'alc/backends/loopback.cpp',
  'alc/backends/null.cpp',
  'alc/backends/wave.cpp',
  # Default backends, always available
)

hrtf_h = custom_target(
  'hrtf-header',
  output: 'default_hrtf.txt',
  input: 'hrtf/Default HRTF.mhr',
  command: ['hexify.py', '@INPUT@', '@OUTPUT@', 'default_hrtf'],
)

cdata = configuration_data()
cdata.set('HAVE_WAVE', true)
cdata.set('HAVE_LIBDL', dl_dep.found())
cdata.set('HAVE_ALSA', alsa_dep.found())
cdata.set('HAVE_COREAUDIO', apple_dep.found())
cdata.set('HAVE_JACK', jack_dep.found())
cdata.set('HAVE_OPENSL', opensl_dep.found())
cdata.set('HAVE_OSS', oss_dep.found())
cdata.set('HAVE_PIPEWIRE', pipewire_dep.found())
cdata.set('HAVE_PORTAUDIO', portaudio_dep.found())
cdata.set('HAVE_PULSEAUDIO', pulseaudio_dep.found())
cdata.set('HAVE_RTKIT', rtkit_dep.found())
cdata.set('HAVE_SDL2', sdl2_dep.found())
cdata.set('HAVE_SNDIO', sndio_dep.found())
cdata.set('HAVE_SOLARIS', solaris_dep.found())
cdata.set('HAVE_WINMM', mm_dep.found())
cdata.set('HAVE_DSOUND', cpp.has_header('dsound.h'))
cdata.set('HAVE_WASAPI', cpp.has_header('wasapi.h'))

#ignore for now
cdata.set('ALSOFT_EAX', false)
cdata.set('HAVE_OBOE', false)

foreach b : ['alsa', 'coreaudio', 'jack', 'opensl', 'oss', 'pipewire', 'portaudio', 'pulseaudio', 'sdl2', 'sndio', 'solaris', 'winmm', 'dsound', 'wasapi']
  if cdata.get('HAVE_@0@'.format(b.to_upper()))
    alc_sources += 'alc/backends/@0@.cpp'.format(b)
  endif
endforeach

if cdata.get('HAVE_RTKIT')
  alc_sources += files('core/dbus_wrap.cpp', 'core/rtkit.cpp')
endif

foreach h : ['dlfcn.h', 'guiddef.h', 'initguid.h', 'malloc.h', 'pthread_np.h']
  cdata.set('HAVE_@0@'.format(h.underscorify().to_upper()), cpp.has_header(h))
endforeach

#needs to be check_header for LLVM as well as MinGW
cdata.set('HAVE_CPUID_H', cpp.check_header('cpuid.h'))
cdata.set('HAVE_INTRIN_H', cpp.check_header('intrin.h'))
cdata.set('HAVE_SSE', cpp.check_header('xmmintrin.h'))
cdata.set('HAVE_SSE2', cpp.check_header('emmintrin.h'))
cdata.set('HAVE_SSE3', cpp.check_header('pmmintrin.h'))
cdata.set('HAVE_SSE4_1', cpp.check_header('smmintrin.h'))
cdata.set('HAVE_NEON', cpp.check_header('arm_neon.h'))

#need to check for non windows because meson wrongly detects its presence under MinGW
cdata.set('HAVE_POSIX_MEMALIGN', cpp.has_function('posix_memalign') and host_machine.system() != 'windows')
cdata.set('HAVE__ALIGNED_MALLOC', cpp.has_function('_aligned_malloc'))
cdata.set('HAVE_PROC_PIDPATH', cpp.has_function('proc_pidpath'))
cdata.set('HAVE_PTHREAD_SETSCHEDPARAM', cpp.has_function('pthread_setschedparam', dependencies: thread_dep))
cdata.set('HAVE_PTHREAD_SETNAME_NP', cpp.has_function('pthread_setname_np', dependencies: thread_dep))
cdata.set('HAVE_PTHREAD_SET_NAME_NP', cpp.has_function('pthread_set_name_np', dependencies: thread_dep))
cdata.set('HAVE_GETOPT', cpp.has_function('getopt'))

cdata.set('HAVE_CPUID_INTRINSIC', cpp.get_argument_syntax() == 'msvc')
cdata.set('HAVE_GCC_GET_CPUID', cpp.has_function('__get_cpuid', prefix: '#include <cpuid.h>'))
cdata.set('HAVE_SSE_INTRINSICS', cpp.has_header_symbol('xmmintrin.h', '_mm_pause'))

cdata.set('ALSOFT_EMBED_HRTF_DATA', true)
cdata.set('ALSOFT_INSTALL_DATADIR', get_option('prefix') / get_option('datadir'))

configure_file(input: 'config.h.in', output: 'config.h', format: 'cmake@', configuration: cdata)

vdata = configuration_data()
vdata.set('GIT_BRANCH', run_command('git', 'rev-parse', '--symbolic-full-name', 'HEAD', check: false, capture: true).stdout().strip())
vdata.set('GIT_COMMIT_HASH', run_command('git', 'rev-parse', 'HEAD', check: false, capture: true).stdout().strip())
vdata.set('LIB_VERSION', meson.project_version())
vdata.set('LIB_VERSION_NUM', meson.project_version().replace('.', ','))

configure_file(input: 'version.h.in', output: 'version.h', format: 'cmake', configuration: vdata)

if cdata.get('HAVE_SSE')
  openal_args += cpp.get_supported_arguments('-msse', '/arch:SSE', '-mfpmath=sse')
  core_sources += 'core/mixer/mixer_sse.cpp'
endif

if cdata.get('HAVE_SSE2')
  openal_args += cpp.get_supported_arguments('-msse2', '/arch:SSE2')
  core_sources += 'core/mixer/mixer_sse2.cpp'
endif

if cdata.get('HAVE_SSE3')
  openal_args += cpp.get_supported_arguments('-msse3', '/arch:SSE3')
  core_sources += 'core/mixer/mixer_sse3.cpp'
endif

if cdata.get('HAVE_SSE4_1')
  openal_args += cpp.get_supported_arguments('-msse4.1', '/arch:SSE4.1')
  core_sources += 'core/mixer/mixer_sse41.cpp'
endif

if cdata.get('HAVE_NEON')
  if cpp.sizeof('void*') == 4
    openal_args += cpp.get_supported_arguments('-mfpu=neon')
  endif
  core_sources += 'core/mixer/mixer_neon.cpp'
endif

common_lib = static_library(
  'common',
  common_sources,
)

common_inc = include_directories('.')

common_dep = declare_dependency(
  link_with: common_lib,
  include_directories: common_inc,
)

openal_inc = include_directories('common', 'include', 'include/AL')

openal_lib = library(
  'openal',
  core_sources,
  openal_sources,
  alc_sources,
  hrtf_h,
  cpp_args: openal_args,
  dependencies: [
    common_dep,
    dl_dep,
    thread_dep,
    alsa_dep,
    apple_dep,
    jack_dep,
    mm_dep,
    opensl_dep,
    oss_dep,
    pipewire_dep,
    portaudio_dep,
    pulseaudio_dep,
    rtkit_dep,
    sdl2_dep,
    sndio_dep,
    solaris_dep,
  ],
  include_directories: openal_inc,
  gnu_symbol_visibility: 'hidden',
  version: meson.project_version(),
  soversion: host_machine.system() == 'windows' ? '' : '1',
  install: true,
)

openal_dep = declare_dependency(
  link_with: openal_lib,
  include_directories: openal_inc,
  dependencies: common_dep,
  compile_args: get_option('default_library') == 'static' ? '-DAL_LIBTYPE_STATIC' : [],
)

if meson.version().version_compare('>=0.54.0')
  meson.override_dependency('openal', openal_dep)
endif

install_headers(
  'include/AL/al.h',
  'include/AL/alc.h',
  'include/AL/alext.h',
  'include/AL/efx-creative.h',
  'include/AL/efx-presets.h',
  'include/AL/efx.h',
  subdir: 'AL',
)

install_data(
  'alsoftrc.sample',
  install_dir: get_option('datadir') / 'openal',
)

install_data(
  'hrtf/Default HRTF.mhr',
  install_dir: get_option('datadir') / 'openal' / 'hrft',
)

install_data(
  'presets/hexagon.ambdec',
  'presets/itu5.1-nocenter.ambdec',
  'presets/itu5.1.ambdec',
  'presets/rectangle.ambdec',
  'presets/square.ambdec',
  'presets/3D7.1.ambdec',
  'presets/presets.txt',
  install_dir: get_option('datadir') / 'openal' / 'presets',
)

pconf = import('pkgconfig')
pconf.generate(
  openal_lib,
  description: 'OpenAL is a cross-platform 3D audio API',
  subdirs: 'AL',
)

subdir('utils')
