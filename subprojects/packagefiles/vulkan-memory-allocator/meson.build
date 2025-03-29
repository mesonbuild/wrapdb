project(
  'VulkanMemoryAllocator',
  ['c', 'cpp'],
  version: '3.1.0',
)

vma_allocator_dep = declare_dependency(
  include_directories: 'include',
)

if get_option('build_samples')
  subdir('src')
endif
