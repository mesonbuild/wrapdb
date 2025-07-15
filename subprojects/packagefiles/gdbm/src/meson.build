conf = configuration_data()
conf.set('GDBM_DEBUG_ENABLE', get_option('gdbm_debug') ? 1 : 0)
count_t = 'unsigned long'
if cc.has_type('unsigned long long int')
  count_t = 'unsigned long long int'
endif
conf.set('GDBM_COUNT_T', count_t)
version = meson.project_version().split('.')
conf.set('GDBM_VERSION_MAJOR', version[0])
conf.set('GDBM_VERSION_MINOR', version[1])
conf.set('GDBM_VERSION_PATCH', 0)
configure_file(
  input: 'gdbm.h.in',
  output: 'gdbm.h',
  configuration: conf,
)

src = files(
  'avail.c',
  'base64.c',
  'bucket.c',
  'falloc.c',
  'findkey.c',
  'fullio.c',
  'gdbmclose.c',
  'gdbmcount.c',
  'gdbmdelete.c',
  'gdbmdump.c',
  'gdbmerrno.c',
  'gdbmexists.c',
  'gdbmexp.c',
  'gdbmfdesc.c',
  'gdbmfetch.c',
  'gdbmimp.c',
  'gdbmload.c',
  'gdbmopen.c',
  'gdbmreorg.c',
  'gdbmseq.c',
  'gdbmsetopt.c',
  'gdbmstore.c',
  'gdbmsync.c',
  'hash.c',
  'lock.c',
  'mmap.c',
  'recover.c',
  'update.c',
  'version.c',
)

if get_option('gdbm_debug')
  src += files('debug.c')
endif

libgdbm = library(
  'gdbm',
  src,
  include_directories: autoconf_include,
  dependencies: deps,
)

depinc = include_directories('.')
gdbm = declare_dependency(
  link_with: libgdbm,
  include_directories: depinc,
)
