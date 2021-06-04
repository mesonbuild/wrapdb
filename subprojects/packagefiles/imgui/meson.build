project('imgui', 'cpp',
    version: '1.81',
    license: 'MIT',
)

include_dirs = include_directories('.', 'backends')
sources = ['imgui_demo.cpp', 'imgui_draw.cpp', 'imgui_tables.cpp', 'imgui_widgets.cpp', 'imgui.cpp']

cpp = meson.get_compiler('cpp')
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
metal_dep = cpp.find_library('metal', required: get_option('metal'))
if get_option('metal').enabled()
    sources += 'backends/imgui_impl_metal.mm'
    dependencies += metal_dep
endif
glew_dep = dependency('glew', required: get_option('opengl'))
if glew_dep.found()
    sources += 'backends/imgui_impl_opengl3.cpp'
    dependencies += glew_dep
endif
vulkan_dep = dependency('vulkan', required: get_option('vulkan'))
if vulkan_dep.found()
    sources += 'backends/imgui_impl_vulkan.cpp'
    dependencies += vulkan_dep
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
allegro5_dep = dependency('allegro5', required: get_option('allegro5'))
if allegro5_dep.found()
    sources += 'backends/imgui_impl_allegro5.cpp'
    dependencies += allegro5_dep
endif
marmalade_dep = cpp.find_library('marmalade', required: get_option('marmalade'))
if marmalade_dep.found()
    sources += 'backends/imgui_impl_marmalade.cpp'
    dependencies += marmalade_dep
endif

imgui = library('imgui',
    sources,
    dependencies: dependencies,
    include_directories: include_dirs,
)

imgui_dep = declare_dependency(include_directories: include_dirs, link_with: imgui)
