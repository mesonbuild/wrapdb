project(
  'safeclib',
  'c',
  version: '3.9.1',
  license: 'MIT',
  meson_version: '>=1.3.0',
)

cc = meson.get_compiler('c')

conf = configuration_data()

conf.set(
  'INSERT_BOOL_SUPPORT',
  cc.check_header('stdbool.h') ? '#include <stdbool.h>' : '',
)
conf.set(
  'INSERT_INTTYPES_H',
  cc.check_header('inttypes.h') ? '#include <inttypes.h>' : '',
)
conf.set(
  'INSERT_STDINT_H',
  cc.check_header('stdint.h') ? '#include <stdint.h>' : '',
)
conf.set(
  'INSERT_SYS_TYPES_H',
  cc.check_header('sys/types.h') ? '#include <sys/types.h>' : '',
)
conf.set(
  'INSERT_ERRNO_H',
  cc.check_header('errno.h') ? '#include <errno.h>' : '',
)

funcs = ('vswprintf vswscanf mbsrtowcs ' +
'__bnd_chk_ptr_bounds __bnd_set_ptr_bounds __bnd_null_ptr_bounds ' +
'__memcpy_chk __memmove_chk __memset_chk ' +
'__strcpy_chk __strncpy_chk __strcat_chk __strncat_chk ' +
'__printf_chk __sprintf_chk __snprintf_chk ' +
'__vfprintf_chk __vfwprintf_chk __vsprintf_chk __vsnprintf_chk ' +
'__vsscanf_chk ' +
'memset strcmp strcasecmp strcasestr strcspn strpbrk strspn ' +
'strnstr strnlen strrchr memrchr strstr bcmp secure_getenv timingsafe_memcmp ' +
'timingsafe_bcmp explicit_bzero explicit_memset ' +
'asctime_r ctime_r gmtime_r localtime_r memccpy stpcpy stpncpy strerror ' +
'fileno ftruncate isinfl ' +
'wmemchr wmemcmp wcscmp wcsstr ' +
'vswprintf vsnwprintf vswscanf mbsrtowcs mbstowcs iswdigit iswspace ' +
'towlower towupper towctrans ' +
'_memcpy_s_chk _memmove_s_chk _memset_s_chk _memcmp_s_chk ' +
'_strcpy_s_chk _strncpy_s_chk _strcat_s_chk _strncat_s_chk _strnlen_s_chk ' +
'_printf_s_chk _sprintf_s_chk _snprintf_s_chk ' +
'_vfprintf_s_chk _vsprintf_s_chk _vsnprintf_s_chk ' +
'memset_s memcpy_s memmove_s memzero_s memchr_s memrchr_s memccpy_s ' +
'sprintf_s strcat_s strcpy_s strncat_s strncpy_s ' +
'strnlen_s strtok_s strerror_s vsprintf_s tmpnam_s snprintf_s vsnprintf_s ' +
'strspn_s strset_s strchr_s strrchr_s strstr_s strzero_s strnset_s ' +
'stpcpy_s stpncpy_s ' +
'sscanf_s fscanf_s scanf_s vfscanf_s ' +
'vsscanf_s vscanf_s printf_s fprintf_s tmpfile_s vfprintf_s vprintf_s ' +
'fopen_s freopen_s gets_s bsearch_s qsort_s gmtime_s localtime_s ' +
'asctime_s ctime_s getenv_s feenableexcept ' +
'mbsrtowcs_s mbstowcs_s wcsrtombs_s wcstombs_s ' +
'wcrtomb_s wctomb_s wcsnlen_s wcscpy_s wcsncpy_s wcscat_s wcsncat_s ' +
'wmemcpy_s wmemmove_s wcstok_s vswprintf_s swprintf_s vfwprintf_s ' +
'vwprintf_s wprintf_s snwprintf_s fwprintf_s swscanf_s vswscanf_s wscanf_s ' +
'vfwscanf_s fwscanf_s vwscanf_s vsnwprintf_s wcsstr_s wmemcmp_s ' +
'wcscmp_s wcsncmp_s wcsicmp_s wcsset_s wcsnset_s wcscoll_s wcslwr_s ' +
'wcsupr_s towfc_s wcsfc_s ' +
'_swprintf_s_chk _vfwprintf_s_chk').split(' ')
foreach f : funcs
  conf.set('HAVE_@0@'.format(f.underscorify().to_upper()), cc.has_function(f))
endforeach

headers = [
  'sys/time.h',
  'stdlib.h',
  'memory.h',
  'ctype.h',
  'malloc.h',
  'string.h',
  'limits.h',
  'stddef.h',
  'unistd.h',
  'float.h',
  'math.h',
  'sys/types.h',
  'inttypes.h',
  'stdint.h',
  'errno.h',
  'wchar.h',
  'langinfo.h',
  'valgrind/valgrind.h',
  'fenv.h',
  'intrin.h',
  'xmmintrin.h',
  'emmintrin.h',
  'x86intrin.h',
  'arm_neon.h',
  'arm_acle.h',
  'mmintrin.h',
  'altivec.h',
  'spe.h',
  'mbarrier.h',
]
foreach h : headers
  conf.set('HAVE_@0@'.format(h.underscorify().to_upper()), cc.check_header(h))
endforeach

sizeofs = ['size_t', 'wchar_t', 'time_t']
foreach s : sizeofs
  conf.set('SIZEOF_@0@'.format(s.underscorify().to_upper()), cc.sizeof(s))
