incdir = include_directories('inc')

azure_storage_file_datalake_header = ['inc/azure/storage/files/datalake.hpp']
install_headers(
  azure_storage_file_datalake_header,
  subdir: 'azure/storage/files',
)

azure_storage_file_datalake_headers = [
  'inc/azure/storage/files/datalake/datalake_directory_client.hpp',
  'inc/azure/storage/files/datalake/datalake_file_client.hpp',
  'inc/azure/storage/files/datalake/datalake_file_system_client.hpp',
  'inc/azure/storage/files/datalake/datalake_lease_client.hpp',
  'inc/azure/storage/files/datalake/datalake_options.hpp',
  'inc/azure/storage/files/datalake/datalake_path_client.hpp',
  'inc/azure/storage/files/datalake/datalake_responses.hpp',
  'inc/azure/storage/files/datalake/datalake_sas_builder.hpp',
  'inc/azure/storage/files/datalake/datalake_service_client.hpp',
  'inc/azure/storage/files/datalake/dll_import_export.hpp',
  'inc/azure/storage/files/datalake/rest_client.hpp',
  'inc/azure/storage/files/datalake/rtti.hpp',
]
install_headers(
  azure_storage_file_datalake_headers,
  subdir: 'azure/storage/files/datalake',
)

azure_storage_file_datalake_headers_all = azure_storage_file_datalake_header + azure_storage_file_datalake_headers

azure_storage_files_datalake_sources = [
  'src/datalake_directory_client.cpp',
  'src/datalake_file_client.cpp',
  'src/datalake_file_system_client.cpp',
  'src/datalake_lease_client.cpp',
  'src/datalake_options.cpp',
  'src/datalake_path_client.cpp',
  'src/datalake_responses.cpp',
  'src/datalake_sas_builder.cpp',
  'src/datalake_service_client.cpp',
  'src/datalake_utilities.cpp',
  'src/private/datalake_constants.hpp',
  'src/private/datalake_utilities.hpp',
  'src/private/package_version.hpp',
  'src/rest_client.cpp',
]

azure_storage_files_datalake_args = []
if get_option('default_library') != 'static'
  azure_storage_files_datalake_args += ['-DAZ_STORAGE_FILES_DATALAKE_DLL']
endif

azure_storage_files_datalake_lib = library(
  'azure-storage-files-datalake',
  sources: azure_storage_file_datalake_headers_all + azure_storage_files_datalake_sources,
  include_directories: incdir,
  dependencies: azure_storage_blobs_dep,
  cpp_args: ['-DAZ_STORAGE_FILES_DATALAKE_BEING_BUILT'] + azure_storage_files_datalake_args,
)

azure_storage_files_datalake_dep = declare_dependency(
  link_with: azure_storage_files_datalake_lib,
  include_directories: incdir,
  dependencies: azure_storage_blobs_dep,
  compile_args: azure_storage_files_datalake_args,
)
