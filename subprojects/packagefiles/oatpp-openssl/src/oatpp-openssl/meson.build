header_files = files(
    'client/ConnectionProvider.hpp',
    'configurer/CertificateChainFile.hpp',
    'configurer/CertificateFile.hpp',
    'configurer/ContextConfigurer.hpp',
    'configurer/PrivateKeyFile.hpp',
    'server/ConnectionProvider.hpp',
    'Config.hpp',
    'Connection.hpp',
)

src_files += header_files

src_files += files(
    'client/ConnectionProvider.cpp',
    'configurer/CertificateChainFile.cpp',
    'configurer/CertificateFile.cpp',
    'configurer/PrivateKeyFile.cpp',
    'server/ConnectionProvider.cpp',
    'Config.cpp',
    'Connection.cpp',
)

install_headers(header_files, subdir: 'oatpp-openssl')
