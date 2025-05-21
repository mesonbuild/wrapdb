project(
  'azure-sdk-for-cpp',
  'cpp',
  version: '1.9.0',
  default_options: ['cpp_std=c++14'],
)

if host_machine.system() == 'windows'
  cc = meson.get_compiler('cpp')
  bcrypt_dep = cc.find_library('bcrypt')
  azure_crypto_dep = bcrypt_dep
else
  openssl_dep = dependency('openssl')
  azure_crypto_dep = openssl_dep
endif

subdir('sdk/core')
subdir('sdk/identity')
subdir('sdk/storage')
