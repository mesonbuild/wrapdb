project(
  'imgui-sfml',
  'cpp',
  version: '2.6.1',
  license: 'MIT',
  meson_version: '>=0.49.0',
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

api = ['-DImGuiKey_=ImGuiKey', '-DImGuiNavInput_=ImGuiNavInput']
exp = []
if get_option('default_library') != 'static'
  api += '-DIMGUI_SFML_SHARED_LIB'
  exp += '-DIMGUI_SFML_EXPORTS'
endif

is_lib = library(
  'imgui-sfml',
  'imgui-SFML.cpp',
  cpp_args: [api, exp],
  dependencies: [sfml_dep, imgui_dep, opengl_dep],
)

depinc = include_directories('.')
imgui_sfml_dep = declare_dependency(
  include_directories: depinc,
  compile_args: api,
  dependencies: imgui_dep,
  link_with: is_lib,
)
