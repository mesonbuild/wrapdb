project(
  'imgui-sfml',
  'cpp',
  version: '3.0',
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

# workaround issue (#14939) in Meson 1.8.4 - 1.9.0, where
# default_options:['cpp_std=c++17'] doesn't work under certain circumstances
override_opts = ['cpp_std=c++17']

is_lib = library(
  'imgui-sfml',
  'imgui-SFML.cpp',
  cpp_args: [api, exp],
  dependencies: [sfml_dep, imgui_dep, opengl_dep],
  override_options: override_opts,
)

depinc = include_directories('.')
imgui_sfml_dep = declare_dependency(
  include_directories: depinc,
  compile_args: api,
  dependencies: imgui_dep,
  link_with: is_lib,
)
