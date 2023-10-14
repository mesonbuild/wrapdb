header_files = files(
    'client/ConnectionProvider.hpp',
    'server/ConnectionProvider.hpp',
    'Callbacks.hpp',
    'Config.hpp',
    'Connection.hpp',
    'TLSObject.hpp',
)

src_files += header_files

src_files += files(
    'client/ConnectionProvider.cpp',
    'server/ConnectionProvider.cpp',
    'Callbacks.cpp',
    'Config.cpp',
    'Connection.cpp',
    'TLSObject.cpp',
)

install_headers(header_files, subdir: 'oatpp-libressl')
