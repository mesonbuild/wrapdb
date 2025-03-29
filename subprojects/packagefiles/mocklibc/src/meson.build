sources = files('grp.c', 'netdb.c', 'netgroup.c', 'pwd.c')

libmocklibc = shared_library(
  meson.project_name(),
  version: libversion,
  sources: sources,
)

# The library itself must be placed before the real system libc
# (something that is done by setting the LD_PRELOAD environment variable
# or just using the executable mocklibc provided by the package).
libmocklibc_dep = declare_dependency(
  link_with: libmocklibc,
)

executable(
  meson.project_name() + '-debug-netgroup',
  sources: 'netgroup-debug.c',
  link_with: libmocklibc,
)
