if not get_option('examples')
  subdir_done()
endif

executable(
  'helloworld',
  'helloworld.cpp',
  dependencies: crow_dep,
  override_options: crow_private_options,
  cpp_args: crow_private_args,
)

if zlib_dep.found()
  executable(
    'example_compression',
    'example_compression.cpp',
    dependencies: crow_dep,
    override_options: crow_private_options,
    cpp_args: crow_private_args,
  )
endif

if openssl_dep.found()
  executable(
    'example_ssl',
    'ssl/example_ssl.cpp',
    dependencies: crow_dep,
    override_options: crow_private_options,
    cpp_args: crow_private_args,
  )
endif

executable(
  'example_websocket',
  'websocket/example_ws.cpp',
  dependencies: crow_dep,
  override_options: crow_private_options,
  cpp_args: crow_private_args,
)
# TODO: meson does not support writing file into subdir
# configure_file(copy: true, input: 'websocket/templates/ws.html', output: 'templates/ws.html')

executable(
  'basic_example',
  'example.cpp',
  dependencies: crow_dep,
  override_options: crow_private_options,
  cpp_args: crow_private_args,
)

executable(
  'example_chat',
  'example_chat.cpp',
  dependencies: crow_dep,
  override_options: crow_private_options,
  cpp_args: crow_private_args,
)
# TODO: meson does not support writing file into subdir
# configure_file(copy: true, input: 'example_chat.html', output: 'templates/example_chat.html')

executable(
  'example_static_file',
  'example_static_file.cpp',
  dependencies: crow_dep,
  override_options: crow_private_options,
  cpp_args: crow_private_args,
)

executable(
  'example_catchall',
  'example_catchall.cpp',
  dependencies: crow_dep,
  override_options: crow_private_options,
  cpp_args: crow_private_args,
)

executable(
  'example_json_map',
  'example_json_map.cpp',
  dependencies: crow_dep,
  override_options: crow_private_options,
  cpp_args: crow_private_args,
)

executable(
  'example_blueprint',
  'example_blueprint.cpp',
  dependencies: crow_dep,
  override_options: crow_private_options,
  cpp_args: crow_private_args,
)

executable(
  'example_middleware',
  'example_middleware.cpp',
  dependencies: crow_dep,
  override_options: crow_private_options,
  cpp_args: crow_private_args,
)

executable(
  'example_cors',
  'middlewares/example_cors.cpp',
  dependencies: crow_dep,
  override_options: crow_private_options,
  cpp_args: crow_private_args,
)

executable(
  'example_cookies',
  'middlewares/example_cookies.cpp',
  dependencies: crow_dep,
  override_options: crow_private_options,
  cpp_args: crow_private_args,
)

executable(
  'example_session',
  'middlewares/example_session.cpp',
  dependencies: crow_dep,
  override_options: crow_private_options,
  cpp_args: crow_private_args,
)

executable(
  'example_file_upload',
  'example_file_upload.cpp',
  dependencies: crow_dep,
  override_options: crow_private_options,
  cpp_args: crow_private_args,
)

executable(
  'example_unix_socket',
  'example_unix_socket.cpp',
  dependencies: crow_dep,
  override_options: crow_private_options,
  cpp_args: crow_private_args,
)

if meson.get_compiler('cpp').get_argument_syntax() == 'msvc'
  executable(
    'example_vs',
    'example_vs.cpp',
    dependencies: crow_dep,
    override_options: crow_private_options,
    cpp_args: crow_private_args,
  )
endif
