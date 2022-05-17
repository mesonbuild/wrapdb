project('imgui', 'cpp',
    version: '1.87',
    license: 'MIT',
)

if host_machine.system() == 'darwin'
    add_languages('objcpp')
    #hack for current version - fixed in next
    add_project_arguments('-fobjc-weak', language: 'objcpp')
endif

include_dirs = include_directories('.', 'backends')
sources = ['imgui_demo.cpp', 'imgui_draw.cpp', 'imgui_tables.cpp', 'imgui_widgets.cpp', 'imgui.cpp', 'misc/cpp/imgui_stdlib.cpp']

cpp = meson.get_compiler('cpp')
if cpp.get_argument_syntax() == 'msvc'
  if get_option('buildtype') != 'static'
    add_project_arguments('-DIMGUI_API=__declspec(dllexport)', language: 'cpp')
  else
    add_project_arguments('-DIMGUI_API=__declspec(dllimport)', language: 'cpp')
  endif
endif

dependencies = []

# renderer backends
dx9_dep = cpp.find_library('d3d9', required: get_option('dx9'))
if dx9_dep.found()
    sources += 'backends/imgui_impl_dx9.cpp'
    dependencies += dx9_dep
endif
dx10_dep = cpp.find_library('d3d10', required: get_option('dx10'))
if dx10_dep.found()
    sources += 'backends/imgui_impl_dx10.cpp'
    dependencies += dx10_dep
endif
dx11_dep = cpp.find_library('d3d11', required: get_option('dx11'))
if dx11_dep.found()
    sources += 'backends/imgui_impl_dx11.cpp'
    dependencies += dx11_dep
endif
dx12_dep = cpp.find_library('d3d12', required: get_option('dx12'))
if dx12_dep.found()
    sources += 'backends/imgui_impl_dx12.cpp'
    dependencies += dx12_dep
endif
metal_dep = dependency('appleframeworks', modules : [ 'Foundation', 'AppKit', 'GameController', 'Metal' ], required: get_option('metal'))
if metal_dep.found()
    sources += 'backends/imgui_impl_metal.mm'
    dependencies += metal_dep
endif
libdl_dep = cpp.find_library('dl', required: get_option('opengl'))
if libdl_dep.found()
    sources += 'backends/imgui_impl_opengl3.cpp'
    dependencies += libdl_dep
endif
sdl2_renderer_dep = dependency('sdl2', version: '>=2.0.17', required: get_option('sdl_renderer'))
if sdl2_renderer_dep.found()
    sources += 'backends/imgui_impl_sdlrenderer.cpp'
    dependencies += sdl2_renderer_dep
endif
vulkan_dep = dependency('vulkan', required: get_option('vulkan'))
if vulkan_dep.found()
    sources += 'backends/imgui_impl_vulkan.cpp'
    dependencies += vulkan_dep
endif
if cpp.has_header('webgpu/webgpu.h', required: get_option('webgpu'))
    sources += 'backends/imgui_impl_wgpu.cpp'
endif

# platform backends
glfw_dep = dependency('glfw3', required: get_option('glfw'))
if glfw_dep.found()
    sources += 'backends/imgui_impl_glfw.cpp'
    dependencies += glfw_dep
endif
sdl2_dep = dependency('sdl2', required: get_option('sdl2'))
if sdl2_dep.found()
    sources += 'backends/imgui_impl_sdl.cpp'
    dependencies += sdl2_dep
endif
if get_option('osx').enabled() or (get_option('osx').auto() and target_machine.system() == 'darwin')
    sources += 'backends/imgui_impl_osx.mm'
endif
if get_option('win').enabled() or (get_option('win').auto() and target_machine.system() == 'windows')
    sources += 'backends/imgui_impl_win32.cpp'
endif

# frameworks
allegro5_dep = dependency('allegro-5', required: get_option('allegro5'))
allegro5_primitives_dep = dependency('allegro_primitives-5', required: get_option('allegro5'))
if allegro5_dep.found() and allegro5_primitives_dep.found()
    sources += 'backends/imgui_impl_allegro5.cpp'
    dependencies += [allegro5_dep, allegro5_primitives_dep]
endif

imgui = library('imgui',
    sources,
    dependencies: dependencies,
    include_directories: include_dirs,
)

imgui_dep = declare_dependency(include_directories: include_dirs, link_with: imgui)
