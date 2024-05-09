project('libjpeg-turbo', 'c',
  version : '3.0.3',
  license : 'bsd-like',
  meson_version : '>= 0.64.0')

pkg = import('pkgconfig')
python = find_program('python3')

cc = meson.get_compiler('c')
host_system = host_machine.system()
host_cpu = host_machine.cpu_family()

cdata = configuration_data()
cdata.set('CMAKE_PROJECT_NAME', meson.project_name())
cdata.set('VERSION', meson.project_version())
cdata.set('COPYRIGHT_YEAR', '1991-2024')

jpeg_lib_version = 80
so_major = jpeg_lib_version / 10
so_age = 3
so_minor = 2
so_version = '@0@.@1@.@2@'.format(so_major, so_age, so_minor)
vs_defs = 'win/jpeg8.def'

version_arr = meson.project_version().split('.')
version_major = version_arr[0]
version_minor = version_arr[1]
version_revision = version_arr[2]

# Add padding to build an integer: 2.1.0 -> 2001000
if version_major.to_int() < 10
  version_major += '00'
elif version_major.to_int() < 100
  version_major += '0'
endif

if version_minor.to_int() < 10
  version_minor += '00'
elif version_minor.to_int() < 100
  version_minor += '0'
endif

cdata.set('JPEG_LIB_VERSION', jpeg_lib_version)
cdata.set('LIBJPEG_TURBO_VERSION_NUMBER', version_major + version_minor + version_revision)

cdata.set('C_ARITH_CODING_SUPPORTED', true)
cdata.set('D_ARITH_CODING_SUPPORTED', true)

check_headers = ['local.h', 'stddef.h', 'stdlib.h', 'sys/types.h']
if cc.get_id() == 'msvc'
  check_headers += 'intrin.h'
endif

foreach header : check_headers
  have_header = cc.has_header(header)
  cdata.set('HAVE_' + header.underscorify().to_upper(), have_header)
  cdata.set('NEED_' + header.underscorify().to_upper(), have_header)
endforeach

has_memset = cc.has_header_symbol('string.h', 'memset')
has_memcpy = cc.has_header_symbol('string.h', 'memcpy')
cdata.set('NEED_BSD_STRINGS', not has_memset or not has_memcpy)

size_t = cc.sizeof('size_t')
unsigned_long = cc.sizeof('unsigned long')
cdata.set('SIZE_T', size_t)
cdata.set('HAVE_UNSIGNED_CHAR', cc.sizeof('unsigned char') != -1)
cdata.set('HAVE_UNSIGNED_SHORT', cc.sizeof('unsigned short') != -1)
if size_t == unsigned_long
  cdata.set('HAVE_BUILTIN_CTZL', cc.has_function('__builtin_ctzl'))
endif

code = 'int main(void) { typedef struct undefined_structure *undef_struct_ptr;  undef_struct_ptr ptr = 0;  return ptr != 0; }'
cdata.set('INCOMPLETE_TYPES_BROKEN', not cc.links(code))

if meson.can_run_host_binaries()
  code = '''
      #include <stdio.h>
      #include <stdlib.h>
      static int is_shifting_signed (long arg) {
        long res = arg >> 4;
        if (res == -0x7F7E80CL)
          return 1; /* right shift is signed */
        /* see if unsigned-shift hack will fix it. */
        /* we can't just test exact value since it depends on width of long... */
        res |= 0xFFFFFFFFL << (32-4);
        if (res == -0x7F7E80CL)
          return 0; /* right shift is unsigned */
        printf(\"Right shift isn't acting as I expect it to.\\\\n\");
        printf(\"I fear the JPEG software will not work at all.\\\\n\\\\n\");
        return 0; /* try it with unsigned anyway */
      }
      int main (void) {
        exit(is_shifting_signed(-0x7F7E80B1L));
      }
  '''
  cdata.set('RIGHT_SHIFT_IS_UNSIGNED', cc.run(code).returncode() == 0)
else
  cdata.set('RIGHT_SHIFT_IS_UNSIGNED', false)
endif

p = run_command(python, '-c', 'import datetime; print(datetime.datetime.now().strftime("%Y%m%d"))', check: true)
cdata.set('BUILD', p.stdout().strip())

if cc.get_id() == 'msvc'
  cdata.set('THREAD_LOCAL', '__declspec(thread)')
else
  cdata.set('THREAD_LOCAL', '__thread')
endif

cdata.set(
  'HIDDEN',
  cc.has_function_attribute('visibility:hidden')
  ? '__attribute__((visibility("hidden")))'
  : '',
)

if get_option('force_inline')
  if cc.get_id() == 'msvc'
    cdata.set('INLINE', '__forceinline')
  else
    cdata.set('INLINE', 'inline __attribute__((always_inline))')
  endif
else
  cdata.set('INLINE', 'inline')
endif

if host_system == 'windows'
  add_project_arguments('-DDLLDEFINE', language: 'c')
endif

incdir = include_directories('.')

subdir('simd')
cdata.set('WITH_SIMD', have_simd)

jconfig_h = configure_file(input: 'jconfig.h.in',
  output: 'jconfig.h',
  format: 'cmake@',
  configuration: cdata)

configure_file(input: 'jconfigint.h.in',
  output: 'jconfigint.h',
  format: 'cmake@',
  configuration: cdata)

configure_file(input: 'jversion.h.in',
  output: 'jversion.h',
  format: 'cmake@',
  configuration: cdata)

install_headers('jmorecfg.h', 'jerror.h', 'jpeglib.h', jconfig_h)

