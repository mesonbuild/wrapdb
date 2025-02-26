project(
  'cfitsio',
  'c',
  version: '4.5.0',
  meson_version: '>=1.1.0',
  license: 'CFITSIO',
  license_files: ['licenses/License.txt'],
)
SOVERSION = 10

cc = meson.get_compiler('c')
libm = cc.find_library('m', required: false)
zlib = dependency('zlib', method: 'pkg-config', required:true, fallback: ['zlib', 'zlib_dep'])
deps = [libm,zlib]
has_fortran = false

if host_machine.system() == 'windows'
  has_fortran = false
  add_project_arguments('-Dcfitsio_EXPORTS', language: 'c')
else
  has_fortran = add_languages(
    'fortran',
    native: false,
    required: get_option('fortran'),
  )

  bzip2 = cc.find_library('bz2', required: false)
  if not bzip2.found()
    bzip2_proj = subproject('bzip2')
    bzip2 = bzip2_proj.get_variable('bzip2_dep')
  endif
  if bzip2.found()
    add_project_arguments('-DHAVE_BZIP2=1', language: 'c')
    deps += bzip2
  endif

  threads = dependency('threads', required: get_option('reentrant'))
  if threads.found()
    add_project_arguments('-D_REENTRANT', language: 'c')
    deps += threads
  endif

  curl = dependency(
    'libcurl',
    method: 'pkg-config',
    required: get_option('curl'),
  )
  if curl.found()
    add_project_arguments('-DCFITSIO_HAVE_CURL', language: 'c')
    deps += curl
  endif
endif

if get_option('hera')
  add_project_arguments('-DBUILD_HERA=1', language: 'c')
endif

if cc.has_header('unistd.h')
  add_project_arguments('-DHAVE_UNISTD_H', language: 'c')
  if cc.has_header_symbol('unistd.h', 'ftruncate')
     add_project_arguments('-DHAVE_FTRUNCATE', language: 'c')
  endif
else
  add_project_arguments('-DYY_NO_UNISTD_H', language: 'c')
endif

if cc.has_function('gethostbyname') and cc.has_function('connect')
  add_project_arguments('-DHAVE_NET_SERVICES', language: 'c')
  if cc.has_header_symbol('stdio.h', 'fmemopen')
    add_project_arguments('-DHAVE_FMEMOPEN', language: 'c')
  endif
endif

shmem_prefix = [
  '#include <sys/ipc.h>',
  '#include <sys/shm.h>',
  '#include <sys/sem.h>',
]
flock_prefix = ['#include <sys/flock.h>']

have_shmem_services = true
foreach func : ['shmat', 'shmdt', 'shmget', 'semget']
  have_shmem_services = have_shmem_services and cc.has_function(
    func,
    prefix: shmem_prefix,
  )
endforeach
if have_shmem_services
  add_project_arguments('-DHAVE_SHMEM_SERVICES', language: 'c')
  if cc.has_type('flock_t', prefix: flock_prefix)
    add_project_arguments('-DHAVE_FLOCK_T', language: 'c')
  endif
  if cc.has_type('union semun', prefix: shmem_prefix)
    add_project_arguments('-DHAVE_UNION_SEMUN', language: 'c')
  endif
endif

if cc.has_type('long long')
  add_project_arguments('-DHAVE_LONGLONG', language: 'c')
endif

install_headers('fitsio.h', 'fitsio2.h', 'longnam.h')

libcfitsio_SOURCES = [
  'buffers.c',
  'cfileio.c',
  'checksum.c',
  'drvrfile.c',
  'drvrmem.c',
  'drvrnet.c',
  'drvrsmem.c',
  'editcol.c',
  'edithdu.c',
  'eval_l.c',
  'eval_y.c',
  'eval_f.c',
  'fitscore.c',
  'getcol.c',
  'getcolb.c',
  'getcold.c',
  'getcole.c',
  'getcoli.c',
  'getcolj.c',
  'getcolk.c',
  'getcoll.c',
  'getcols.c',
  'getcolsb.c',
  'getcoluk.c',
  'getcolui.c',
  'getcoluj.c',
  'getkey.c',
  'group.c',
  'grparser.c',
  'histo.c',
  'iraffits.c',
  'modkey.c',
  'putcol.c',
  'putcolb.c',
  'putcold.c',
  'putcole.c',
  'putcoli.c',
  'putcolj.c',
  'putcolk.c',
  'putcoluk.c',
  'putcoll.c',
  'putcols.c',
  'putcolsb.c',
  'putcolu.c',
  'putcolui.c',
  'putcoluj.c',
  'putkey.c',
  'region.c',
  'scalnull.c',
  'swapproc.c',
  'wcssub.c',
  'wcsutil.c',
  'imcompress.c',
  'quantize.c',
  'ricecomp.c',
  'pliocomp.c',
  'fits_hcompress.c',
  'fits_hdecompress.c',
  'simplerng.c',
  'zcompress.c',
  'zuncompress.c',
]

if has_fortran
  libcfitsio_SOURCES += [
    'f77_wrap1.c',
    'f77_wrap2.c',
    'f77_wrap3.c',
    'f77_wrap4.c',
  ]
endif

libcfitsio = library(
  'cfitsio',
  libcfitsio_SOURCES,
  dependencies: deps,
  version: meson.project_version(),
  soversion: SOVERSION,
  install: true,
)
message('libcfitsio: '+libcfitsio.name()+' '+libcfitsio.full_path())

cfitsio_dep = declare_dependency(
  link_with: libcfitsio,
)

pkg = import('pkgconfig')
pkg.generate(
  libraries: libcfitsio,
  version: meson.project_version(),
  name: 'cfitsio',
  description: 'FITS File Subroutine Library',
  url: 'https://heasarc.gsfc.nasa.gov/fitsio/',
)

if get_option('utils')
  executable(
    'fitscopy',
    'utilities/fitscopy.c',
    dependencies: cfitsio_dep,
    install: true,
  )
  executable(
    'fitsverify',
    'utilities/ftverify.c',
    'utilities/fvrf_data.c',
    'utilities/fvrf_file.c',
    'utilities/fvrf_head.c',
    'utilities/fvrf_key.c',
    'utilities/fvrf_misc.c',
    c_args: '-DSTANDALONE',
    dependencies: cfitsio_dep,
    install: true,
  )
  executable(
    'fpack',
    'utilities/fpack.c',
    'utilities/fpackutil.c',
    dependencies: [libm, cfitsio_dep],
    install: true,
  )
  executable(
    'funpack',
    'utilities/funpack.c',
    'utilities/fpackutil.c',
    dependencies: [libm,cfitsio_dep],
    link_with: libcfitsio,
    install: true,
  )
endif

test(
  'cookbook',
  executable('cookbook', 'utilities/cookbook.c', link_with: libcfitsio),
)
cmp = find_program('test_compare.py')
testprog = executable(
  'testprog',
  'utilities/testprog.c',
  dependencies: cfitsio_dep,
)
test('testprog', cmp, args: [testprog, meson.current_source_dir()])
if has_fortran
  testf77 = executable(
    'testf77',
    'utilities/testf77.f',
    dependencies: cfitsio_dep,
  )
  test('testf77', cmp, args: [testf77, meson.current_source_dir()])
endif

# this benchmark uses POSIX sys/time.h which isn't available on msvc
if cc.get_id() != 'msvc'
  benchmark(
    'speed',
    executable('speed', 'utilities/speed.c', dependencies: cfitsio_dep),
  )
endif

