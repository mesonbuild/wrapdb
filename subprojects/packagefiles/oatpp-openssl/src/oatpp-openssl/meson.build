header_files = files(
  'Config.hpp',
  'Connection.hpp',
  'client/ConnectionProvider.hpp',
  'configurer/CertificateChainFile.hpp',
  'configurer/CertificateFile.hpp',
  'configurer/ContextConfigurer.hpp',
  'configurer/PrivateKeyFile.hpp',
  'server/ConnectionProvider.hpp',
)

src_files += header_files

src_files += files(
  'Config.cpp',
  'Connection.cpp',
  'client/ConnectionProvider.cpp',
  'configurer/CertificateChainFile.cpp',
  'configurer/CertificateFile.cpp',
  'configurer/PrivateKeyFile.cpp',
  'server/ConnectionProvider.cpp',
)

install_headers(
  header_files,
  subdir: 'oatpp-openssl',
)
