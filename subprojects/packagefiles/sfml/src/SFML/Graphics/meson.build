graphics_sources = files(
  'BlendMode.cpp',
  'Font.cpp',
  'GLCheck.cpp',
  'GLExtensions.cpp',
  'Glsl.cpp',
  'Image.cpp',
  'RenderStates.cpp',
  'RenderTarget.cpp',
  'RenderTexture.cpp',
  'RenderWindow.cpp',
  'Shader.cpp',
  'StencilMode.cpp',
  'Texture.cpp',
  'TextureSaver.cpp',
  'Transform.cpp',
  'Transformable.cpp',
  'View.cpp',
)

graphics_sources += files(
  'CircleShape.cpp',
  'ConvexShape.cpp',
  'RectangleShape.cpp',
  'Shape.cpp',
  'Sprite.cpp',
  'Text.cpp',
  'VertexArray.cpp',
  'VertexBuffer.cpp',
)

graphics_sources += files(
  'RenderTexture.cpp',
  'RenderTextureImplDefault.cpp',
  'RenderTextureImplFBO.cpp',
)

graphics_args = []

graphics_args += get_option('default_library') != 'static' ? '-DSFML_GRAPHICS_EXPORTS' : '-DSFML_STATIC'

freetype_dep = dependency('freetype2', version: '>=2.14.3')
harfbuzz_dep = dependency(
  'harfbuzz',
  #version: '>=14.1.0',
  default_options: [
    'subset=disabled', #font subsetting and instancing library
    'raster=disabled', #glyph rasterization library
    'vector=disabled', #glyph vector drawing library
    'gpu=disabled', #GPU rasterization library
  ],
)

#harfbuzz
graphics_args += [
  '-DHB_DISABLE_DEPRECATED',
  '-DHB_NO_ATEXIT',
  '-DHB_NO_BORING_EXPANSION',
  '-DHB_NO_BUFFER_MESSAGE',
  '-DHB_NO_BUFFER_SERIALIZE',
  '-DHB_NO_BUFFER_VERIFY',
  '-DHB_NO_BITMAP',
  '-DHB_NO_DRAW',
  '-DHB_NO_ERRNO',
  '-DHB_NO_GETENV',
  '-DHB_NO_MT',
  '-DHB_NO_PAINT',
  '-DHB_NO_SETLOCALE',
  '-DHB_OPTIMIZE_SIZE',
]

sheenbidi_dep = dependency('sheenbidi')

graphics_lib = library(
  'sfml-graphics',
  graphics_sources,
  cpp_args: graphics_args,
  include_directories: [glad_inc, pub_inc, priv_inc, stb_inc, qoi_inc],
  link_with: [window_lib, system_lib],
  dependencies: [gl_dep, freetype_dep, harfbuzz_dep, sheenbidi_dep],
  override_options: override_opts,
  install: true,
)
