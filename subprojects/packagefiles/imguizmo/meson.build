project(
  'ImGuizmo',
  'cpp',
  version: '1.83',
)

sources = files(
  'GraphEditor.cpp',
  'ImCurveEdit.cpp',
  'ImGuizmo.cpp',
  'ImSequencer.cpp',
)

imgui = dependency('imgui')

imguizmo_inc = include_directories('.')
imguizmo_lib = library(
  'imguizmo',
  sources,
  include_directories: imguizmo_inc,
  dependencies: imgui,
)
imguizmo_dep = declare_dependency(
  include_directories: imguizmo_inc,
  link_with: imguizmo_lib,
  dependencies: imgui,
)
