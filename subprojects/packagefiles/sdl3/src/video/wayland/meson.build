sources += files(
  'SDL_waylandclipboard.c',
  'SDL_waylandcolor.c',
  'SDL_waylanddatamanager.c',
  'SDL_waylanddyn.c',
  'SDL_waylandevents.c',
  'SDL_waylandkeyboard.c',
  'SDL_waylandmessagebox.c',
  'SDL_waylandmouse.c',
  'SDL_waylandopengles.c',
  'SDL_waylandshmbuffer.c',
  'SDL_waylandutil.c',
  'SDL_waylandvideo.c',
  'SDL_waylandvulkan.c',
  'SDL_waylandwindow.c',
)

if opt_video_wayland_libdecor.allowed()
  libdecor_dep = dependency(
    'libdecor-0',
    required: opt_video_wayland_libdecor,
  )
  have_libdecor = libdecor_dep.found() and cc.has_header(
    'libdecor.h',
    dependencies: libdecor_dep,
  )
  cdata.set10('HAVE_LIBDECOR_H', have_libdecor)

  if have_libdecor
    sdl_deps += libdecor_dep

    # Libdecor doesn't provide internal version defines, so generate them here.
    libdecor_version = libdecor_dep.version().split('.')
    libdecor_major = libdecor_version[0].to_int()
    libdecor_minor = libdecor_version[1].to_int()
    libdecor_patch = libdecor_version[2].to_int()

    cdata.set('SDL_LIBDECOR_VERSION_MAJOR', libdecor_major)
    cdata.set('SDL_LIBDECOR_VERSION_MINOR', libdecor_minor)
    cdata.set('SDL_LIBDECOR_VERSION_PATCH', libdecor_patch)
  endif
endif

# parse XKB version to avoid issues within SDL3 config
xkdbcommon_version = xkbcommon_dep.version().split('.')

xkdbcommon_major = xkdbcommon_version[0].to_int()
xkdbcommon_minor = xkdbcommon_version[1].to_int()
xkdbcommon_patch = xkdbcommon_version[2].to_int()

cdata.set('SDL_XKBCOMMON_VERSION_MAJOR', xkdbcommon_major)
cdata.set('SDL_XKBCOMMON_VERSION_MINOR', xkdbcommon_minor)
cdata.set('SDL_XKBCOMMON_VERSION_PATCH', xkdbcommon_patch)