endforeach

conf.set(
  'HAVE_TM_GMTOFF',
  cc.has_member(
    'struct tm',
    'tm_gmtoff',
    prefix: '#include <time.h>',
  ),
)
conf.set('HAVE_FLOAT128', cc.compiles('int main(void) { __float128 x = 1.0Q; }'))
conf.set(
  'HAVE_TOWUPPER_OK',
  cc.run(
    '''
#include <wctype.h>
int main(void) {
  return (towupper(0x1C80) == 0x412
     && towupper(0xB5) == 0x3BC
     && towupper(0x432) == 0x1C80)
       ? 0 : 1;
}
''',
  ).returncode() == 0,
)
conf.set(
  'HAVE_STRNSTR_OK',
  cc.run(
    '''
#include <string.h>
int main(void) {
  return strnstr("%s %n", "%n", 6) ? 0 : 1;
}
''',
  ).returncode() == 0 ? '1' : false,
)

conf.set(
  'PRINTF_DISABLE_SUPPORT_FLOAT',
  get_option('float').allowed() ? false : 1,
)
conf.set(
  'PRINTF_DISABLE_SUPPORT_EXPONENTIAL',
  get_option('float-exp').allowed() ? false : 1,
)
conf.set(
  'PRINTF_DISABLE_SUPPORT_LONG_LONG',
  get_option('long-long').allowed() ? false : 1,
)
conf.set(
  'PRINTF_DISABLE_SUPPORT_LONG_DOUBLE',
  get_option('long-double').allowed() ? false : 1,
)
conf.set(
  'PRINTF_DISABLE_SUPPORT_PTRDIFF_T',
  get_option('printf-ptrdiff').allowed() ? false : 1,
)

conf.set(
  'INSERT_EXTS',
  get_option('extensions').allowed() ? '#undef SAFECLIB_DISABLE_EXTENSIONS' : '#define SAFECLIB_DISABLE_EXTENSIONS 1',
)
conf.set(
  'INSERT_NULLSLACK',
  get_option('nullslack').allowed() ? '#define SAFECLIB_STR_NULL_SLACK 1' : '#undef SAFECLIB_STR_NULL_SLACK',
)
conf.set(
  'INSERT_CONSTRAINT_HANDLER',
  get_option('constraint-handler').allowed() ? '#undef SAFECLIB_DISABLE_CONSTRAINT_HANDLER' : '#define SAFECLIB_DISABLE_CONSTRAINT_HANDLER 1',
)
conf.set(
  'INSERT_UNSAFE',
  get_option('unsafe').allowed() ? '#define SAFECLIB_ENABLE_UNSAFE 1' : '#undef SAFECLIB_ENABLE_UNSAFE',
)
haveBuiltinObjectSize = cc.has_function('__builtin_object_size')
conf.set('HAVE___BUILTIN_OBJECT_SIZE', haveBuiltinObjectSize ? '1' : false)
conf.set(
  'INSERT_OBJECT_SIZE',
  haveBuiltinObjectSize ? '#define HAVE___BUILTIN_OBJECT_SIZE 1' : '',
)
conf.set(
  'INSERT_WARN_DMAX',
  (get_option('warn-dmax').allowed() or get_option('error-dmax').allowed()) and haveBuiltinObjectSize ? '#define HAVE_WARN_DMAX 1' : '',
)
conf.set(
  'INSERT_ERROR_DMAX',
  get_option('error-dmax').allowed() and haveBuiltinObjectSize ? '#define HAVE_ERROR_DMAX 1' : '',
)
conf.set(
  'INSERT_DEFAULT_HANDLER',
  get_option('default-handler') == 'no' ? '#undef SAFECLIB_DEFAULT_HANDLER' : '#define SAFECLIB_DEFAULT_HANDLER @0@_handler_s'.format(
    get_option('default-handler'),
  ),
)
conf.set(
  'INSERT_CONSTANT_P',
  cc.has_function('__builtin_constant_p') ? '#define HAVE___BUILTIN_CONSTANT_P 1' : '#undef HAVE___BUILTIN_CONSTANT_P',
)
conf.set('INSERT_DISABLE_DLLIMPORT', '#undef DISABLE_DLLIMPORT')
conf.set(
  'INSERT_DISABLE_WCHAR',
  get_option('wchar').allowed() ? '#undef SAFECLIB_DISABLE_WCHAR' : '#define SAFECLIB_DISABLE_WCHAR 1',
)
conf.set('INSERT_SAFECLIB_HAVE_C99', '#define SAFECLIB_HAVE_C99 1')
conf.set('RSIZE_MAX_MEM', get_option('memmax'))
conf.set('RSIZE_MAX_STR', get_option('strmax'))
conf.set(
  'FALLBACK_ERRNO_T',
  cc.has_type(
    'errno_t',
    prefix: '#include <errno.h>',
  ) ? '' : 'typedef int errno_t;',
)
conf.set('HAVE_ATTRIBUTE_FORMAT_WPRINTF', '0')
conf.set('HAVE_ATTRIBUTE_FORMAT_WSCANF', '0')
conf.set('STDC_HEADERS', true)
conf.set('configure_input', '')

subdir('include')
subdir('src')

libsafec_dep = declare_dependency(
  include_directories: inc,
  link_with: libsafec,
)
