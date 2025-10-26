# Copyright © 2023 Erik Faye-Lund

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

project(
  'freeglut',
  'c',
  version: '3.6.0',
  license: 'MIT',
  meson_version: '>= 0.58.0',
)

cc = meson.get_compiler('c')
host_system = host_machine.system()
version = meson.project_version().split('.')

config = configuration_data()
config.set('VERSION_MAJOR', version[0])
config.set('VERSION_MINOR', version[1])
config.set('VERSION_PATCH', version[2])

freeglut_sources = files(
  'src/fg_callback_macros.h',
  'src/fg_callbacks.c',
  'src/fg_cursor.c',
  'src/fg_display.c',
  'src/fg_ext.c',
  'src/fg_font.c',
  'src/fg_font_data.c',
  'src/fg_gamemode.c',
  'src/fg_geometry.c',
  'src/fg_gl2.c',
  'src/fg_gl2.h',
  'src/fg_init.c',
  'src/fg_init.h',
  'src/fg_input_devices.c',
  'src/fg_internal.h',
  'src/fg_joystick.c',
  'src/fg_main.c',
  'src/fg_menu.c',
  'src/fg_misc.c',
  'src/fg_overlay.c',
  'src/fg_spaceball.c',
  'src/fg_state.c',
  'src/fg_stroke_mono_roman.c',
  'src/fg_stroke_roman.c',
  'src/fg_structure.c',
  'src/fg_teapot.c',
  'src/fg_teapot_data.h',
  'src/fg_videoresize.c',
  'src/fg_window.c',
)

freeglut_deps = [
  cc.find_library(
    'm',
    required: false,
  ),
  dependency('gl'),
]

if host_system == 'windows'
  if cc.get_id() == 'msvc'
    add_project_arguments(
      '/source-charset:windows-1252',
      language: 'c',
    )
  endif

  freeglut_sources += files(
    'src/mswin/fg_cmap_mswin.c',
    'src/mswin/fg_cursor_mswin.c',
    'src/mswin/fg_display_mswin.c',
    'src/mswin/fg_ext_mswin.c',
    'src/mswin/fg_gamemode_mswin.c',
    'src/mswin/fg_init_mswin.c',
    'src/mswin/fg_input_devices_mswin.c',
    'src/mswin/fg_internal_mswin.h',
    'src/mswin/fg_joystick_mswin.c',
    'src/mswin/fg_main_mswin.c',
    'src/mswin/fg_menu_mswin.c',
    'src/mswin/fg_spaceball_mswin.c',
    'src/mswin/fg_state_mswin.c',
    'src/mswin/fg_structure_mswin.c',
    'src/mswin/fg_window_mswin.c',
  )

  freeglut_rc = configure_file(
    input: 'freeglut.rc.in',
    output: 'freeglut.rc',
    encoding: 'cp1252',
    configuration: config,
  )
  freeglut_sources += import('windows').compile_resources(freeglut_rc)

  add_project_arguments(
    '-DFREEGLUT_EXPORTS',
    language: 'c',
  )
  add_project_arguments(
    '-D_WIN32_WINNT=0x0601',
    language: 'c',
  )

  freeglut_deps += cc.find_library('winmm')
  freeglut_deps += cc.find_library('gdi32')

