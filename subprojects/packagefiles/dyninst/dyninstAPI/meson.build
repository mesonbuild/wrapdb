if get_option('lightweight_symtab')
  message('-Dlightweight_symtab=true; dyninstAPI not built')
  subdir_done()
endif

srcs = files(
  'src/BPatch.C',
  'src/BPatch_addressSpace.C',
  'src/BPatch_basicBlock.C',
  'src/BPatch_basicBlockLoop.C',
  'src/BPatch_binaryEdit.C',
  'src/BPatch_collections.C',
  'src/BPatch_edge.C',
  'src/BPatch_flowGraph.C',
  'src/BPatch_frame.C',
  'src/BPatch_function.C',
  'src/BPatch_image.C',
  'src/BPatch_instruction.C',
  'src/BPatch_loopTreeNode.C',
  'src/BPatch_memoryAccess.C',
  'src/BPatch_memoryAccessAdapter.C',
  'src/BPatch_module.C',
  'src/BPatch_object.C',
  'src/BPatch_parRegion.C',
  'src/BPatch_point.C',
  'src/BPatch_process.C',
  'src/BPatch_snippet.C',
  'src/BPatch_sourceBlock.C',
  'src/BPatch_statement.C',
  'src/BPatch_thread.C',
  'src/BPatch_type.C',
  'src/Parsing-arch.C',
  'src/Parsing.C',
  'src/Patching.C',
  'src/Relocation/CFG/RelocBlock.C',
  'src/Relocation/CFG/RelocEdge.C',
  'src/Relocation/CFG/RelocGraph.C',
  'src/Relocation/CFG/RelocTarget.C',
  'src/Relocation/CodeBuffer.C',
  'src/Relocation/CodeMover.C',
  'src/Relocation/CodeTracker.C',
  'src/Relocation/DynAddrSpace.C',
  'src/Relocation/DynCFGMaker.C',
  'src/Relocation/DynInstrumenter.C',
  'src/Relocation/DynObject.C',
  'src/Relocation/DynPointMaker.C',
  'src/Relocation/Springboard.C',
  'src/Relocation/Transformers/Instrumenter.C',
  'src/Relocation/Transformers/Modification.C',
  'src/Relocation/Transformers/Movement-adhoc.C',
  'src/Relocation/Transformers/Movement-analysis.C',
  'src/Relocation/Transformers/Transformer.C',
  'src/Relocation/Widgets/ASTWidget.C',
  'src/Relocation/Widgets/CFWidget.C',
  'src/Relocation/Widgets/CallbackWidget.C',
  'src/Relocation/Widgets/InsnWidget.C',
  'src/Relocation/Widgets/InstWidget.C',
  'src/Relocation/Widgets/PCWidget.C',
  'src/Relocation/Widgets/RelDataWidget.C',
  'src/Relocation/Widgets/StackModWidget.C',
  'src/Relocation/patchapi_debug.C',
  'src/addressSpace.C',
  'src/ast.C',
  'src/baseTramp.C',
  'src/binaryEdit.C',
  'src/block.C',
  'src/codeRange.C',
  'src/codegen.C',
  'src/debug.C',
  'src/dynProcess.C',
  'src/dynThread.C',
  'src/edge.C',
  'src/frame.C',
  'src/frameChecker.C',
  'src/function.C',
  'src/hybridCallbacks.C',
  'src/hybridInstrumentation.C',
  'src/hybridOverwrites.C',
  'src/image.C',
  'src/infHeap.C',
  'src/inst.C',
  'src/instPoint.C',
  'src/mapped_module.C',
  'src/mapped_object.C',
  'src/parRegion.C',
  'src/parse-cfg.C',
  'src/pcEventHandler.C',
  'src/pcEventMuxer.C',
  'src/registerSpace.C',
  'src/util.C',
  'src/variable.C',
)

if cap_stack_mods
  srcs += files(
    'src/StackMod/OffsetVector.C',
    'src/StackMod/StackAccess.C',
    'src/StackMod/StackLocation.C',
    'src/StackMod/StackMod.C',
    'src/StackMod/StackModChecker.C',
    'src/StackMod/StackModExpr.C',
    'src/StackMod/TMap.C',
  )
endif

if host_machine.cpu_family() in ['x86', 'x86_64']
  srcs += files(
    'src/IAPI_to_AST.C',
    'src/RegisterConversion-x86.C',
    'src/Relocation/Widgets/CFWidget-x86.C',
    'src/Relocation/Widgets/PCWidget-x86.C',
    'src/codegen-x86.C',
    'src/dynProcess-x86.C',
    'src/emit-x86.C',
    'src/inst-x86.C',
    'src/parse-x86.C',
    'src/stackwalk-x86.C',
  )
elif host_machine.cpu_family() == 'ppc64'
  srcs += files(
    'src/RegisterConversion-ppc.C',
    'src/Relocation/Widgets/CFWidget-ppc.C',
    'src/Relocation/Widgets/PCWidget-ppc.C',
    'src/codegen-power.C',
    'src/inst-power.C',
    'src/parse-power.C',
    'src/stackwalk-ppc.C',
  )
