project(
  'vulkan-headers',
  'c',
  license : 'Apache-2.0',
  version : '1.2.158',
)

vulkan_api_xml = files(join_paths('registry', 'vk.xml'))

vulkan_headers_dep = declare_dependency(
  include_directories : include_directories('include'),
)
