srcs = files(
  'src/AddrSpace.C',
  'src/CFGMaker.C',
  'src/Command.C',
  'src/Instrumenter.C',
  'src/ParseCallback.C',
  'src/PatchBlock.C',
  'src/PatchCallback.C',
  'src/PatchEdge.C',
  'src/PatchFunction.C',
  'src/PatchLoop.C',
  'src/PatchLoopTreeNode.C',
  'src/PatchMgr.C',
  'src/PatchModifier.C',
  'src/PatchObject.C',
  'src/Point.C',
  'src/PointMaker.C',
)

args = ['-DPATCHAPI_LIB']

install_headers(
  'h/AddrSpace.h',
  'h/CFGMaker.h',
  'h/Command.h',
  'h/Instrumenter.h',
  'h/PatchCallback.h',
  'h/PatchCFG.h',
  'h/PatchCommon.h',
  'h/PatchMgr.h',
  'h/PatchModifier.h',
  'h/PatchObject.h',
  'h/Point.h',
  'h/Snippet.h',
)

iface_deps = [common_dep, instructionapi_dep, parseapi_dep]
patchAPI_lib = library(
  'patchAPI',
  srcs,
  gnu_symbol_visibility: 'inlineshidden',
  override_options: ['b_ndebug=false'],
  include_directories: include_directories(
    '../common/h',  # This order is needed because there are multiple util.h
    '..',
    'src',
    'h',
    # Comes through hacky CMake target trickery
    '../common/src',
    '../instructionAPI/src',
    '../parseAPI/src',
  ),
  c_args: args,
  cpp_args: args,
  dependencies: [iface_deps, boost_dep],
  version: meson.project_version(),
  soversion: dyninst_soversion,
  install: true,
)
patchapi_dep = declare_dependency(
  link_with: patchAPI_lib,
  include_directories: include_directories('h'),
  dependencies: iface_deps,
)
all_deps += patchapi_dep