elif host_machine.cpu_family() == 'aarch64'
  srcs += files(
    'src/RegisterConversion-aarch64.C',
    'src/Relocation/Widgets/CFWidget-aarch64.C',
    'src/Relocation/Widgets/PCWidget-aarch64.C',
    'src/codegen-aarch64.C',
    'src/emit-aarch64.C',
    'src/inst-aarch64.C',
    'src/parse-aarch64.C',
    'src/stackwalk-aarch64.C',
  )
endif

if host_machine.system() == 'freebsd'
  srcs += files(
    'src/freebsd-x86.C',
    'src/freebsd.C',
    'src/syscall-freebsd.C',
    'src/syscallNotification.C',
    'src/unix.C',
  )
elif host_machine.system() == 'linux'
  srcs += files(
    'src/inst-linux.C',
    'src/linux.C',
    'src/syscall-linux.C',
    'src/syscallNotification.C',
    'src/unix.C',
  )
  if host_machine.cpu_family() in ['x86', 'x86_64']
    srcs += files('src/linux-x86.C')
  elif host_machine.cpu_family() == 'ppc64'
    srcs += files('src/linux-power.C')
  elif host_machine.cpu_family() == 'aarch64'
    srcs += files('src/linux-aarch64.C')
  endif
elif host_machine.system() == 'windows'
  srcs += files(
    'src/Relocation/DynAddrSpace.C',
    'src/Relocation/DynCFGMaker.C',
    'src/Relocation/DynInstrumenter.C',
    'src/Relocation/DynObject.C',
    'src/Relocation/DynPointMaker.C',
    'src/hybridCallbacks.C',
    'src/hybridInstrumentation.C',
    'src/hybridOverwrites.C',
    'src/inst-winnt.C',
    'src/pdwinnt.C',
    'src/syscall-nt.C',
  )
endif

args = ['-DBPATCH_DLL_BUILD']

if host_machine.cpu_family() == 'x86' and host_machine.system() == 'linux'
  srcs += files('src/cpuid-x86.S')
endif

cpp = meson.get_compiler('cpp')
if cpp.get_argument_syntax() == 'gcc'
  search_dirs = run_command(
    cpp,
    '-print-search-dirs',
    check: false,
    capture: true,
  )
  if search_dirs.returncode() == 0
    foreach line : search_dirs.stdout().split('\n')
      if line.startswith('libraries:')
        line = line.substring(10)
        if line.startswith(' ')
          line = line.substring(1)
        endif
        if line.startswith('=')
          line = line.substring(1)
        endif
        args += ['-DDYNINST_COMPILER_SEARCH_DIRS=@0@'.format(line)]
        break
      endif
    endforeach
  endif
endif

install_headers(
  'h/BPatch_addressSpace.h',
  'h/BPatch_basicBlock.h',
  'h/BPatch_basicBlockLoop.h',
  'h/BPatch_binaryEdit.h',
  'h/BPatch_callbacks.h',
  'h/BPatch_dll.h',
  'h/BPatch_edge.h',
  'h/BPatch_enums.h',
  'h/BPatch_flowGraph.h',
  'h/BPatch_frame.h',
  'h/BPatch_function.h',
  'h/BPatch.h',
  'h/BPatch_image.h',
  'h/BPatch_instruction.h',
  'h/BPatch_loopTreeNode.h',
  'h/BPatch_memoryAccess_NP.h',
  'h/BPatch_module.h',
  'h/BPatch_object.h',
  'h/BPatch_parRegion.h',
  'h/BPatch_point.h',
  'h/BPatch_process.h',
  'h/BPatch_Set.h',
  'h/BPatch_snippet.h',
  'h/BPatch_sourceBlock.h',
  'h/BPatch_sourceObj.h',
  'h/BPatch_statement.h',
  'h/BPatch_thread.h',
  'h/BPatch_type.h',
  'h/BPatch_Vector.h',
  'h/StackMod.h',
)

iface_deps = [
  common_dep,
  instructionapi_dep,
  stackwalk_dep,
  pcontrol_dep,
  patchapi_dep,
  parseapi_dep,
  symtabapi_dep,
  boost_dep,
]
dyninstAPI_lib = library(
  'dyninstAPI',
  srcs,
  gnu_symbol_visibility: 'inlineshidden',
  override_options: ['b_ndebug=false'],
  include_directories: include_directories(
    '..',
    'src',
    'h',
    # Comes through hacky CMake target trickery
    '../common/src',
    '../instructionAPI/src',
    '../stackwalk/src',
    '../proccontrol/src',
    '../patchAPI/src',
    '../parseAPI/src',
    '../symtabAPI/src',
  ),
  c_args: args,
  cpp_args: args,
  dependencies: [iface_deps, libelf_dep, libdw_dep, threads_dep],
  version: meson.project_version(),
  soversion: dyninst_soversion,
  install: true,
)
dyninstapi_dep = declare_dependency(
  link_with: dyninstAPI_lib,
  include_directories: include_directories('h'),
  dependencies: iface_deps,
)
all_deps += dyninstapi_dep
