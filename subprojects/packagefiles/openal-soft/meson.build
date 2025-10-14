project(
  'openal-soft',
  'cpp',
  license: 'LGPL-2.1-or-later',
  version: '1.24.3',
  meson_version: '>=0.58',
)

cpp_std = 'cpp_std=c++17'

cpp = meson.get_compiler('cpp')
if meson.version().version_compare('>= 0.62')
  dl_dep = dependency(
    'dl',
    required: false,
  )
else
  dl_dep = cpp.find_library(
    'dl',
    required: false,
  )
endif

fmt_dep = dependency('fmt')

if host_machine.system() != 'windows'
  thread_dep = dependency('threads')
else
  thread_dep = declare_dependency()
endif

alsa_dep = dependency(
  'alsa',
  required: get_option('alsa'),
)
apple_dep = dependency(
  'appleframeworks',
  modules: ['AudioToolbox', 'CoreAudio', 'CoreFoundation'],
  required: host_machine.system() == 'darwin',
)
jack_dep = dependency(
  'jack',
  required: get_option('jack'),
)
mm_dep = cpp.find_library(
  'winmm',
  required: get_option('winmm'),
)
oboe_dep = dependency(
  'oboe',
  required: get_option('oboe'),
)
opensl_dep = dependency(
  'opensl',
  required: get_option('opensl'),
)
oss_dep = dependency(
  'oss',
  required: get_option('oss'),
)
pipewire_dep = dependency(
  'libpipewire-0.3',
  required: get_option('pipewire'),
)
portaudio_dep = dependency(
  'portaudio',
  required: get_option('portaudio'),
)
pulseaudio_dep = dependency(
  'libpulse',
  required: get_option('pulseaudio'),
)
rtkit_dep = dependency(
  'dbus-1',
  required: get_option('rtkit'),
)
sdl2_dep = dependency(
  'sdl2',
  required: get_option('sdl2'),
)
sndio_dep = dependency(
  'sndio',
  required: get_option('sndio'),
)
solaris_dep = dependency(
  'audioio',
  required: get_option('solaris'),
)

if host_machine.system() == 'windows'
  add_project_arguments(
    '-DNOMINMAX',
    language: 'cpp',
  )
  if cpp.get_argument_syntax() == 'msvc'
    add_project_arguments(
      '-D_CRT_SECURE_NO_WARNINGS',
      language: 'cpp',
    )
    add_project_arguments(
      '/wd5051',
      language: 'cpp',
    )
  endif
endif

add_project_arguments(
  '-DRESTRICT=__restrict',
  language: 'cpp',
)

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
  'common/alassert.cpp',
  'common/alcomplex.cpp',
  'common/alsem.cpp',
  'common/alstring.cpp',
  'common/althrd_setname.cpp',
  'common/dynload.cpp',
  'common/pffft.cpp',
  'common/polyphase_resampler.cpp',
  'common/ringbuffer.cpp',
  'common/strutils.cpp',
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
  'core/fpu_ctrl.cpp',
  'core/helpers.cpp',
  'core/hrtf.cpp',
  'core/logging.cpp',
  'core/mastering.cpp',
  'core/mixer.cpp',
  'core/mixer/mixer_c.cpp',
  'core/storage_formats.cpp',
  'core/uhjfilter.cpp',
  'core/uiddefs.cpp',
  'core/voice.cpp',
)

