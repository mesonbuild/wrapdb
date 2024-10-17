header_files = files(
  'algorithm/CRC.hpp',
  'codegen/ApiClient_define.hpp',
  'codegen/ApiClient_undef.hpp',
  'codegen/ApiController_define.hpp',
  'codegen/ApiController_undef.hpp',
  'codegen/DTO_define.hpp',
  'codegen/DTO_undef.hpp',
  'codegen/DbClient_define.hpp',
  'codegen/DbClient_undef.hpp',
  'codegen/api_controller/auth_define.hpp',
  'codegen/api_controller/auth_undef.hpp',
  'codegen/api_controller/base_define.hpp',
  'codegen/api_controller/base_undef.hpp',
  'codegen/api_controller/bundle_define.hpp',
  'codegen/api_controller/bundle_undef.hpp',
  'codegen/api_controller/cors_define.hpp',
  'codegen/api_controller/cors_undef.hpp',
  'codegen/dto/base_define.hpp',
  'codegen/dto/base_undef.hpp',
  'codegen/dto/enum_define.hpp',
  'codegen/dto/enum_undef.hpp',
  'core/IODefinitions.hpp',
  'core/Types.hpp',
  'core/async/ConditionVariable.hpp',
  'core/async/Coroutine.hpp',
  'core/async/CoroutineWaitList.hpp',
  'core/async/Error.hpp',
  'core/async/Executor.hpp',
  'core/async/Lock.hpp',
  'core/async/Processor.hpp',
  'core/async/utils/FastQueue.hpp',
  'core/async/worker/IOEventWorker.hpp',
  'core/async/worker/IOWorker.hpp',
  'core/async/worker/TimerWorker.hpp',
  'core/async/worker/Worker.hpp',
  'core/base/CommandLineArguments.hpp',
  'core/base/Config.hpp',
  'core/base/Countable.hpp',
  'core/base/Environment.hpp',
  'core/base/ObjectHandle.hpp',
  'core/concurrency/SpinLock.hpp',
  'core/concurrency/Thread.hpp',
  'core/data/Bundle.hpp',
  'core/data/buffer/FIFOBuffer.hpp',
  'core/data/buffer/IOBuffer.hpp',
  'core/data/buffer/Processor.hpp',
  'core/data/mapping/ObjectMapper.hpp',
  'core/data/mapping/TypeResolver.hpp',
  'core/data/mapping/type/Any.hpp',
  'core/data/mapping/type/Collection.hpp',
  'core/data/mapping/type/Enum.hpp',
  'core/data/mapping/type/List.hpp',
  'core/data/mapping/type/Map.hpp',
  'core/data/mapping/type/Object.hpp',
  'core/data/mapping/type/PairList.hpp',
  'core/data/mapping/type/Primitive.hpp',
  'core/data/mapping/type/Type.hpp',
  'core/data/mapping/type/UnorderedMap.hpp',
  'core/data/mapping/type/UnorderedSet.hpp',
  'core/data/mapping/type/Vector.hpp',
  'core/data/resource/File.hpp',
  'core/data/resource/InMemoryData.hpp',
  'core/data/resource/Resource.hpp',
  'core/data/resource/TemporaryFile.hpp',
  'core/data/share/LazyStringMap.hpp',
  'core/data/share/MemoryLabel.hpp',
  'core/data/share/StringTemplate.hpp',
  'core/data/stream/BufferStream.hpp',
  'core/data/stream/FIFOStream.hpp',
  'core/data/stream/FileStream.hpp',
  'core/data/stream/Stream.hpp',
  'core/data/stream/StreamBufferedProxy.hpp',
  'core/macro/basic.hpp',
  'core/macro/codegen.hpp',
  'core/macro/component.hpp',
  'core/parser/Caret.hpp',
  'core/parser/ParsingError.hpp',
  'core/provider/Invalidator.hpp',
  'core/provider/Pool.hpp',
  'core/provider/Provider.hpp',
  'core/utils/Binary.hpp',
  'core/utils/ConversionUtils.hpp',
  'core/utils/Random.hpp',
  'core/utils/String.hpp',
  'encoding/Base64.hpp',
  'encoding/Hex.hpp',
  'encoding/Unicode.hpp',
  'encoding/Url.hpp',
  'network/Address.hpp',
  'network/ConnectionHandler.hpp',
  'network/ConnectionPool.hpp',
  'network/ConnectionProvider.hpp',
  'network/ConnectionProviderSwitch.hpp',
  'network/Server.hpp',
  'network/Url.hpp',
  'network/monitor/ConnectionInactivityChecker.hpp',
  'network/monitor/ConnectionMaxAgeChecker.hpp',
  'network/monitor/ConnectionMonitor.hpp',
  'network/monitor/MetricsChecker.hpp',
  'network/monitor/StatCollector.hpp',
  'network/tcp/Connection.hpp',
  'network/tcp/ConnectionConfigurer.hpp',
  'network/tcp/client/ConnectionProvider.hpp',
  'network/tcp/server/ConnectionProvider.hpp',
  'network/virtual_/Interface.hpp',
  'network/virtual_/Pipe.hpp',
  'network/virtual_/Socket.hpp',
  'network/virtual_/client/ConnectionProvider.hpp',
  'network/virtual_/server/ConnectionProvider.hpp',
  'orm/Connection.hpp',
  'orm/DbClient.hpp',
  'orm/Executor.hpp',
  'orm/QueryResult.hpp',
  'orm/SchemaMigration.hpp',
  'orm/Transaction.hpp',
  'parser/json/Beautifier.hpp',
  'parser/json/Utils.hpp',
  'parser/json/mapping/Deserializer.hpp',
  'parser/json/mapping/ObjectMapper.hpp',
  'parser/json/mapping/Serializer.hpp',
  'web/client/ApiClient.hpp',
  'web/client/HttpRequestExecutor.hpp',
  'web/client/RequestExecutor.hpp',
  'web/client/RetryPolicy.hpp',
  'web/mime/multipart/FileProvider.hpp',
  'web/mime/multipart/InMemoryDataProvider.hpp',
  'web/mime/multipart/Multipart.hpp',
  'web/mime/multipart/Part.hpp',
  'web/mime/multipart/PartList.hpp',
  'web/mime/multipart/PartReader.hpp',
  'web/mime/multipart/Reader.hpp',
  'web/mime/multipart/StatefulParser.hpp',
  'web/mime/multipart/TemporaryFileProvider.hpp',
  'web/protocol/CommunicationError.hpp',
  'web/protocol/http/Http.hpp',
  'web/protocol/http/encoding/Chunked.hpp',
  'web/protocol/http/encoding/EncoderProvider.hpp',
  'web/protocol/http/encoding/ProviderCollection.hpp',
  'web/protocol/http/incoming/BodyDecoder.hpp',
  'web/protocol/http/incoming/Request.hpp',
  'web/protocol/http/incoming/RequestHeadersReader.hpp',
  'web/protocol/http/incoming/Response.hpp',
  'web/protocol/http/incoming/ResponseHeadersReader.hpp',
  'web/protocol/http/incoming/SimpleBodyDecoder.hpp',
  'web/protocol/http/outgoing/Body.hpp',
  'web/protocol/http/outgoing/BufferBody.hpp',
  'web/protocol/http/outgoing/MultipartBody.hpp',
  'web/protocol/http/outgoing/Request.hpp',
  'web/protocol/http/outgoing/Response.hpp',
  'web/protocol/http/outgoing/ResponseFactory.hpp',
  'web/protocol/http/outgoing/StreamingBody.hpp',
  'web/protocol/http/utils/CommunicationUtils.hpp',
  'web/server/AsyncHttpConnectionHandler.hpp',
  'web/server/HttpConnectionHandler.hpp',
  'web/server/HttpProcessor.hpp',
  'web/server/HttpRequestHandler.hpp',
  'web/server/HttpRouter.hpp',
  'web/server/api/ApiController.hpp',
  'web/server/api/Endpoint.hpp',
  'web/server/handler/AuthorizationHandler.hpp',
  'web/server/handler/ErrorHandler.hpp',
  'web/server/interceptor/AllowCorsGlobal.hpp',
  'web/server/interceptor/RequestInterceptor.hpp',
  'web/server/interceptor/ResponseInterceptor.hpp',
  'web/url/mapping/Pattern.hpp',
  'web/url/mapping/Router.hpp',





























































































































)

