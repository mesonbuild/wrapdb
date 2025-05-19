incdir = include_directories('inc')

azure_identity_headers = [
  'inc/azure/identity.hpp',
  'inc/azure/identity/azure_cli_credential.hpp',
  'inc/azure/identity/azure_pipelines_credential.hpp',
  'inc/azure/identity/chained_token_credential.hpp',
  'inc/azure/identity/client_assertion_credential.hpp',
  'inc/azure/identity/client_certificate_credential.hpp',
  'inc/azure/identity/client_secret_credential.hpp',
  'inc/azure/identity/default_azure_credential.hpp',
  'inc/azure/identity/detail/client_credential_core.hpp',
  'inc/azure/identity/detail/token_cache.hpp',
  'inc/azure/identity/dll_import_export.hpp',
  'inc/azure/identity/environment_credential.hpp',
  'inc/azure/identity/managed_identity_credential.hpp',
  'inc/azure/identity/rtti.hpp',
  'inc/azure/identity/workload_identity_credential.hpp',
]

install_headers(
  azure_identity_headers,
  subdir: 'azure/identity',
)

azure_identity_sources = [
  'src/azure_cli_credential.cpp',
  'src/azure_pipelines_credential.cpp',
  'src/chained_token_credential.cpp',
  'src/client_assertion_credential.cpp',
  'src/client_certificate_credential.cpp',
  'src/client_credential_core.cpp',
  'src/client_secret_credential.cpp',
  'src/default_azure_credential.cpp',
  'src/environment_credential.cpp',
  'src/managed_identity_credential.cpp',
  'src/managed_identity_source.cpp',
  'src/private/chained_token_credential_impl.hpp',
  'src/private/client_assertion_credential_impl.hpp',
  'src/private/identity_log.hpp',
  'src/private/managed_identity_source.hpp',
  'src/private/package_version.hpp',
  'src/private/tenant_id_resolver.hpp',
  'src/private/token_credential_impl.hpp',
  'src/tenant_id_resolver.cpp',
  'src/token_cache.cpp',
  'src/token_credential_impl.cpp',
  'src/workload_identity_credential.cpp',
]

azure_identity_args = []
if get_option('default_library') != 'static'
  azure_identity_args += ['-DAZ_IDENTIFY_DLL']
endif

azure_identity_lib = library(
  'azure-identity',
  sources: [azure_identity_sources],
  include_directories: incdir,
  dependencies: [azure_core_dep, azure_crypto_dep],
  cpp_args: ['-DAZ_IDENTIFY_BEING_BUILT'] + azure_identity_args,
)

azure_identity_dep = declare_dependency(
  link_with: azure_identity_lib,
  include_directories: incdir,
  dependencies: azure_core_dep,
  compile_args: azure_identity_args,
)
