project(
  'sfml',
  'cpp',
  license: 'Zlib',
  version: '3.0.2',
  default_options: ['wrap_mode=forcefallback'],
  meson_version: '>=0.64.0',
)

cpp = meson.get_compiler('cpp')

thread_dep = dependency('threads')
gl_dep = dependency('gl')
winmm_dep = cpp.find_library(
  'winmm',
  required: host_machine.system() == 'windows',
)
w32_dep = cpp.find_library(
  'ws2_32',
  required: host_machine.system() == 'windows',
)

stb_inc = include_directories('extlibs/headers/stb_image')
glad_inc = include_directories('extlibs/headers/glad/include')
vulkan_inc = include_directories('extlibs/headers/vulkan')
mp3_inc = include_directories('extlibs/headers/minimp3')
pub_inc = include_directories('include')
priv_inc = include_directories('src')

if build_machine.endian() == 'big'
  add_project_arguments(
    '-DSFML_IS_BIG_ENDIAN=1',
    language: 'cpp',
  )
else
  add_project_arguments(
    '-DSFML_IS_BIG_ENDIAN=0',
    language: 'cpp',
  )
endif

# workaround issue (#14939) in Meson 1.8.4 - 1.9.0, where
# default_options:['cpp_std=c++17'] doesn't work under certain circumstances
override_opts = ['cpp_std=c++17']

sfml_libs = []
subdir('src/SFML')

compile_args = get_option('default_library') == 'static' ? '-DSFML_STATIC' : []

sfml_dep = declare_dependency(
  include_directories: pub_inc,
  link_with: sfml_libs,
  compile_args: compile_args,
)
meson.override_dependency('sfml', sfml_dep)
meson.override_dependency('sfml-all', sfml_dep)

if get_option('examples') and build_machine.system() != 'android'
  subdir('examples')
endif