openal_sources = files(
  'al/auxeffectslot.cpp',
  'al/buffer.cpp',
  'al/debug.cpp',
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
  'alc/events.cpp',
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
cdata.set('HAVE_ALSA', alsa_dep.found())
cdata.set('HAVE_COREAUDIO', apple_dep.found())
cdata.set('HAVE_JACK', jack_dep.found())
cdata.set('HAVE_OBOE', oboe_dep.found())
cdata.set('HAVE_OPENSL', opensl_dep.found())
cdata.set('HAVE_OSS', oss_dep.found())
cdata.set('HAVE_PIPEWIRE', pipewire_dep.found())
cdata.set('HAVE_PORTAUDIO', portaudio_dep.found())
cdata.set('HAVE_PULSEAUDIO', pulseaudio_dep.found())
cdata.set('HAVE_SDL2', sdl2_dep.found())
cdata.set('HAVE_SNDIO', sndio_dep.found())
cdata.set('HAVE_SOLARIS', solaris_dep.found())
cdata.set('HAVE_WINMM', mm_dep.found())
cdata.set(
  'HAVE_DSOUND',
  cpp.has_header(
    'dsound.h',
    dependencies: mm_dep,
  ),
)
cdata.set(
  'HAVE_WASAPI',
  cpp.has_header(
    'wasapi.h',
    dependencies: mm_dep,
  ),
)
configure_file(
  input: 'config_backends.h.in',
  output: 'config_backends.h',
  format: 'cmake',
  configuration: cdata,
)

foreach b : [
  'alsa',
  'coreaudio',
  'jack',
  'opensl',
  'oss',
  'pipewire',
  'portaudio',
  'pulseaudio',
  'sdl2',
  'sndio',
  'solaris',
  'winmm',
  'dsound',
  'wasapi',
]
  if cdata.get('HAVE_@0@'.format(b.to_upper()))
    alc_sources += 'alc/backends/@0@.cpp'.format(b)
  endif
endforeach

cdata = configuration_data()
cdata.set('HAVE_SSE', cpp.check_header('xmmintrin.h'))
cdata.set('HAVE_SSE2', cpp.check_header('emmintrin.h'))
cdata.set('HAVE_SSE3', cpp.check_header('pmmintrin.h'))
cdata.set('HAVE_SSE4_1', cpp.check_header('smmintrin.h'))
cdata.set(
  'HAVE_SSE_INTRINSICS',
  cpp.has_header_symbol('xmmintrin.h', '_mm_pause'),
)
cdata.set('HAVE_NEON', cpp.check_header('arm_neon.h'))

if cdata.get('HAVE_SSE')
  openal_args += cpp.get_supported_arguments('-msse', '-mfpmath=sse')
  core_sources += 'core/mixer/mixer_sse.cpp'
endif

if cdata.get('HAVE_SSE2')
  openal_args += cpp.get_supported_arguments('-msse2')
  core_sources += 'core/mixer/mixer_sse2.cpp'
endif

if cdata.get('HAVE_SSE3')
  openal_args += cpp.get_supported_arguments('-msse3')
  core_sources += 'core/mixer/mixer_sse3.cpp'
endif

if cdata.get('HAVE_SSE4_1')
  openal_args += cpp.get_supported_arguments('-msse4.1')
  core_sources += 'core/mixer/mixer_sse41.cpp'
endif

if cdata.get('HAVE_NEON')
  if cpp.sizeof('void*') == 4
    openal_args += cpp.get_supported_arguments('-mfpu=neon')
  endif
  core_sources += 'core/mixer/mixer_neon.cpp'
endif

configure_file(
  input: 'config_simd.h.in',
  output: 'config_simd.h',
  format: 'cmake',
  configuration: cdata,
)

cdata = configuration_data()

#ignore for now
cdata.set('ALSOFT_UWP', false)

cdata.set('ALSOFT_EAX', host_machine.system() == 'windows')
if cdata.get('ALSOFT_EAX')
  alc_sources += files(
    'al/eax/api.cpp',
    'al/eax/call.cpp',
    'al/eax/exception.cpp',
    'al/eax/fx_slot_index.cpp',
    'al/eax/fx_slots.cpp',
    'al/eax/utils.cpp',
  )
endif

cdata.set('HAVE_RTKIT', rtkit_dep.found())
if cdata.get('HAVE_RTKIT')
  alc_sources += files('core/dbus_wrap.cpp', 'core/rtkit.cpp')
endif

headers = {
  'dlfcn.h': dl_dep,
  'guiddef.h': [],
  'pthread_np.h': [],
}
foreach h, d : headers
  if cpp.has_header(
    h,
    dependencies: d,
  )
    cdata.set('HAVE_@0@'.format(h.underscorify().to_upper()), 1)
  endif
endforeach

#needs to be check_header for LLVM as well as MinGW
cdata.set('HAVE_CPUID_H', cpp.check_header('cpuid.h'))
cdata.set('HAVE_INTRIN_H', cpp.check_header('intrin.h'))

functions = {
  #need to check for non windows because meson wrongly detects its presence under MinGW
  'proc_pidpath': [],
  'pthread_setschedparam': thread_dep,
  'pthread_setname_np': thread_dep,
  'pthread_set_name_np': thread_dep,
}
foreach f, d : functions
  if cpp.has_function(
    f,
    dependencies: d,
  )
    cdata.set('HAVE_@0@'.format(f.underscorify().to_upper()), 1)
  endif
endforeach

cdata.set('HAVE_CPUID_INTRINSIC', cpp.get_argument_syntax() == 'msvc')
cdata.set(
  'HAVE_GCC_GET_CPUID',
  cpp.has_function(
    '__get_cpuid',
    prefix: '#include <cpuid.h>',
  ),
)

if cpp.has_function_attribute('force_align_arg_pointer')
  cdata.set('ALSOFT_FORCE_ALIGN', '__attribute__((force_align_arg_pointer))')
else
  cdata.set('ALSOFT_FORCE_ALIGN', '')
endif

cdata.set('ALSOFT_EMBED_HRTF_DATA', true)
cdata.set('ALSOFT_INSTALL_DATADIR', get_option('prefix') / get_option('datadir'))

configure_file(
  input: 'config.h.in',
  output: 'config.h',
  format: 'cmake@',
  configuration: cdata,
)

vdata = configuration_data()
vdata.set(
  'GIT_BRANCH',
  run_command(
    'git',
    'rev-parse',
    '--symbolic-full-name',
    'HEAD',
    check: false,
    capture: true,
  ).stdout().strip(),
)
vdata.set(
  'GIT_COMMIT_HASH',
  run_command(
    'git',
    'rev-parse',
    'HEAD',
    check: false,
    capture: true,
  ).stdout().strip(),
)
vdata.set('LIB_VERSION', meson.project_version())
vdata.set('LIB_VERSION_NUM', meson.project_version().replace('.', ','))

configure_file(
  input: 'version.h.in',
  output: 'version.h',
  format: 'cmake',
  configuration: vdata,
)

if cpp.links(
  '#include <atomic>\n#include <bitset>\nint main(){std::atomic<std::bitset<3>> b;std::atomic_is_lock_free(&b);}',
)
  atomic_dep = dependency(
    '',
    required: false,
  )
else
  atomic_dep = cpp.find_library(
    'atomic',
    required: false,
  )
endif

common_lib = static_library(
  'common',
  common_sources,
  override_options: cpp_std,
  pic: true,
  dependencies: fmt_dep,
)

common_inc = include_directories('.')

common_dep = declare_dependency(
  link_with: common_lib,
  include_directories: common_inc,
  dependencies: [atomic_dep, fmt_dep],
)

openal_inc = include_directories('common', 'include', 'include/AL')

openal_lib = library(
  'openal',
  core_sources,
  openal_sources,
  alc_sources,
  hrtf_h,
  cpp_args: openal_args,
  override_options: cpp_std,
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
  dependencies: [atomic_dep, fmt_dep],
  compile_args: get_option('default_library') == 'static' ? '-DAL_LIBTYPE_STATIC' : [],
)

meson.override_dependency('openal', openal_dep)

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
