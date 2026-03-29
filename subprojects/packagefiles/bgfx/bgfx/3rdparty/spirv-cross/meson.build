# spirv-cross

spirv_cross_sources = files(
  'spirv_cfg.cpp',
  'spirv_cpp.cpp',
  'spirv_cross.cpp',
  'spirv_cross_parsed_ir.cpp',
  'spirv_cross_util.cpp',
  'spirv_glsl.cpp',
  'spirv_hlsl.cpp',
  'spirv_msl.cpp',
  'spirv_parser.cpp',
  'spirv_reflect.cpp',
)

spirv_cross_lib = static_library('spirv-cross', spirv_cross_sources,
  cpp_args: ['-DSPIRV_CROSS_EXCEPTIONS_TO_ASSERTIONS'],
  include_directories: [
    include_directories('.'),
    include_directories('include'),
  ],
  override_options: ['cpp_std=c++17'],
)

spirv_cross_dep = declare_dependency(
  link_with: spirv_cross_lib,
  include_directories: include_directories('.'),
)
