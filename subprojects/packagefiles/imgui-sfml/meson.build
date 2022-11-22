project(
  'imgui-sfml',
  'cpp',
  version: '2.5',
  license: 'MIT',
  meson_version: '>=0.50.0',
)

imgui_dep = dependency('imgui')
sfml_dep = dependency('sfml')
opengl_dep = dependency('gl')

# We do not look up sfml here because there are many different
# names for the .pc files and others and it is unclear which
# ones we should use. Thus users of this wrap must look up sfml
# by themselves and add it to their targets.
#
# This is suboptimal, hopefully this can be fixed once we have
# more usage experience.

api = []
if get_option('default_library') != 'static'
  api += '-DIMGUI_SFML_SHARED_LIB'
endif

is_lib = library(
  'imgui-sfml',
  'imgui-SFML.cpp',
  cpp_args: api,
  dependencies: [sfml_dep, imgui_dep, opengl_dep],
)

imgui_sfml_dep = declare_dependency(
  include_directories: '.',
  compile_args: api,
  dependencies: imgui_dep, link_with: is_lib,
)
