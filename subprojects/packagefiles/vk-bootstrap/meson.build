project(
  'vk-bootstrap',
  'cpp',
  version: '8.2.4',
  license: 'MIT',
  meson_version: '>=0.56.0',
)

vk_bootstrap_inc = include_directories('src')

vulkan_dep = dependency(
  'vulkan',
  required: true,
  fallback: ['vulkan-headers', 'vulkan_headers_dep'],
)

vk_bootstrap_lib = static_library(
  'vk-bootstrap',
  ['src/VkBootstrap.cpp'],
  include_directories: vk_bootstrap_inc,
  dependencies: [vulkan_dep],
)

vk_bootstrap_dep = declare_dependency(
  include_directories: vk_bootstrap_inc,
  link_with: vk_bootstrap_lib,
  dependencies: [vulkan_dep],
)

meson.override_dependency('vk-bootstrap', vk_bootstrap_dep)
