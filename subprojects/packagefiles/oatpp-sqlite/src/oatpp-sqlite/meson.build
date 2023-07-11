header_files = files(
    'mapping/Deserializer.hpp',
    'mapping/ResultMapper.hpp',
    'mapping/Serializer.hpp',
    'mapping/type/Blob.hpp',
    'ql_template/Parser.hpp',
    'ql_template/TemplateValueProvider.hpp',
    'Connection.hpp',
    'ConnectionProvider.hpp',
    'Executor.hpp',
    'QueryResult.hpp',
    'Types.hpp',
    'Utils.hpp',
    'orm.hpp',
)

src_files += header_files

src_files += files(
    'mapping/Deserializer.cpp',
    'mapping/ResultMapper.cpp',
    'mapping/Serializer.cpp',
    'mapping/type/Blob.cpp',
    'ql_template/Parser.cpp',
    'ql_template/TemplateValueProvider.cpp',
    'Connection.cpp',
    'ConnectionProvider.cpp',
    'Executor.cpp',
    'QueryResult.cpp',
    'Utils.cpp',
)

install_headers(header_files, subdir: 'oatpp-sqlite')