jpeg16_sources = [
  'jcapistd.c', 'jccolor.c', 'jcdiffct.c', 'jclossls.c', 'jcmainct.c',
  'jcprepct.c', 'jcsample.c', 'jdapistd.c', 'jdcolor.c', 'jddiffct.c',
  'jdlossls.c', 'jdmainct.c', 'jdpostct.c', 'jdsample.c', 'jutils.c',
]
jpeg12_sources = [
  jpeg16_sources, 'jccoefct.c', 'jcdctmgr.c', 'jdcoefct.c', 'jddctmgr.c',
  'jdmerge.c', 'jfdctfst.c', 'jfdctint.c', 'jidctflt.c', 'jidctfst.c',
  'jidctint.c', 'jidctred.c', 'jquant1.c', 'jquant2.c',
]
sources = [
  jpeg12_sources, 'jcapimin.c', 'jchuff.c', 'jcicc.c', 'jcinit.c',
  'jclhuff.c', 'jcmarker.c', 'jcmaster.c', 'jcomapi.c', 'jcparam.c',
  'jcphuff.c', 'jctrans.c', 'jdapimin.c', 'jdatadst.c', 'jdatasrc.c',
  'jdhuff.c', 'jdicc.c', 'jdinput.c', 'jdlhuff.c', 'jdmarker.c',
  'jdmaster.c', 'jdphuff.c', 'jdtrans.c', 'jerror.c', 'jfdctflt.c',
  'jmemmgr.c', 'jmemnobs.c', 'jpeg_nbits.c',
  # TODO: `with_arith_dec` / `with_arith_enc` only.
  'jaricom.c',
  # TODO: `with_arith_enc` only
  'jcarith.c',
  # TODO: `with_arith_dec` only
  'jdarith.c',
]

jpeg12 = static_library('jpeg12', jpeg12_sources,
  c_args: ['-DBITS_IN_JSAMPLE=12'],
  pic: get_option('default_library') != 'static',
)
jpeg16 = static_library('jpeg16', jpeg16_sources,
  c_args: ['-DBITS_IN_JSAMPLE=16'],
  pic: get_option('default_library') != 'static',
)
jpeg = library('jpeg', sources,
  link_with: [jpeg12, jpeg16, simd],
  soversion: so_version,
  vs_module_defs: vs_defs,
  install: true,
)

pkg.generate(jpeg, description: 'A SIMD-accelerated JPEG codec that provides the libjpeg API', name: 'libjpeg')

jpeg_dep = declare_dependency(
  include_directories: incdir,
  link_with: jpeg
)

meson.override_dependency('libjpeg', jpeg_dep)

if get_option('jpeg-turbo').allowed()

  install_headers('turbojpeg.h')

  turbojpeg12 = static_library(
    'turbojpeg12',
    ['rdppm.c', 'wrppm.c'],
    c_args: ['-DBITS_IN_JSAMPLE=12', '-DPPM_SUPPORTED'],
  )

  turbojpeg16 = static_library(
    'turbojpeg16',
    ['rdppm.c', 'wrppm.c'],
    c_args: ['-DBITS_IN_JSAMPLE=16', '-DPPM_SUPPORTED'],
  )

  turbojpeg = library(
    'turbojpeg',
    sources + [
      'turbojpeg.c',
      'transupp.c',
      'jdatadst-tj.c',
      'jdatasrc-tj.c',
      'rdbmp.c',
      'rdppm.c',
      'wrbmp.c',
      'wrppm.c',
    ],
    c_args: ['-DBMP_SUPPORTED', '-DPPM_SUPPORTED'],
    install: true,
    link_with: [jpeg12, jpeg16, simd, turbojpeg12, turbojpeg16],
    soversion: '0.3.0',
  )

  pkg.generate(
    turbojpeg,
    description: 'A SIMD-accelerated JPEG codec that provides the TurboJPEG API',
    name: 'libturbojpeg',
  )

  turbojpeg_dep = declare_dependency(
    include_directories: incdir,
    link_with: turbojpeg,
  )

  meson.override_dependency('libturbojpeg', turbojpeg_dep)

endif

if get_option(
  'tests',
).require(
  get_option('jpeg-turbo').allowed(),
  error_message: 'jpeg-turbo feature needed',
).allowed()

  tjunittest = executable(
    'tjunittest',
    [
      'tjunittest.c',
      'tjutil.c',
      'md5/md5.c',
      'md5/md5hl.c',
    ],
    dependencies: turbojpeg_dep,
  )

  foreach _test, _args : {
    'tjunittest'                 : '',
    'tjunittest-alloc'           : '-alloc',
    'tjunittest-yuv'             : '-yuv',
    'tjunittest-yuv-alloc'       : '-yuv -alloc',
    'tjunittest-yuv-nopad'       : '-yuv -noyuvpad',
    'tjunittest-lossless'        : '-lossless',
    'tjunittest-lossless-alloc'  : '-lossless -alloc',
    'tjunittest-bmp'             : '-bmp',
    'tjunittest12'               : '-precision 12',
    'tjunittest12-alloc'         : '-precision 12 -alloc',
    'tjunittest12-lossless'      : '-precision 12 -lossless',
    'tjunittest12-lossless-alloc': '-precision 12 -lossless -alloc',
    'tjunittest12-bmp'           : '-precision 12 -bmp',
    'tjunittest16-lossless'      : '-precision 16',
    'tjunittest16-lossless-alloc': '-precision 16 -alloc',
    'tjunittest16-bmp'           : '-precision 16 -bmp',
  }
    test(
      _test,
      tjunittest,
      args: _args.split(),
      timeout: 60,
    )
  endforeach

endif
