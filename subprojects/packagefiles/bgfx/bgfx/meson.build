# bgfx library + example-common (imgui)

# =============================================================================
# bgfx library
# =============================================================================

# renderer_mtl/vk/webgpu excluded — added per-platform (ObjC++ on macOS, C++ elsewhere)
bgfx_src = files(
  'src/bgfx.cpp',
  'src/debug_renderdoc.cpp',
  'src/dxgi.cpp',
  'src/glcontext_egl.cpp',
  'src/glcontext_html5.cpp',
  'src/glcontext_wgl.cpp',
  'src/nvapi.cpp',
  'src/renderer_agc.cpp',
  'src/renderer_d3d11.cpp',
  'src/renderer_d3d12.cpp',
  'src/renderer_gl.cpp',
  'src/renderer_gnm.cpp',
  'src/renderer_noop.cpp',
  'src/renderer_nvn.cpp',
  'src/shader.cpp',
  'src/shader_dxbc.cpp',
  'src/shader_spirv.cpp',
  'src/topology.cpp',
  'src/vertexlayout.cpp',
)

bgfx_public_inc = include_directories('include')
bgfx_private_inc = include_directories(
  '3rdparty',
  '3rdparty/khronos',
)

bgfx_compile_args = [
  '-D__STDC_LIMIT_MACROS',
  '-D__STDC_FORMAT_MACROS',
  '-D__STDC_CONSTANT_MACROS',
] + bgfx_config_args

bgfx_private_args = []
bgfx_platform_deps = []
bgfx_link_extra = []
bgfx_dx_inc = []

if host_machine.system() == 'darwin'
  bgfx_platform_deps += dependency('appleframeworks',
    modules: ['Cocoa', 'Metal', 'QuartzCore', 'IOKit', 'CoreFoundation'],
  )
  # renderer_mtl/vk/webgpu include ObjC headers on macOS — compile as ObjC++
  bgfx_src_inc = include_directories('src')
  bgfx_objcpp_files = []
  foreach f : ['renderer_mtl', 'renderer_vk', 'renderer_webgpu']
    bgfx_objcpp_files += configure_file(
      input: 'src/' + f + '.cpp',
      output: f + '.mm',
      copy: true,
    )
  endforeach
  bgfx_objcpp_lib = static_library('bgfx_objcpp',
    bgfx_objcpp_files,
    include_directories: [bgfx_public_inc, bgfx_private_inc, bgfx_src_inc],
    dependencies: [bx_dep, bimg_dep],
    objcpp_args: bgfx_compile_args,
  )
  bgfx_link_extra += bgfx_objcpp_lib

elif host_machine.system() == 'linux'
  bgfx_platform_deps += dependency('x11')
  bgfx_platform_deps += dependency('gl')
  bgfx_platform_deps += dependency('threads')
  bgfx_platform_deps += meson.get_compiler('cpp').find_library('dl')
  if opt_with_wayland
    bgfx_private_args += '-DWL_EGL_PLATFORM=1'
    bgfx_platform_deps += dependency('wayland-egl')
  endif
  bgfx_src += files(
    'src/renderer_mtl.cpp',
    'src/renderer_vk.cpp',
    'src/renderer_webgpu.cpp',
  )
  bgfx_dx_inc = include_directories(
    '3rdparty/directx-headers/include/directx',
    '3rdparty/directx-headers/include',
    '3rdparty/directx-headers/include/wsl/stubs',
  )

elif host_machine.system() == 'windows'
  bgfx_private_args += '-D_CRT_SECURE_NO_WARNINGS'
  bgfx_src += files(
    'src/renderer_mtl.cpp',
    'src/renderer_vk.cpp',
    'src/renderer_webgpu.cpp',
  )
  bgfx_dx_inc = include_directories(
    '3rdparty/directx-headers/include/directx',
    '3rdparty/directx-headers/include',
  )
endif

bgfx_lib = static_library('bgfx',
  bgfx_src,
  include_directories: [bgfx_public_inc, bgfx_private_inc] + bgfx_dx_inc,
  dependencies: [bx_dep, bimg_dep] + bgfx_platform_deps,
  cpp_args: bgfx_compile_args + bgfx_private_args,
  link_with: bgfx_link_extra,
)

bgfx_dep = declare_dependency(
  include_directories: bgfx_public_inc,
  link_with: bgfx_lib,
  compile_args: bgfx_compile_args,
  dependencies: bgfx_platform_deps,
)

# =============================================================================
# Shared interface dependencies (cmake: shared.cmake equivalents)
# =============================================================================

