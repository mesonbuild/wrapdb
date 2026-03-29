project('bgfx', 'c', 'cpp',
  version: '1.142.9197',
  license: 'BSD-2-Clause',
  meson_version: '>=1.1.0',
  default_options: ['cpp_std=c++20'],
)

if host_machine.system() == 'darwin'
  add_languages('objc', 'objcpp', native: false, required: true)
  # bgfx uses manual retain/release — do NOT add -fobjc-arc
endif

# MSVC: conformant preprocessor for __VA_OPT__ support (tint, etc.)
# /Zc:__cplusplus is already set by meson via cpp_std=c++20
# /EHs-c- is bx-only (PRIVATE) — see bx/meson.build
if meson.get_compiler('cpp').get_id() == 'msvc'
  add_project_arguments('/Zc:preprocessor', language: ['c', 'cpp'])
endif

# ============================================================================
# Resolve cmake_dependent_option logic
# ============================================================================

# cmake: cmake_dependent_option(BGFX_BUILD_TOOLS_* ... BGFX_BUILD_TOOLS OFF)
# When bgfx_build_tools=false, all tool sub-options are forced OFF.
opt_build_tools          = get_option('bgfx_build_tools')
opt_build_tools_bin2c    = opt_build_tools and get_option('bgfx_build_tools_bin2c')
opt_build_tools_shader   = opt_build_tools and get_option('bgfx_build_tools_shader')
opt_build_tools_geometry = opt_build_tools and get_option('bgfx_build_tools_geometry')
opt_build_tools_texture  = opt_build_tools and get_option('bgfx_build_tools_texture')

# cmake: cmake_dependent_option(BGFX_BUILD_EXAMPLE_COMMON ...
#         OFF "NOT BGFX_BUILD_EXAMPLES;NOT BGFX_BUILD_TOOLS" ON)
# Condition: "NOT examples AND NOT tools" → forced OFF.
# Otherwise: user option (default ON).
# Translation: example_common is ON only when (examples OR tools) AND user option.
opt_build_examples       = get_option('bgfx_build_examples')
opt_build_example_common = (opt_build_examples or opt_build_tools) and get_option('bgfx_build_example_common')

# cmake: cmake_dependent_option(BGFX_CONFIG_MULTITHREADED ... ON
#         "NOT CMAKE_SYSTEM_NAME STREQUAL Emscripten" OFF)
# Translation: ON unless building for Emscripten.
opt_multithreaded = get_option('bgfx_config_multithreaded')
# (Emscripten cross-build would need a cross-file to override this)

# cmake: cmake_dependent_option(BGFX_WITH_WAYLAND ... ON
#         "CMAKE_SYSTEM_NAME STREQUAL Linux" OFF)
# Translation: only meaningful on Linux.
opt_with_wayland = host_machine.system() == 'linux' and get_option('bgfx_with_wayland')

# ============================================================================
# Collect BGFX_CONFIG_* defines from options
# ============================================================================

bgfx_config_args = []

if opt_multithreaded
  bgfx_config_args += '-DBGFX_CONFIG_MULTITHREADED=1'
else
  bgfx_config_args += '-DBGFX_CONFIG_MULTITHREADED=0'
endif

if get_option('bgfx_config_renderer_webgpu')
  bgfx_config_args += '-DBGFX_CONFIG_RENDERER_WEBGPU=1'
endif

if get_option('bgfx_config_debug_annotation')
  bgfx_config_args += '-DBGFX_CONFIG_DEBUG_ANNOTATION=1'
endif

if get_option('bgfx_opengl_version') != ''
  bgfx_config_args += '-DBGFX_CONFIG_RENDERER_OPENGL_MIN_VERSION=' + get_option('bgfx_opengl_version')
endif

if get_option('bgfx_opengles_version') != ''
  bgfx_config_args += '-DBGFX_CONFIG_RENDERER_OPENGLES_MIN_VERSION=' + get_option('bgfx_opengles_version')
endif

# Resource limit overrides (empty = use bgfx defaults)
foreach pair : [
  ['bgfx_config_max_draw_calls', 'BGFX_CONFIG_MAX_DRAW_CALLS'],
  ['bgfx_config_max_views', 'BGFX_CONFIG_MAX_VIEWS'],
  ['bgfx_config_max_frame_buffers', 'BGFX_CONFIG_MAX_FRAME_BUFFERS'],
  ['bgfx_config_max_vertex_layouts', 'BGFX_CONFIG_MAX_VERTEX_LAYOUTS'],
  ['bgfx_config_max_vertex_buffers', 'BGFX_CONFIG_MAX_VERTEX_BUFFERS'],
  ['bgfx_config_max_dynamic_vertex_buffers', 'BGFX_CONFIG_MAX_DYNAMIC_VERTEX_BUFFERS'],
  ['bgfx_config_max_index_buffers', 'BGFX_CONFIG_MAX_INDEX_BUFFERS'],
  ['bgfx_config_max_dynamic_index_buffers', 'BGFX_CONFIG_MAX_DYNAMIC_INDEX_BUFFERS'],
  ['bgfx_config_max_textures', 'BGFX_CONFIG_MAX_TEXTURES'],
  ['bgfx_config_max_texture_samplers', 'BGFX_CONFIG_MAX_TEXTURE_SAMPLERS'],
  ['bgfx_config_max_shaders', 'BGFX_CONFIG_MAX_SHADERS'],
  ['bgfx_config_default_max_encoders', 'BGFX_CONFIG_DEFAULT_MAX_ENCODERS'],
  ['bgfx_config_sort_key_num_bits_program', 'BGFX_CONFIG_SORT_KEY_NUM_BITS_PROGRAM'],
]
  if get_option(pair[0]) != ''
    bgfx_config_args += '-D@0@=@1@'.format(pair[1], get_option(pair[0]))
  endif
endforeach

# ============================================================================
# Libraries (always built)
# ============================================================================

subdir('bx')    # → bx_dep
subdir('bimg')  # → bimg_dep, bimg_decode_dep, bimg_encode_dep
subdir('bgfx')  # → bgfx_dep, imgui_dep (if opt_build_example_common)

# ============================================================================
# Tools (gated by options, respecting cmake_dependent_option logic)
# ============================================================================

if opt_build_tools_bin2c
  subdir('bx/tools/bin2c')
endif

if opt_build_tools_shader
  subdir('bgfx/tools/shaderc')
endif

if opt_build_tools_geometry
  subdir('bgfx/tools/geometryc')
  subdir('bgfx/tools/geometryv')
endif

if opt_build_tools_texture
  subdir('bimg/tools/texturec')
  subdir('bgfx/tools/texturev')
endif

# ============================================================================
# Tests (gated by bgfx_build_tests)
# ============================================================================

if get_option('bgfx_build_tests')
  subdir('bx/tests')
endif
