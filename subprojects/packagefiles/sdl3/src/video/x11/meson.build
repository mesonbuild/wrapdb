cdata.set10('SDL_VIDEO_DRIVER_X11', true)

sources += files(
  'edid-parse.c',
  'SDL_x11clipboard.c',
  'SDL_x11dyn.c',
  'SDL_x11events.c',
  'SDL_x11framebuffer.c',
  'SDL_x11keyboard.c',
  'SDL_x11messagebox.c',
  'SDL_x11modes.c',
  'SDL_x11mouse.c',
  'SDL_x11opengl.c',
  'SDL_x11opengles.c',
  'SDL_x11pen.c',
  'SDL_x11settings.c',
  'SDL_x11shape.c',
  'SDL_x11toolkit.c',
  'SDL_x11touch.c',
  'SDL_x11video.c',
  'SDL_x11vulkan.c',
  'SDL_x11window.c',
  'SDL_x11xfixes.c',
  'SDL_x11xinput2.c',
  'SDL_x11xsync.c',
  'SDL_x11xtest.c',
  'xsettings-client.c',
)


xi_dep = dependency(
  'xi',
  required: get_option('use_video_x11_xinput'),
)
xfixes_dep = dependency(
  'xfixes',
  required: get_option('use_video_x11_xfixes').require(xi_dep.found()),  # SDL3 uses Xfixes with XIBarrierReleasePointer
)
xcursor_dep = dependency(
  'xcursor',
  required: get_option('use_video_x11_xcursor'),
)
xrandr_dep = dependency(
  'xrandr',
  required: get_option('use_video_x11_xrandr'),
)
xscrnsaver_dep = dependency(
  'xscrnsaver',
  required: get_option('use_video_x11_xscrnsaver'),
)
xtst_dep = dependency(
  'xtst',
  required: get_option('use_video_x11_xtest'),
)

cdata.set10('SDL_VIDEO_DRIVER_X11_XINPUT2', xi_dep.found())
sdl_deps += xi_dep
cdata.set10('SDL_VIDEO_DRIVER_X11_XFIXES', xfixes_dep.found())
sdl_deps += xfixes_dep
cdata.set10('SDL_VIDEO_DRIVER_X11_XCURSOR', xcursor_dep.found())
sdl_deps += xcursor_dep
cdata.set10('SDL_VIDEO_DRIVER_X11_XRANDR', xrandr_dep.found())
sdl_deps += xrandr_dep
cdata.set10('SDL_VIDEO_DRIVER_X11_XSCRNSAVER', xscrnsaver_dep.found())
sdl_deps += xscrnsaver_dep
cdata.set10('SDL_VIDEO_DRIVER_X11_XTEST', xtst_dep.found())
sdl_deps += xtst_dep



have_XSYNC_header = cc.has_header(
  'X11/extensions/sync.h',
  required: get_option('use_video_x11_xsync'),
)
have_XSHAPE_header = cc.has_header(
  'X11/extensions/shape.h',
  required: get_option('use_video_x11_xshape'),
)
have_XDBE_header = cc.has_header(
  'X11/extensions/Xdbe.h',
  required: get_option('use_video_x11_xdbe'),
)
have_XEXT_header = cc.has_header('X11/extensions/Xext.h')

cdata.set10('SDL_VIDEO_DRIVER_X11_XSYNC', have_XSYNC_header)
cdata.set10('SDL_VIDEO_DRIVER_X11_XSHAPE', have_XSHAPE_header)
cdata.set10('SDL_VIDEO_DRIVER_X11_XDBE', have_XDBE_header)
cdata.set10('SDL_VIDEO_DRIVER_X11_HAS_XKBLIB', cc.has_header('X11/XKBlib.h'))

have_shmat_in_libc_code = '''
  #include <sys/shm.h>
  int main(int argc, char **argv) { shmat;}
'''
have_shmat_in_libc = cc.compiles(
  have_shmat_in_libc_code,
  name: 'have shmat in libc',
)

if not have_shmat_in_libc
  cdata.set('NO_SHARED_MEMORY', 1)
endif

have_X11_genericevent_code = '''
  #include <X11/Xlib.h>
  int main(int argc, char **argv) {
  Display *display;
  XEvent event;
  XGenericEventCookie *cookie = &event.xcookie;
  XNextEvent(display, &event);
  XGetEventData(display, cookie);
  XFreeEventData(display, cookie);
  return 0; }
'''
have_X11_genericevent = cc.compiles(
  have_X11_genericevent_code,
  name: 'have OpenGL genericevent support',
)

if have_X11_genericevent
  cdata.set('SDL_VIDEO_DRIVER_X11_SUPPORTS_GENERIC_EVENTS', 1)
endif


# X11/XKBlib is not used within CMake script

if xi_dep.found()
  # X11 scroll info
  have_XInput2_ScrollInfo_code = '''
    #include <X11/Xlib.h>
    #include <X11/Xproto.h>
    #include <X11/extensions/XInput2.h>
    XIScrollClassInfo *s;
    int main(int argc, char **argv) {}
  '''
  have_XInput2_ScrollInfo = cc.compiles(
    have_XInput2_ScrollInfo_code,
    name: 'have XInput2 scrollinfo',
  )

  if have_XInput2_ScrollInfo
    cdata.set('SDL_VIDEO_DRIVER_X11_XINPUT2_SUPPORTS_SCROLLINFO', 1)
  endif


  # X11 multitouch

  have_XInput2_multitouch_code = '''
    #include <X11/Xlib.h>
    #include <X11/Xproto.h>
    #include <X11/extensions/XInput2.h>
    int event_type = XI_TouchBegin;
    XITouchClassInfo *t;
    Status XIAllowTouchEvents(Display *a,int b,unsigned int c,Window d,int f) {
      return (Status)0;
    }
    int main(int argc, char **argv) { return 0; }
  '''
  have_XInput2_multitouch = cc.compiles(
    have_XInput2_multitouch_code,
    name: 'have XInput2 multi-touch',
  )

  if have_XInput2_multitouch
    cdata.set('SDL_VIDEO_DRIVER_X11_XINPUT2_SUPPORTS_MULTITOUCH', 1)
  endif


  # X11 touch gestures

  have_XInput2_gesture_code = '''
    #include <X11/Xlib.h>
    #include <X11/Xproto.h>
    #include <X11/extensions/XInput2.h>
    int event_type = XI_GesturePinchBegin;
    XITouchClassInfo *t;
    Status XIAllowTouchEvents(Display *a,int b,unsigned int c,Window d,int f) {
      return (Status)0;
    }
    int main(int argc, char **argv) { return 0; }
  '''
  have_XInput2_gesture = cc.compiles(
    have_XInput2_gesture_code,
    name: 'have XInput2 touch gesture',
  )

  if have_XInput2_gesture
    cdata.set('SDL_VIDEO_DRIVER_X11_XINPUT2_SUPPORTS_GESTURE', 1)
  endif
endif
