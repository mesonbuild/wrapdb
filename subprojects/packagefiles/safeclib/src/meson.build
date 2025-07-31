misc_funcs = ['bsearch_s', 'qsort_s']
misc_sources = files()
foreach f : misc_funcs
  if not cc.has_function(f)
    misc_sources += files('misc/@0@.c'.format(f))
  endif
endforeach

extwchar_funcs = [
  'wcsstr_s',
  'wcsfc_s',
  'wcscoll_s',
  'wcsicmp_s',
  'towfc_s',
  'wcscmp_s',
  'wcsnatcmp_s',
  'wcsstr',
  'wcsncmp_s',
  'wmemcmp_s',
  'wcsnset_s',
  'wcsset_s',
  'wcsupr_s',
  'wcslwr_s',
  'wcsnorm_s',
]
extwchar_sources = files('extwchar/towctrans.c')
foreach f : extwchar_funcs
  if not cc.has_function(f)
    extwchar_sources += files('extwchar/@0@.c'.format(f))
  endif
endforeach

io_funcs = [
  'fscanf_s',
  'sscanf_s',
  'fprintf_s',
  'gets_s',
  'tmpfile_s',
  'vsscanf_s',
  'vfscanf_s',
  'fopen_s',
  'freopen_s',
  'printf_s',
  'vfprintf_s',
  'vprintf_s',
  'scanf_s',
  'vscanf_s',
]
if get_option('unsafe').allowed()
  io_funcs += ['tmpnam_s']
endif
io_sources = files()
foreach f : io_funcs
  if not cc.has_function(f)
    io_sources += files('io/@0@.c'.format(f))
  endif
endforeach

extmem_funcs = [
  'memchr_s',
  'memmove16_s',
  'memcmp16_s',
  'memzero16_s',
  'memcpy16_s',
  'memset32_s',
  'memset16_s',
  'memcmp_s',
  'memcpy32_s',
  'timingsafe_bcmp',
  'memzero_s',
  'memzero32_s',
  'timingsafe_memcmp',
  'memcmp32_s',
  'memrchr_s',
  'memccpy_s',
  'memmove32_s',
]
extmem_sources = files()
foreach f : extmem_funcs
  if not cc.has_function(f)
    extmem_sources += files('extmem/@0@.c'.format(f))
  endif
endforeach

extstr_funcs = [
  'strlastsame_s',
  'strlastdiff_s',
  'strcoll_s',
  'strchr_s',
  'strismixedcase_s',
  'strstr_s',
  'strpbrk_s',
  'strispassword_s',
  'strisuppercase_s',
  'strremovews_s',
  'strzero_s',
  'strrchr_s',
  'strtouppercase_s',
  'strcasecmp_s',
  'strljustify_s',
  'strfirstsame_s',
  'strcmpfld_s',
  'strfirstdiff_s',
  'strspn_s',
  'strfirstchar_s',
  'strprefix_s',
  'strisascii_s',
  'strnterminate_s',
  'strset_s',
  'strisalphanumeric_s',
  'strcpyfldin_s',
  'strcmp_s',
  'strnset_s',
  'strcpyfldout_s',
  'strisdigit_s',
  'stpncpy_s',
  'strcpyfld_s',
  'strislowercase_s',
  'strcspn_s',
  'strnatcmp_s',
  'stpcpy_s',
  'strtolowercase_s',
  'strlastchar_s',
  'strcasestr_s',
  'strishex_s',
]
extstr_sources = files()
foreach f : extstr_funcs
  if not cc.has_function(f)
    extstr_sources += files('extstr/@0@.c'.format(f))
  endif
endforeach

wchar_funcs = [
  'vsnwprintf_s',
  'swprintf_s',
  'wcstok_s',
  'wcrtomb_s',
  'mbsrtowcs_s',
  'fwscanf_s',
  'wcsnlen_s',
  'swscanf_s',
  'vfwprintf_s',
  'vwprintf_s',
  'snwprintf_s',
  'wcstombs_s',
  'wctomb_s',
  'vfwscanf_s',
  'vwscanf_s',
  'vswscanf_s',
  'fwprintf_s',
  'wprintf_s',
  'wcscat_s',
  'vswprintf_s',
  'wcsrtombs_s',
  'wcsncat_s',
  'wmemmove_s',
  'mbstowcs_s',
  'wcscpy_s',
  'wcsncpy_s',
  'wmemcpy_s',
  'wscanf_s',
]
wchar_sources = files()
foreach f : wchar_funcs
  if not cc.has_function(f)
    wchar_sources += files('wchar/@0@.c'.format(f))
  endif
endforeach

os_funcs = ['localtime_s', 'ctime_s', 'asctime_s', 'getenv_s', 'gmtime_s']
os_sources = files()
foreach f : os_funcs
  if not cc.has_function(f)
    os_sources += files('os/@0@.c'.format(f))
  endif
endforeach

str_funcs = [
  'snprintf_s',
  'sprintf_s',
  'strerror_s',
  'safe_str_constraint',
  'strtok_s',
  'strnlen_s',
  'strcat_s',
  'strncat_s',
  'strncpy_s',
  'vsprintf_s',
  'strcpy_s',
  'vsnprintf_s',
]
str_sources = files()
foreach f : str_funcs
  if not cc.has_function(f)
    str_sources += files('str/@0@.c'.format(f))
  endif
endforeach

mem_funcs = [
  'mem_primitives_lib',
  'memmove_s',
  'memset_s',
  'safe_mem_constraint',
  'memcpy_s',
]
mem_sources = files()
foreach f : mem_funcs
  if not cc.has_function(f)
    mem_sources += files('mem/@0@.c'.format(f))
  endif
endforeach

handler_sources = files('abort_handler_s.c', 'ignore_handler_s.c')

sources = io_sources + os_sources + str_sources + mem_sources + handler_sources + misc_sources
if get_option('extensions').allowed()
  sources += extmem_sources
  sources += extstr_sources
  if get_option('wchar').allowed()
    sources += extwchar_sources
  endif
endif
if get_option('wchar').allowed()
  sources += wchar_sources
endif

configure_file(
  output: 'config.h',
  configuration: conf,
)

libsafec = library(
  'safec',
  sources,
  install: true,
  include_directories: inc,
)
