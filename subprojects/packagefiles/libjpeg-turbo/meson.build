project('libjpeg-turbo', 'c',
  version : '3.1.0',
  license : 'bsd-like',
  meson_version : '>= 0.64.0',
)

pkg = import('pkgconfig')
python = import('python').find_installation()

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
vs_defs = files('win/jpeg8.def')[0]

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

incdir = include_directories('src')

subdir('simd')
cdata.set('WITH_SIMD', have_simd)

subdir('src')