# bgfx-vertexlayout — used by shaderc, geometryc, and example-common
bgfx_vertexlayout_src = files('src/vertexlayout.cpp')
bgfx_vertexlayout_dep_list = [bx_dep]
if host_machine.system() == 'darwin'
  bgfx_vertexlayout_dep_list += dependency('appleframeworks', modules: ['Cocoa'])
endif
bgfx_vertexlayout_dep = declare_dependency(
  include_directories: bgfx_public_inc,
  sources: bgfx_vertexlayout_src,
  dependencies: bgfx_vertexlayout_dep_list,
)

# bgfx-shader — used by shaderc
bgfx_shader_src = files(
  'src/shader.cpp',
  'src/shader_dxbc.cpp',
  'src/shader_spirv.cpp',
)
bgfx_shader_dep = declare_dependency(
  include_directories: bgfx_public_inc,
  sources: bgfx_shader_src,
  dependencies: bx_dep,
)

# webgpu — header-only interface (cmake: 3rdparty/webgpu.cmake)
# Only available when webgpu renderer is enabled and the headers exist.
if get_option('bgfx_config_renderer_webgpu')
  webgpu_inc = include_directories('3rdparty/webgpu/include')
  webgpu_dep = declare_dependency(include_directories: webgpu_inc)
else
  webgpu_dep = declare_dependency()
endif

# =============================================================================
# 3rdparty: meshoptimizer (used by geometryc AND example-common)
# =============================================================================

subdir('3rdparty/meshoptimizer')

# =============================================================================
# 3rdparty for shader tools (cmake: if(BGFX_BUILD_TOOLS_SHADER) in CMakeLists.txt)
# =============================================================================

if opt_build_tools_shader
  subdir('3rdparty/fcpp')
  subdir('3rdparty/spirv-cross')
  subdir('3rdparty/spirv-opt')
  subdir('3rdparty/glslang')
  subdir('3rdparty/glsl-optimizer')
  subdir('3rdparty/tint')
endif

# =============================================================================
# example-common (imgui, debugdraw, entry, font, nanovg, ps)
# =============================================================================

# cmake: BGFX_BUILD_EXAMPLE_COMMON is ON unless BOTH examples AND tools are OFF.
# opt_build_example_common is resolved in the root meson.build.
if opt_build_example_common

  subdir('3rdparty/dear-imgui')

  example_common_src = files(
    'examples/common/bgfx_utils.cpp',
    'examples/common/camera.cpp',
    'examples/common/cube_atlas.cpp',
    'examples/common/example-glue.cpp',
    'examples/common/debugdraw/debugdraw.cpp',
    'examples/common/entry/cmd.cpp',
    'examples/common/entry/dialog.cpp',
    'examples/common/entry/entry.cpp',
    'examples/common/entry/entry_android.cpp',
    'examples/common/entry/entry_glfw.cpp',
    'examples/common/entry/entry_html5.cpp',
    'examples/common/entry/entry_noop.cpp',
    'examples/common/entry/entry_sdl.cpp',
    'examples/common/entry/entry_windows.cpp',
    'examples/common/entry/entry_x11.cpp',
    'examples/common/entry/input.cpp',
    'examples/common/font/font_manager.cpp',
    'examples/common/font/text_buffer_manager.cpp',
    'examples/common/font/text_metrics.cpp',
    'examples/common/font/utf8.cpp',
    'examples/common/imgui/imgui.cpp',
    'examples/common/nanovg/nanovg.cpp',
    'examples/common/nanovg/nanovg_bgfx.cpp',
    'examples/common/ps/particle_system.cpp',
  )

  if host_machine.system() == 'darwin'
    example_common_src += files(
      'examples/common/entry/dialog_darwin.mm',
      'examples/common/entry/entry_osx.mm',
    )
  endif

  example_common_public_inc = include_directories(
    'examples/common',
    '3rdparty',
  )

  example_common_platform_deps = []
  if host_machine.system() == 'linux'
    example_common_platform_deps += dependency('x11')
  endif

  example_common_lib = static_library('example-common',
    dear_imgui_src + meshoptimizer_src + example_common_src,
    include_directories: [example_common_public_inc, bgfx_public_inc, bgfx_private_inc],
    dependencies: [bgfx_dep, bx_dep, bimg_dep, bimg_decode_dep] + example_common_platform_deps,
    cpp_args: ['-D__STDC_FORMAT_MACROS', '-D_CRT_SECURE_NO_WARNINGS'],
  )

  imgui_dep = declare_dependency(
    include_directories: [example_common_public_inc, bgfx_public_inc],
    link_with: example_common_lib,
    dependencies: [bgfx_dep, bx_dep, bimg_dep, bimg_decode_dep],
  )
else
  imgui_dep = disabler()
endif

# =============================================================================
# Examples (gated by bgfx_build_examples)
# =============================================================================

if opt_build_examples
  subdir('examples')
endif
