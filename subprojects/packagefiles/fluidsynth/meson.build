project(
  'fluidsynth',
  'c',
  'cpp',
  version: '2.3.3',
  license: 'LGPL-2.1-or-later',
  default_options: ['b_ndebug=if-release'],
  meson_version: '>= 0.54.1',
)

cc = meson.get_compiler('c')

summary('Build type', get_option('buildtype'), section: 'Build Summary')
summary('Install prefix', get_option('prefix'), section: 'Build Summary')

# Due to symbol visibility issues, don't allow building 'both' library
# types on MSVC
if get_option('default_library') == 'both' and cc.get_argument_syntax() == 'msvc'
  error('default_library=both not supported when compiling with MSVC')
endif

# Is a shared library being built?
is_shared_lib = get_option('default_library') == 'shared'

# Set global WIN32 define if windows
if host_machine.system() == 'windows'
  add_project_arguments('-DWIN32=1', language: ['c', 'cpp'])
endif

# Detect if compiling in an MSYS2-based MinGW/Clang environment
host_is_msys2 = host_machine.system() == 'windows' and cc.get_argument_syntax() == 'gcc'

# config file
#
# TODO there are many, many more options to set/detect in upstream template
#      see meson_options.txt for list

conf = configuration_data()

conf.set('PACKAGE', meson.project_name())
conf.set(
  'DEFAULT_SOUNDFONT',
  get_option('datadir') / 'soundfonts' / 'default.sf2',
)
conf.set(
  'TEST_SOUNDFONT',
  meson.current_source_dir() / 'sf2' / 'VintageDreamsWaves-v2.sf2',
)
conf.set(
  'TEST_SOUNDFONT_SF3',
  meson.current_source_dir() / 'sf2' / 'VintageDreamsWaves-v2.sf3',
)
conf.set('STDC_HEADERS', 1)

if host_machine.system() == 'darwin'
  conf.set('DARWIN', 1)
endif

if host_machine.endian() == 'big'
  conf.set('WORDS_BIGENDIAN', 1)
endif

if get_option('enable-floats')
  conf.set('WITH_FLOAT', 1)
endif
summary(
  'Samples type',
  conf.has('WITH_FLOAT').to_string('float', 'double'),
  section: 'Developer nerds info',
)

headers_to_check = [
  'arpa/inet.h',
  'errno.h',
  'fcntl.h',
  'getopt.h',
  'inttypes.h',
  'io.h',
  'limits.h',
  'linux/soundcard.h',
  'machine/soundcard.h',
  'math.h',
  'netinet/in.h',
  'netinet/tcp.h',
  'pthread.h',
  'signal.h',
  'stdarg.h',
  'stdint.h',
  'stdio.h',
  'stdlib.h',
  'string.h',
  'strings.h',
  'sys/mman.h',
  'sys/socket.h',
  'sys/soundcard.h',
  'sys/stat.h',
  'sys/time.h',
  'sys/types.h',
  'unistd.h',
  'windows.h',
]

foreach h : headers_to_check
  if cc.has_header(h)
    conf.set10('HAVE_' + h.underscorify().to_upper(), true)
  endif
endforeach

if cc.has_function('inet_ntop', prefix: '#include <arpa/inet.h>')
  conf.set('HAVE_INETNTOP', 1) # lib uses ifdef for this one
endif

foreach fun : ['sinf', 'cosf', 'fabsf', 'powf', 'sqrtf', 'logf']
  if cc.has_function(fun)
    conf.set10('HAVE_' + fun.to_upper(), true)
  endif
endforeach

# Some compilers such as msvc may not support VLA, the following test
# is adapted from upstream CMake
vla_code = 'int main(int argc, char *argv[]){int arr[argc]; return 0;}'
if cc.compiles(vla_code, name: 'VLA check')
  conf.set('SUPPORTS_VLA', 1)
endif

# external dependencies

m_dep = cc.find_library('m', required: false)
glib_dep = dependency('glib-2.0', static: get_option('try-static-deps'))
gthread_dep = dependency('gthread-2.0', static: get_option('try-static-deps'))
if cc.get_argument_syntax() != 'msvc'
  openmp_dep = dependency('openmp', required: get_option('openmp'), version: '>=4.0')
else
  openmp_dep = dependency('', required: false)
endif

ext_deps = [m_dep, glib_dep, gthread_dep, openmp_dep]

# Windows specific options
lib_args = []
if host_machine.system() == 'windows'
  if is_shared_lib
    lib_args = ['-DFLUIDSYNTH_DLL_EXPORTS']
  endif
  # Specific workaround on MSYS2 to obtain static dependencies of intl, such as iconv
  # This is required as of meson 0.59
  if get_option('try-static-deps') and host_is_msys2
    ext_deps += [dependency('intl', static: true)]
  endif
endif

if openmp_dep.found()
  conf.set('HAVE_OPENMP', 1)
endif
summary(
  'OpenMP 4.0',
  openmp_dep.found().to_string('yes', 'no'),
  section: 'Developer nerds info',
)

if get_option('enable-threads')
  conf.set('ENABLE_MIXER_THREADS', 1)
endif
summary(
  'Multi-threading',
  conf.has('ENABLE_MIXER_THREADS').to_string('yes', 'no'),
  section: 'Developer nerds info',
)

# config.h

configure_file(
  input: 'src/config.cmake',
  output: 'config.h',
  format: 'cmake@',
  configuration: conf,
)

# fluidsynth lib

subdir('include')
subdir('include/fluidsynth')
subdir('src')

lib_includes = [include_directories('.', 'include'), src_includes]
dep_includes = include_directories('include')

fluidsynth_lib = library(
  'fluidsynth',
  fluidsynth_sources,
  gen_tables,
  dependencies: ext_deps,
  gnu_symbol_visibility: 'hidden',
  include_directories: lib_includes,
  c_args: lib_args,
  cpp_args: lib_args,
)

fluidsynth_obj = fluidsynth_lib.extract_objects(fluidsynth_sources)

fluidsynth_dep = declare_dependency(
  link_with: fluidsynth_lib,
  include_directories: dep_includes,
)

# unit tests
if get_option('tests')
  subdir('test')
endif
