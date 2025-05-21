incdir = include_directories('inc')

azure_core_headers = {
  'azure/core': [
    'inc/azure/core.hpp',
    'inc/azure/core/azure_assert.hpp',
    'inc/azure/core/base64.hpp',
    'inc/azure/core/case_insensitive_containers.hpp',
    'inc/azure/core/context.hpp',
    'inc/azure/core/credentials/credentials.hpp',
    'inc/azure/core/credentials/token_credential_options.hpp',
    'inc/azure/core/cryptography/hash.hpp',
    'inc/azure/core/datetime.hpp',
    'inc/azure/core/diagnostics/logger.hpp',
    'inc/azure/core/dll_import_export.hpp',
    'inc/azure/core/etag.hpp',
    'inc/azure/core/exception.hpp',
    'inc/azure/core/match_conditions.hpp',
    'inc/azure/core/modified_conditions.hpp',
    'inc/azure/core/nullable.hpp',
    'inc/azure/core/operation.hpp',
    'inc/azure/core/operation_status.hpp',
    'inc/azure/core/paged_response.hpp',
    'inc/azure/core/platform.hpp',
    'inc/azure/core/response.hpp',
    'inc/azure/core/rtti.hpp',
    'inc/azure/core/url.hpp',
    'inc/azure/core/uuid.hpp',
  ],
  'azure/core/http': [
    'inc/azure/core/http/http.hpp',
    'inc/azure/core/http/http_status_code.hpp',
    'inc/azure/core/http/policies/policy.hpp',
    'inc/azure/core/http/raw_response.hpp',
    'inc/azure/core/http/transport.hpp',
  ],
  'azure/core/internal': [
    'inc/azure/core/internal/client_options.hpp',
    'inc/azure/core/internal/contract.hpp',
    'inc/azure/core/internal/environment.hpp',
    'inc/azure/core/internal/extendable_enumeration.hpp',
    'inc/azure/core/internal/strings.hpp',
    'inc/azure/core/internal/unique_handle.hpp',
  ],
  'azure/core/internal/credentials': [
    'inc/azure/core/internal/credentials/authorization_challenge_parser.hpp',
  ],
  'azure/core/internal/cryptography': [
    'inc/azure/core/internal/cryptography/sha_hash.hpp',
  ],
  'azure/core/internal/diagnostics': [
    'inc/azure/core/internal/diagnostics/global_exception.hpp',
    'inc/azure/core/internal/diagnostics/log.hpp',
  ],
  'azure/core/internal/http': [
    'inc/azure/core/internal/http/http_sanitizer.hpp',
    'inc/azure/core/internal/http/pipeline.hpp',
    'inc/azure/core/internal/http/user_agent.hpp',
  ],
  'azure/core/internal/io': ['inc/azure/core/internal/io/null_body_stream.hpp'],
  'azure/core/internal/json': [
    'inc/azure/core/internal/json/json.hpp',
    'inc/azure/core/internal/json/json_optional.hpp',
    'inc/azure/core/internal/json/json_serializable.hpp',
  ],
  'azure/core/internal/tracing': [
    'inc/azure/core/internal/tracing/service_tracing.hpp',
    'inc/azure/core/internal/tracing/tracing_impl.hpp',
  ],
  'azure/core/io': ['inc/azure/core/io/body_stream.hpp'],
  'azure/core/tracing': ['inc/azure/core/tracing/tracing.hpp'],
}

azure_core_header_files = []
foreach subdir, files : azure_core_headers
  install_headers(
    files,
    subdir: subdir,
  )
  azure_core_header_files += files
endforeach

azure_core_sources = [
  'src/azure_assert.cpp',
  'src/base64.cpp',
  'src/context.cpp',
  'src/credentials/authorization_challenge_parser.cpp',
  'src/cryptography/md5.cpp',
  'src/cryptography/sha_hash.cpp',
  'src/datetime.cpp',
  'src/environment.cpp',
  'src/environment_log_level_listener.cpp',
  'src/etag.cpp',
  'src/exception.cpp',
  'src/http/bearer_token_authentication_policy.cpp',
  'src/http/http.cpp',
  'src/http/http_sanitizer.cpp',
  'src/http/log_policy.cpp',
  'src/http/policy.cpp',
  'src/http/raw_response.cpp',
  'src/http/request.cpp',
  'src/http/request_activity_policy.cpp',
  'src/http/retry_policy.cpp',
  'src/http/telemetry_policy.cpp',
  'src/http/transport_policy.cpp',
  'src/http/url.cpp',
  'src/http/user_agent.cpp',
  'src/io/body_stream.cpp',
  'src/io/random_access_file_body_stream.cpp',
  'src/logger.cpp',
  'src/operation_status.cpp',
  'src/private/environment_log_level_listener.hpp',
  'src/private/package_version.hpp',
  'src/tracing/tracing.cpp',
  'src/uuid.cpp',
]

azure_core_args = []
if get_option('default_library') != 'static'
  azure_core_args += ['-DAZ_CORE_DLL']
endif

azure_core_lib = library(
  'azure-core',
  sources: azure_core_header_files + azure_core_sources,
  include_directories: incdir,
  dependencies: azure_crypto_dep,
  cpp_args: ['-DAZ_CORE_BEING_BUILT'] + azure_core_args,
)

threads_dep = dependency('threads')

azure_core_dep = declare_dependency(
  link_with: azure_core_lib,
  include_directories: incdir,
  dependencies: [threads_dep],
  compile_args: azure_core_args,
)
