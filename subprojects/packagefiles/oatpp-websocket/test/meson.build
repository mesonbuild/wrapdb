test_src_files = files(
  'oatpp-websocket/FullAsyncTest.cpp',
  'oatpp-websocket/FullAsyncTest.hpp',
  'oatpp-websocket/FullTest.cpp',
  'oatpp-websocket/FullTest.hpp',
  'oatpp-websocket/app/AsyncController.hpp',
  'oatpp-websocket/app/AsyncWebSocketListener.hpp',
  'oatpp-websocket/app/Controller.hpp',
  'oatpp-websocket/app/WebSocketListener.hpp',
  'oatpp-websocket/tests.cpp',
)

test_deps = deps
test_deps += dependency(
  'oatpp-test',
  version: '1.3.0',
)
test_deps += oatpp_websocket_dep

test_inc_dirs = inc_dirs
test_inc_dirs += include_directories('.')

websocket_tests = executable(
  'oatpp_websocket_tests',
  test_src_files,
  include_directories: test_inc_dirs,
  dependencies: test_deps,
)

test('oatpp websocket module tests', websocket_tests)
