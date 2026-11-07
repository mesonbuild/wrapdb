dep_uring = dependency(
  'liburing-ffi',
  required: opt_liburing,
)
have_liburing = dep_uring.found() and cc.has_header(
  'liburing.h',
  dependencies: dep_uring,
)
cdata.set10('HAVE_LIBURING_H', have_liburing)
if have_liburing
  sdl_deps += dep_uring
  subdir('io_uring')
elif platform_is_windows
  subdir('windows')
endif

subdir('generic')

sources += files('SDL_asyncio.c', 'SDL_iostream.c')
