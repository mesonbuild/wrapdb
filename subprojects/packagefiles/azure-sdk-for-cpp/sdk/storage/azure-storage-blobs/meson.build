incdir = include_directories('inc')

azure_storage_blob_header = ['inc/azure/storage/blobs.hpp']
install_headers(
  azure_storage_blob_header,
  subdir: 'azure/storage',
)

azure_storage_blobs_headers = [
  'inc/azure/storage/blobs/append_blob_client.hpp',
  'inc/azure/storage/blobs/blob_batch.hpp',
  'inc/azure/storage/blobs/blob_client.hpp',
  'inc/azure/storage/blobs/blob_container_client.hpp',
  'inc/azure/storage/blobs/blob_lease_client.hpp',
  'inc/azure/storage/blobs/blob_options.hpp',
  'inc/azure/storage/blobs/blob_responses.hpp',
  'inc/azure/storage/blobs/blob_sas_builder.hpp',
  'inc/azure/storage/blobs/blob_service_client.hpp',
  'inc/azure/storage/blobs/block_blob_client.hpp',
  'inc/azure/storage/blobs/deferred_response.hpp',
  'inc/azure/storage/blobs/dll_import_export.hpp',
  'inc/azure/storage/blobs/page_blob_client.hpp',
  'inc/azure/storage/blobs/rest_client.hpp',
  'inc/azure/storage/blobs/rtti.hpp',
]
install_headers(
  azure_storage_blobs_headers,
  subdir: 'azure/storage/blobs',
)

azure_storage_blobs_headers_all = azure_storage_blob_header + azure_storage_blobs_headers

azure_storage_blobs_sources = [
  'src/append_blob_client.cpp',
  'src/blob_batch.cpp',
  'src/blob_client.cpp',
  'src/blob_container_client.cpp',
  'src/blob_lease_client.cpp',
  'src/blob_options.cpp',
  'src/blob_responses.cpp',
  'src/blob_sas_builder.cpp',
  'src/blob_service_client.cpp',
  'src/block_blob_client.cpp',
  'src/page_blob_client.cpp',
  'src/private/avro_parser.cpp',
  'src/private/avro_parser.hpp',
  'src/private/package_version.hpp',
  'src/rest_client.cpp',
]

azure_storage_blobs_args = []
if get_option('default_library') != 'static'
  azure_storage_blobs_args += ['-DAZ_STORAGE_BLOBS_DLL']
endif

azure_storage_blobs_lib = library(
  'azure-storage-blobs',
  sources: azure_storage_blobs_headers_all + azure_storage_blobs_sources,
  include_directories: incdir,
  dependencies: azure_storage_common_dep,
  cpp_args: ['-DAZ_STORAGE_BLOBS_BEING_BUILT'] + azure_storage_blobs_args,
)

azure_storage_blobs_dep = declare_dependency(
  link_with: azure_storage_blobs_lib,
  include_directories: incdir,
  dependencies: azure_storage_common_dep,
  compile_args: azure_storage_blobs_args,
)
