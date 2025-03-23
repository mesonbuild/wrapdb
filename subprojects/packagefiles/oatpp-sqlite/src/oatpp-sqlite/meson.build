header_files = files(
  'Connection.hpp',
  'ConnectionProvider.hpp',
  'Executor.hpp',
  'QueryResult.hpp',
  'Types.hpp',
  'Utils.hpp',
  'mapping/Deserializer.hpp',
  'mapping/ResultMapper.hpp',
  'mapping/Serializer.hpp',
  'mapping/type/Blob.hpp',
  'orm.hpp',
  'ql_template/Parser.hpp',
  'ql_template/TemplateValueProvider.hpp',
)

src_files += header_files

src_files += files(
  'Connection.cpp',
  'ConnectionProvider.cpp',
  'Executor.cpp',
  'QueryResult.cpp',
  'Utils.cpp',
  'mapping/Deserializer.cpp',
  'mapping/ResultMapper.cpp',
  'mapping/Serializer.cpp',
  'mapping/type/Blob.cpp',
  'ql_template/Parser.cpp',
  'ql_template/TemplateValueProvider.cpp',
)

install_headers(
  header_files,
  subdir: 'oatpp-sqlite',
)
