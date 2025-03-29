srcs = files(
  'src/Block.C',
  'src/BoundFactCalculator.C',
  'src/BoundFactData.C',
  'src/CFGFactory.C',
  'src/CFGModifier.C',
  'src/CodeObject.C',
  'src/CodeSource.C',
  'src/Function.C',
  'src/IA_IAPI.C',
  'src/IA_aarch64.C',
  'src/IA_amdgpu.C',
  'src/IA_power.C',
  'src/IA_x86.C',
  'src/IdiomModelDesc.C',
  'src/IndirectASTVisitor.C',
  'src/IndirectAnalyzer.C',
  'src/InstructionAdapter.C',
  'src/JumpTableFormatPred.C',
  'src/JumpTableIndexPred.C',
  'src/Loop.C',
  'src/LoopAnalyzer.C',
  'src/LoopTreeNode.C',
  'src/ParseCallback.C',
  'src/ParseData.C',
  'src/Parser-speculative.C',
  'src/Parser.C',
  'src/ParserDetails.C',
  'src/ProbabilisticParser.C',
  'src/StackTamperVisitor.C',
  'src/SymbolicExpression.C',
  'src/ThunkData.C',
  'src/debug_parse.C',
  'src/dominator.C',
)

srcs += files(
  '../dataflowAPI/rose/ExtentMap.C',
  '../dataflowAPI/rose/rangemap.C',
  '../dataflowAPI/rose/semantics/BaseSemantics2.C',
  '../dataflowAPI/rose/semantics/BinarySymbolicExpr.C',
  '../dataflowAPI/rose/semantics/DispatcherAMDGPU.C',
  '../dataflowAPI/rose/semantics/DispatcherARM64.C',
  '../dataflowAPI/rose/semantics/DispatcherPowerpc.C',
  '../dataflowAPI/rose/semantics/RegisterParts.C',
  '../dataflowAPI/rose/semantics/RegisterStateGeneric.C',
  '../dataflowAPI/rose/semantics/Registers.C',
  '../dataflowAPI/rose/semantics/SymEvalSemantics.C',
  '../dataflowAPI/rose/util/Assert.C',
  '../dataflowAPI/rose/util/Attribute.C',
  '../dataflowAPI/rose/util/Combinatorics.C',
  '../dataflowAPI/rose/util/LinearCongruentialGenerator.C',
  '../dataflowAPI/rose/util/Message.C',
  '../dataflowAPI/rose/util/Sawyer.C',
  '../dataflowAPI/rose/util/SmallObject.C',
  '../dataflowAPI/rose/util/Stopwatch.C',
  '../dataflowAPI/rose/util/StringUtility.C',
  '../dataflowAPI/rose/util/Synchronization.C',
  '../dataflowAPI/rose/util/rose_getline.C',
  '../dataflowAPI/src/ABI.C',
  '../dataflowAPI/src/Absloc.C',
  '../dataflowAPI/src/AbslocInterface.C',
  '../dataflowAPI/src/ExpressionConversionVisitor.C',
  '../dataflowAPI/src/InstructionCache.C',
  '../dataflowAPI/src/RegisterMap.C',
  '../dataflowAPI/src/RoseImpl.C',
  '../dataflowAPI/src/RoseInsnFactory.C',
  '../dataflowAPI/src/SymEval.C',
  '../dataflowAPI/src/SymEvalPolicy.C',
  '../dataflowAPI/src/SymbolicExpansion.C',
  '../dataflowAPI/src/Visitors.C',
  '../dataflowAPI/src/convertOpcodes.C',
  '../dataflowAPI/src/debug_dataflow.C',
  '../dataflowAPI/src/liveness.C',
  '../dataflowAPI/src/slicing.C',
  '../dataflowAPI/src/stackanalysis.C',
)

if get_option('lightweight_symtab')
  srcs += files('src/SymLiteCodeSource.C')
  symreader = symlite_dep
else
  srcs += files('src/SymtabCodeSource.C')
  symreader = symtabapi_dep
endif

if false
  srcs += files('src/GraphAdapter.C')
endif

args = ['-DPARSER_LIB', '-DDATAFLOW_LIB']
if host_machine.system() == 'windows'
  args += ['-DROSE_UTIL_EXPORTS', '-DNOMINMAX']
endif

install_headers(
  '../dataflowAPI/h/ABI.h',
  '../dataflowAPI/h/Absloc.h',
  '../dataflowAPI/h/AbslocInterface.h',
  '../dataflowAPI/h/bitArray.h',
  '../dataflowAPI/h/InstructionCache.h',
  '../dataflowAPI/h/liveness.h',
  '../dataflowAPI/h/slicing.h',
  '../dataflowAPI/h/stackanalysis.h',
  '../dataflowAPI/h/SymEval.h',
  'h/CFG.h',
  'h/CFGFactory.h',
  'h/CFGModifier.h',
  'h/CodeObject.h',
  'h/CodeSource.h',
  'h/GraphAdapter.h',
  'h/InstructionAdapter.h',
  'h/InstructionSource.h',
  'h/Location.h',
  'h/LockFreeQueue.h',
  'h/ParseCallback.h',
  'h/ParseContainers.h',
  'h/SymLiteCodeSource.h',
)

iface_deps = [common_dep, instructionapi_dep, symreader, boost_dep]
parseAPI_lib = library(
  'parseAPI',
  srcs,
  gnu_symbol_visibility: 'inlineshidden',
  override_options: ['b_ndebug=false'],
  include_directories: include_directories(
    '../common/h',
    '..',
    'src',
    'h',
    '../dataflowAPI/h',
    (get_option('lightweight_symtab') ? ['../symtabAPI/h'] : []),
    # Comes through hacky CMake target trickery
    '../common/src',
    '../instructionAPI/src',
    (get_option('lightweight_symtab') ? ['../symlite/src'] : [
      '../symtabAPI/src',
    ]),
  ),
  c_args: args,
  cpp_args: args,
  dependencies: [iface_deps, openmp_dep],
  version: meson.project_version(),
  soversion: dyninst_soversion,
  install: true,
)
parseapi_dep = declare_dependency(
  link_with: parseAPI_lib,
  include_directories: include_directories('h', '../dataflowAPI/h'),
  dependencies: iface_deps,
)
all_deps += parseapi_dep