src_files += header_files

src_files += files(
  'algorithm/CRC.cpp',
  'core/IODefinitions.cpp',
  'core/async/ConditionVariable.cpp',
  'core/async/Coroutine.cpp',
  'core/async/CoroutineWaitList.cpp',
  'core/async/Error.cpp',
  'core/async/Executor.cpp',
  'core/async/Lock.cpp',
  'core/async/Processor.cpp',
  'core/async/worker/IOEventWorker_common.cpp',
  'core/async/worker/IOEventWorker_epoll.cpp',
  'core/async/worker/IOEventWorker_kqueue.cpp',
  'core/async/worker/IOEventWorker_stub.cpp',
  'core/async/worker/IOWorker.cpp',
  'core/async/worker/TimerWorker.cpp',
  'core/async/worker/Worker.cpp',
  'core/base/CommandLineArguments.cpp',
  'core/base/Countable.cpp',
  'core/base/Environment.cpp',
  'core/concurrency/SpinLock.cpp',
  'core/concurrency/Thread.cpp',
  'core/data/Bundle.cpp',
  'core/data/buffer/FIFOBuffer.cpp',
  'core/data/buffer/IOBuffer.cpp',
  'core/data/buffer/Processor.cpp',
  'core/data/mapping/ObjectMapper.cpp',
  'core/data/mapping/TypeResolver.cpp',
  'core/data/mapping/type/Any.cpp',
  'core/data/mapping/type/Enum.cpp',
  'core/data/mapping/type/List.cpp',
  'core/data/mapping/type/Object.cpp',
  'core/data/mapping/type/PairList.cpp',
  'core/data/mapping/type/Primitive.cpp',
  'core/data/mapping/type/Type.cpp',
  'core/data/mapping/type/UnorderedMap.cpp',
  'core/data/mapping/type/UnorderedSet.cpp',
  'core/data/mapping/type/Vector.cpp',
  'core/data/resource/File.cpp',
  'core/data/resource/InMemoryData.cpp',
  'core/data/resource/TemporaryFile.cpp',
  'core/data/share/MemoryLabel.cpp',
  'core/data/share/StringTemplate.cpp',
  'core/data/stream/BufferStream.cpp',
  'core/data/stream/FIFOStream.cpp',
  'core/data/stream/FileStream.cpp',
  'core/data/stream/Stream.cpp',
  'core/data/stream/StreamBufferedProxy.cpp',
  'core/parser/Caret.cpp',
  'core/parser/ParsingError.cpp',
  'core/utils/Binary.cpp',
  'core/utils/ConversionUtils.cpp',
  'core/utils/Random.cpp',
  'core/utils/String.cpp',
  'encoding/Base64.cpp',
  'encoding/Hex.cpp',
  'encoding/Unicode.cpp',
  'encoding/Url.cpp',
  'network/Address.cpp',
  'network/ConnectionPool.cpp',
  'network/ConnectionProvider.cpp',
  'network/ConnectionProviderSwitch.cpp',
  'network/Server.cpp',
  'network/Url.cpp',
  'network/monitor/ConnectionInactivityChecker.cpp',
  'network/monitor/ConnectionMaxAgeChecker.cpp',
  'network/monitor/ConnectionMonitor.cpp',
  'network/tcp/Connection.cpp',
  'network/tcp/client/ConnectionProvider.cpp',
  'network/tcp/server/ConnectionProvider.cpp',
  'network/virtual_/Interface.cpp',
  'network/virtual_/Pipe.cpp',
  'network/virtual_/Socket.cpp',
  'network/virtual_/client/ConnectionProvider.cpp',
  'network/virtual_/server/ConnectionProvider.cpp',
  'orm/DbClient.cpp',
  'orm/Executor.cpp',
  'orm/QueryResult.cpp',
  'orm/SchemaMigration.cpp',
  'orm/Transaction.cpp',
  'parser/json/Beautifier.cpp',
  'parser/json/Utils.cpp',
  'parser/json/mapping/Deserializer.cpp',
  'parser/json/mapping/ObjectMapper.cpp',
  'parser/json/mapping/Serializer.cpp',
  'web/client/ApiClient.cpp',
  'web/client/HttpRequestExecutor.cpp',
  'web/client/RequestExecutor.cpp',
  'web/client/RetryPolicy.cpp',
  'web/mime/multipart/FileProvider.cpp',
  'web/mime/multipart/InMemoryDataProvider.cpp',
  'web/mime/multipart/Multipart.cpp',
  'web/mime/multipart/Part.cpp',
  'web/mime/multipart/PartList.cpp',
  'web/mime/multipart/PartReader.cpp',
  'web/mime/multipart/Reader.cpp',
  'web/mime/multipart/StatefulParser.cpp',
  'web/mime/multipart/TemporaryFileProvider.cpp',
  'web/protocol/CommunicationError.cpp',
  'web/protocol/http/Http.cpp',
  'web/protocol/http/encoding/Chunked.cpp',
  'web/protocol/http/encoding/ProviderCollection.cpp',
  'web/protocol/http/incoming/BodyDecoder.cpp',
  'web/protocol/http/incoming/Request.cpp',
  'web/protocol/http/incoming/RequestHeadersReader.cpp',
  'web/protocol/http/incoming/Response.cpp',
  'web/protocol/http/incoming/ResponseHeadersReader.cpp',
  'web/protocol/http/incoming/SimpleBodyDecoder.cpp',
  'web/protocol/http/outgoing/Body.cpp',
  'web/protocol/http/outgoing/BufferBody.cpp',
  'web/protocol/http/outgoing/MultipartBody.cpp',
  'web/protocol/http/outgoing/Request.cpp',
  'web/protocol/http/outgoing/Response.cpp',
  'web/protocol/http/outgoing/ResponseFactory.cpp',
  'web/protocol/http/outgoing/StreamingBody.cpp',
  'web/protocol/http/utils/CommunicationUtils.cpp',
  'web/server/AsyncHttpConnectionHandler.cpp',
  'web/server/HttpConnectionHandler.cpp',
  'web/server/HttpProcessor.cpp',
  'web/server/HttpRouter.cpp',
  'web/server/api/ApiController.cpp',
  'web/server/api/Endpoint.cpp',
  'web/server/handler/AuthorizationHandler.cpp',
  'web/server/handler/ErrorHandler.cpp',
  'web/server/interceptor/AllowCorsGlobal.cpp',
  'web/url/mapping/Pattern.cpp',






































































































































































)

install_headers(header_files, subdir: 'oatpp')
