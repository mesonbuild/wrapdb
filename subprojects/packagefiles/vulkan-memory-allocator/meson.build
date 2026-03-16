project(
  'VulkanMemoryAllocator',
  ['c', 'cpp'],
  license: 'MIT',
  meson_version: '>=0.56.0',
  version: '3.3.0',
)

vma_allocator_dep = declare_dependency(
  include_directories: 'include',
)

meson.override_dependency(
  'VulkanMemoryAllocator',
  vma_allocator_dep,
)

if get_option('build_samples')
  subdir('src')
endif