else  # not windows

  if get_option('wayland')
    freeglut_sources += files(
      'src/egl/fg_display_egl.c',
      'src/egl/fg_ext_egl.c',
      'src/egl/fg_init_egl.c',
      'src/egl/fg_init_egl.h',
      'src/egl/fg_internal_egl.h',
      'src/egl/fg_state_egl.c',
      'src/egl/fg_state_egl.h',
      'src/egl/fg_structure_egl.c',
      'src/egl/fg_structure_egl.h',
      'src/egl/fg_window_egl.c',
      # font, serial port & joystick code are agnostic
      'src/egl/fg_window_egl.h',
      'src/wayland/fg_cursor_wl.c',
      'src/wayland/fg_ext_wl.c',
      'src/wayland/fg_gamemode_wl.c',
      'src/wayland/fg_init_wl.c',
      'src/wayland/fg_input_devices_wl.c',
      'src/wayland/fg_internal_wl.h',
      'src/wayland/fg_main_wl.c',
      'src/wayland/fg_state_wl.c',
      'src/wayland/fg_structure_wl.c',
      'src/wayland/fg_window_wl.c',
      'src/x11/fg_glutfont_definitions_x11.c',
      'src/x11/fg_input_devices_x11.c',
      'src/x11/fg_joystick_x11.c',
    )

    add_project_arguments(
      '-DFREEGLUT_WAYLAND',
      language: 'c',
    )
    freeglut_deps += dependency('wayland-client, wayland-cursor')
    freeglut_deps += dependency('wayland-egl, egl')
    freeglut_deps += dependency('xkbcommon')

  else
    freeglut_sources += files(
      'src/x11/fg_cmap_x11.c',
      'src/x11/fg_cursor_x11.c',
      'src/x11/fg_display_x11_glx.c',
      'src/x11/fg_ext_x11.c',
      'src/x11/fg_gamemode_x11.c',
      'src/x11/fg_glutfont_definitions_x11.c',
      'src/x11/fg_init_x11.c',
      'src/x11/fg_input_devices_x11.c',
      'src/x11/fg_internal_x11.h',
      'src/x11/fg_internal_x11_glx.h',
      'src/x11/fg_joystick_x11.c',
      'src/x11/fg_main_x11.c',
      'src/x11/fg_menu_x11.c',
      'src/x11/fg_spaceball_x11.c',
      'src/x11/fg_state_x11.c',
      'src/x11/fg_state_x11_glx.c',
      'src/x11/fg_state_x11_glx.h',
      'src/x11/fg_structure_x11.c',
      'src/x11/fg_window_x11.c',
      'src/x11/fg_window_x11_glx.c',
      'src/x11/fg_window_x11_glx.h',
      'src/x11/fg_xinput_x11.c',
    )

    if host_machine.system() == 'linux'
      freeglut_deps += dependency('glu')
    endif
    x11_dep = dependency('x11')
    freeglut_deps += x11_dep
    freeglut_deps += dependency('xext')
    freeglut_deps += dependency('xi')
    freeglut_deps += dependency('xkbcommon')

    foreach d, s : {
      'xrandr': 'XRANDR',
      'xxf86vm': 'XF86VMODE',
      'xi': 'XINPUT2',
    }
      _dep = dependency(
        d,
        required: false,
      )
      if _dep.found()
        freeglut_deps += _dep
        add_project_arguments(
          '-DHAVE_X11_EXTENSIONS_@0@_H'.format(s),
          language: 'c',
        )
      endif
    endforeach

  endif

  add_project_arguments(
    '-D_GNU_SOURCE',
    language: 'c',
  )
endif

foreach h : [
  'sys/types.h',
  'unistd.h',
  'sys/time.h',
  'stdbool.h',
  'sys/param.h',
  'sys/ioctl.h',
  'fcntl.h',
  'stdint.h',
  'inttypes.h',
]
  if cc.has_header(h)
    h = h.replace('/', '_')
    h = h.replace('.', '_')
    add_project_arguments(
      '-DHAVE_@0@'.format(h.to_upper()),
      language: 'c',
    )
  endif
endforeach

if cc.has_function('gettimeofday')
  add_project_arguments(
    '-DHAVE_GETTIMEOFDAY',
    language: 'c',
  )
endif

if cc.has_function(
  'XParseGeometry',
  dependencies: freeglut_deps,
  prefix: '#include <X11/Xlib.h>',
)
  add_project_arguments(
    '-DHAVE_XPARSEGEOMETRY',
    language: 'c',
  )
else
  freeglut_sources += files(
    'src/util/xparsegeometry_repl.c',
    'src/util/xparsegeometry_repl.h',
  )
  add_project_arguments(
    '-DNEED_XPARSEGEOMETRY_IMPL',
    language: 'c',
  )
endif

freeglut_def = configure_file(
  input: 'src/freeglutdll.def.in',
  output: 'freeglutdll.def',
  configuration: config,
)

compile_args = ['-DFREEGLUT_LIB_PRAGMAS=0']
if get_option('default_library') == 'static'
  compile_args += '-DFREEGLUT_STATIC'
  add_project_arguments(
    '-DFREEGLUT_STATIC',
    language: 'c',
  )
endif

freeglut_includes = include_directories('include')

libfreeglut = library(
  'freeglut',
  freeglut_sources,
  include_directories: [freeglut_includes, include_directories('src')],
  dependencies: freeglut_deps,
  override_options: 'c_std=c11',
  soversion: host_system == 'windows' ? '' : version[0],
  version: meson.project_version(),
  vs_module_defs: freeglut_def,
  install: true,
)

install_headers(
  'include/GL/freeglut_ext.h',
  'include/GL/freeglut_std.h',
  'include/GL/freeglut_ucall.h',
  'include/GL/freeglut.h',
  'include/GL/glut.h',
  subdir: 'GL',
)

freeglut_dep = declare_dependency(
  compile_args: compile_args,
  link_with: libfreeglut,
  include_directories: freeglut_includes,
)

meson.override_dependency('glut', freeglut_dep)
meson.override_dependency('freeglut', freeglut_dep)
