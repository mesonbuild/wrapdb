# glslang

glslang_sources = files(
  # glslang/CInterface/
  './glslang/CInterface/glslang_c_interface.cpp',
  # glslang/GenericCodeGen/
  './glslang/GenericCodeGen/CodeGen.cpp',
  './glslang/GenericCodeGen/Link.cpp',
  # glslang/HLSL/
  './glslang/HLSL/hlslAttributes.cpp',
  './glslang/HLSL/hlslGrammar.cpp',
  './glslang/HLSL/hlslOpMap.cpp',
  './glslang/HLSL/hlslParseables.cpp',
  './glslang/HLSL/hlslParseHelper.cpp',
  './glslang/HLSL/hlslScanContext.cpp',
  './glslang/HLSL/hlslTokenStream.cpp',
  # glslang/MachineIndependent/
  './glslang/MachineIndependent/attribute.cpp',
  './glslang/MachineIndependent/Constant.cpp',
  './glslang/MachineIndependent/glslang_tab.cpp',
  './glslang/MachineIndependent/InfoSink.cpp',
  './glslang/MachineIndependent/Initialize.cpp',
  './glslang/MachineIndependent/Intermediate.cpp',
  './glslang/MachineIndependent/intermOut.cpp',
  './glslang/MachineIndependent/IntermTraverse.cpp',
  './glslang/MachineIndependent/iomapper.cpp',
  './glslang/MachineIndependent/limits.cpp',
  './glslang/MachineIndependent/linkValidate.cpp',
  './glslang/MachineIndependent/parseConst.cpp',
  './glslang/MachineIndependent/ParseContextBase.cpp',
  './glslang/MachineIndependent/ParseHelper.cpp',
  './glslang/MachineIndependent/PoolAlloc.cpp',
  './glslang/MachineIndependent/propagateNoContraction.cpp',
  './glslang/MachineIndependent/reflection.cpp',
  './glslang/MachineIndependent/RemoveTree.cpp',
  './glslang/MachineIndependent/Scan.cpp',
  './glslang/MachineIndependent/ShaderLang.cpp',
  './glslang/MachineIndependent/SpirvIntrinsics.cpp',
  './glslang/MachineIndependent/SymbolTable.cpp',
  './glslang/MachineIndependent/Versions.cpp',
  # glslang/MachineIndependent/preprocessor/
  './glslang/MachineIndependent/preprocessor/Pp.cpp',
  './glslang/MachineIndependent/preprocessor/PpAtom.cpp',
  './glslang/MachineIndependent/preprocessor/PpContext.cpp',
  './glslang/MachineIndependent/preprocessor/PpScanner.cpp',
  './glslang/MachineIndependent/preprocessor/PpTokens.cpp',
  # glslang/ResourceLimits/
  './glslang/ResourceLimits/resource_limits_c.cpp',
  './glslang/ResourceLimits/ResourceLimits.cpp',
  # glslang/stub.cpp
  './glslang/stub.cpp',
  # SPIRV/
  './SPIRV/CInterface/spirv_c_interface.cpp',
  './SPIRV/disassemble.cpp',
  './SPIRV/doc.cpp',
  './SPIRV/GlslangToSpv.cpp',
  './SPIRV/InReadableOrder.cpp',
  './SPIRV/Logger.cpp',
  './SPIRV/SpvBuilder.cpp',
  './SPIRV/SpvPostProcess.cpp',
  './SPIRV/SpvTools.cpp',
)

# Platform-specific OSDependent
if host_machine.system() == 'windows'
  glslang_sources += files(
    './glslang/OSDependent/Windows/ossource.cpp',
  )
else
  glslang_sources += files(
    './glslang/OSDependent/Unix/ossource.cpp',
  )
endif

glslang_lib = static_library('glslang', glslang_sources,
  cpp_args: [
    '-DENABLE_OPT=1',
    '-DENABLE_HLSL=1',
  ],
  include_directories: [
    include_directories('.'),
    include_directories('./glslang/Public'),
    include_directories('./glslang/Include'),
    include_directories('../'),          # bgfx/3rdparty
    include_directories('../spirv-tools/include'),
    include_directories('../spirv-tools/source'),
  ],
  override_options: ['cpp_std=c++17'],
)

glslang_dep = declare_dependency(
  link_with: glslang_lib,
  include_directories: [
    include_directories('.'),
    include_directories('./glslang/Public'),
    include_directories('./glslang/Include'),
  ],
)
