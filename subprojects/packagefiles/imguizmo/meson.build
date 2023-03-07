project(
  'ImGuizmo',
  'cpp',
  version: '1.83',
  meson_version: '>=0.49.0',
)

sources = files(
  'GraphEditor.cpp',
  'ImCurveEdit.cpp',
  'ImGuizmo.cpp',
  'ImSequencer.cpp',
)

imgui = dependency('imgui')

api = []
if host_machine.system() == 'windows' and get_option('default_library') != 'static'
  api += '-DIMGUI_API=__declspec(dllexport)'
endif

imguizmo_lib = library(
  'imguizmo',
  sources,
  dependencies: imgui,
)

api = []
if host_machine.system() == 'windows' and get_option('default_library') != 'static'
  api += '-DIMGUI_API=__declspec(dllimport)'
endif

imguizmo_inc = include_directories('.')
imguizmo_dep = declare_dependency(
  compile_args: api,
  include_directories: imguizmo_inc,
  link_with: imguizmo_lib, dependencies: imgui,
)
