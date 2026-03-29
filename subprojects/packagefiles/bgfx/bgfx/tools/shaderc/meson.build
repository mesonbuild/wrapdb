# shaderc - bgfx shader compiler
# 3rdparty deps (fcpp, spirv-cross, spirv-opt, glslang, glsl-optimizer, tint)
# are defined in bgfx/3rdparty/ and included by bgfx/meson.build.

# ============================================================================
# shaderc executable
# ============================================================================
shaderc_sources = files(
  'shaderc.cpp',
  'shaderc.h',
  'shaderc_dxil.cpp',
  'shaderc_glsl.cpp',
  'shaderc_hlsl.cpp',
  'shaderc_metal.cpp',
  'shaderc_pssl.cpp',
  'shaderc_spirv.cpp',
  'shaderc_wgsl.cpp',
)

shaderc_include_dirs = [
  include_directories('../../3rdparty/dawn'),
  include_directories('../../3rdparty/dawn/src'),
  include_directories('../../3rdparty/dawn/include'),
]

# On Linux, add directx-headers for DXC support
if host_machine.system() == 'linux'
  shaderc_include_dirs += [
    include_directories('../../3rdparty/directx-headers/include/directx'),
    include_directories('../../3rdparty/directx-headers/include'),
    include_directories('../../3rdparty/directx-headers/include/wsl/stubs'),
  ]
endif

shaderc_deps = [
  bx_dep,
  bimg_dep,
  bgfx_vertexlayout_dep,
  bgfx_shader_dep,
  fcpp_dep,
  glslang_dep,
  glsl_optimizer_dep,
  spirv_opt_dep,
  spirv_cross_dep,
  tint_dep,
]

shaderc = executable('shaderc', shaderc_sources,
  include_directories: shaderc_include_dirs,
  dependencies: shaderc_deps,
  override_options: ['cpp_std=c++20'],
)
