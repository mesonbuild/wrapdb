header_files = files(
  'AsyncConnectionHandler.hpp',
  'AsyncWebSocket.hpp',
  'Config.hpp',
  'ConnectionHandler.hpp',
  'Connector.hpp',
  'Frame.hpp',
  'Handshaker.hpp',
  'SHA1.hpp',
  'Utils.hpp',
  'WebSocket.hpp',
)

src_files += header_files

src_files += files(
  'AsyncConnectionHandler.cpp',
  'AsyncWebSocket.cpp',
  'ConnectionHandler.cpp',
  'Connector.cpp',
  'Frame.cpp',
  'Handshaker.cpp',
  'SHA1.cpp',
  'Utils.cpp',
  'WebSocket.cpp',
)


install_headers(
  header_files,
  subdir: 'oatpp-websocket',
)
