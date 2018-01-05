conf = configuration_data()
conf.set('GDBM_DEBUG_ENABLE', get_option('debug') ? 1 : 0)
count_t = 'unsigned long'
if cc.has_type('unsigned long long int')
    count_t = 'unsigned long long int'
endif
conf.set('GDBM_COUNT_T', count_t)
version = meson.project_version().split('.')
conf.set('GDBM_VERSION_MAJOR', version[0])
conf.set('GDBM_VERSION_MINOR', version[1])
conf.set('GDBM_VERSION_PATCH', version[2])
configure_file(output: 'gdbm.h', input: 'gdbm.h.in', configuration: conf)

inc = autoconf_include

src = [
    'gdbmclose.c',
    'gdbmcount.c',
    'gdbmdelete.c',
    'gdbmdump.c',
    'gdbmerrno.c',
    'gdbmexists.c',
    'gdbmexp.c',
    'gdbmfdesc.c',
    'gdbmfetch.c',
    'gdbmload.c',
    'gdbmopen.c',
    'gdbmimp.c',
    'gdbmreorg.c',
    'gdbmseq.c',
    'gdbmsetopt.c',
    'gdbmstore.c',
    'gdbmsync.c',
    'base64.c',
    'bucket.c',
    'falloc.c',
    'findkey.c',
    'fullio.c',
    'hash.c',
    'lock.c',
    'mmap.c',
    'recover.c',
    'update.c',
    'version.c',
]
if get_option('debug')
    src += 'debug.c'
endif
libgdbm = library('gdbm', src, include_directories: autoconf_include)
gdbm = declare_dependency(
    link_with: libgdbm,
    include_directories: include_directories('.'))
