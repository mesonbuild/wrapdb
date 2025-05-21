incdir = include_directories('inc')

azure_storage_common_headers = [
  'inc/azure/storage/common/access_conditions.hpp',
  'inc/azure/storage/common/account_sas_builder.hpp',
  'inc/azure/storage/common/crypt.hpp',
  'inc/azure/storage/common/dll_import_export.hpp',
  'inc/azure/storage/common/internal/concurrent_transfer.hpp',
  'inc/azure/storage/common/internal/constants.hpp',
  'inc/azure/storage/common/internal/file_io.hpp',
  'inc/azure/storage/common/internal/reliable_stream.hpp',
  'inc/azure/storage/common/internal/shared_key_policy.hpp',
  'inc/azure/storage/common/internal/storage_bearer_token_auth.hpp',
  'inc/azure/storage/common/internal/storage_bearer_token_authentication_policy.hpp',
  'inc/azure/storage/common/internal/storage_per_retry_policy.hpp',
  'inc/azure/storage/common/internal/storage_service_version_policy.hpp',
  'inc/azure/storage/common/internal/storage_switch_to_secondary_policy.hpp',
  'inc/azure/storage/common/internal/xml_wrapper.hpp',
  'inc/azure/storage/common/rtti.hpp',
  'inc/azure/storage/common/storage_common.hpp',
  'inc/azure/storage/common/storage_credential.hpp',
  'inc/azure/storage/common/storage_exception.hpp',
]
install_headers(
  azure_storage_common_headers,
  subdir: 'azure/storage/common/',
)

azure_storage_common_sources = [
  'src/account_sas_builder.cpp',
  'src/crypt.cpp',
  'src/file_io.cpp',
  'src/private/package_version.hpp',
  'src/reliable_stream.cpp',
  'src/shared_key_policy.cpp',
  'src/storage_bearer_token_authentication_policy.cpp',
  'src/storage_credential.cpp',
  'src/storage_exception.cpp',
  'src/storage_per_retry_policy.cpp',
  'src/storage_switch_to_secondary_policy.cpp',
  'src/xml_wrapper.cpp',
]

azure_storage_common_args = []
if get_option('default_library') != 'static'
  azure_storage_common_args += ['-DAZ_STORAGE_COMMON_DLL']
endif

if host_machine.system() == 'windows'
  cc = meson.get_compiler('cpp')
  webservices_dep = cc.find_library('webservices')
  azure_storage_common_web_dep = webservices_dep
else
  libxml2_dep = dependency('libxml-2.0')
  azure_storage_common_web_dep = libxml2_dep
endif

azure_storage_common_lib = library(
  'azure-storage-common',
  sources: azure_storage_common_headers + azure_storage_common_sources,
  include_directories: incdir,
  dependencies: [azure_core_dep, azure_crypto_dep, azure_storage_common_web_dep],
  cpp_args: ['-DAZ_STORAGE_COMMON_BEING_BUILT'] + azure_storage_common_args,
)

azure_storage_common_dep = declare_dependency(
  link_with: azure_storage_common_lib,
  include_directories: incdir,
  dependencies: azure_core_dep,
  compile_args: azure_storage_common_args,
)
