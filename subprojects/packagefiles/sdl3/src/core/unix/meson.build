fribidi_dep = dependency(
  'fribidi',
  required: opt_fribidi,
)
have_fribidi = fribidi_dep.found() and cc.has_header(
  'fribidi.h',
  dependencies: fribidi_dep,
)
cdata.set10('HAVE_FRIBIDI_H', have_fribidi)
if have_fribidi
  sdl_deps += fribidi_dep
  dlopen_table += {
    'option': opt_fribidi_shared,
    'dep_var': 'fribidi_dep',
    'lib': 'fribidi',
    'conf_var': 'SDL_FRIBIDI_DYNAMIC',
  }
endif

libthai_dep = dependency(
  'libthai',
  required: opt_libthai,
)
have_libthai = libthai_dep.found() and cc.has_header(
  'libthai.h',
  dependencies: libthai_dep,
)
cdata.set10('HAVE_LIBTHAI_H', have_libthai)
if have_libthai
  sdl_deps += libthai_dep
  dlopen_table += {
    'option': opt_libthai_shared,
    'dep_var': 'libthai_dep',
    'lib': 'thai',
    'conf_var': 'SDL_LIBTHAI_DYNAMIC',
  }
endif

sources += files(
  'SDL_appid.c',
  'SDL_fribidi.c',
  'SDL_gtk.c',
  'SDL_libthai.c',
  'SDL_poll.c',
)

have_unix_usergroupids_code = '''
    // required for GNU\Linux feature_test_macros(7)
    #define _GNU_SOURCE
    #include <unistd.h>
    int main(int argc, char** argv) { 
	  getresgid; 
	  getresuid; 
	}
'''
have_unix_usergroupids = cc.compiles(
  have_unix_usergroupids_code,
  name: 'have unix effective User/Group functions support',
)

if have_unix_usergroupids
  cdata.set('HAVE_GETRESGID', 1)
  cdata.set('HAVE_GETRESUID', 1)
endif


