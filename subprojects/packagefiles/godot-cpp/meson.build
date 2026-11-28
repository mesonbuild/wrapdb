project(
  'godot-cpp',
  'cpp',
  license: 'MIT',
  version: '10.0.0',
  default_options: ['cpp_std=c++17'],
  meson_version: '>=0.63',
)

cpp_compiler = meson.get_compiler('cpp')
godot_api_version = get_option('api_version')

generated_include_directory = f'@godot_api_version@/gen/include/'

# Existence of version-named directory implies the sources have been generated already
fs = import('fs')
if not fs.exists(generated_include_directory)
  message(f'Generating classes for Godot @godot_api_version@')
  result = run_command(
    './meson-bindings-generator.py',
    godot_api_version,
    check: true,
  )
endif

# The subdirectory handles retrieving the map of common and expected version-specific generated sources.
subdir('meson_sources')

includes = include_directories(
  'include/',
  generated_include_directory,
)

godot_cpp_lib = static_library(
  'libgodot-cpp',
  common_sources + version_specific_sources,
  include_directories: includes,
)

godot_cpp_dep = declare_dependency(
  include_directories: includes,
  link_with: [godot_cpp_lib],
)

meson.override_dependency('godot-cpp', godot_cpp_dep)

