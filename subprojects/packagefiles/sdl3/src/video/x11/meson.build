
sources += files(
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
  'SDL_x11touch.c',
  'SDL_x11video.c',
  'SDL_x11vulkan.c',
  'SDL_x11window.c',
  'SDL_x11xfixes.c',
  'SDL_x11xinput2.c',
  'SDL_x11xsync.c',
  'edid-parse.c',
  'xsettings-client.c',
)

have_shmat_in_libc_code = '''
  #include <sys/shm.h>
  int main(int argc, char **argv) { shmat;}
'''
have_shmat_in_libc = cc.compiles(
  have_shmat_in_libc_code,
  name: 'have shmat in libc',
)

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

if not have_shmat_in_libc
  cdata.set('NO_SHARED_MEMORY', 1)
endif

if have_X11_genericevent
  cdata.set('SDL_VIDEO_DRIVER_X11_SUPPORTS_GENERIC_EVENTS', 1)
endif


