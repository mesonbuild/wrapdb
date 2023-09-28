graphics_sources = files(
  'BlendMode.cpp',
  'Color.cpp',
  'Font.cpp',
  'GLCheck.cpp',
  'GLExtensions.cpp',
  'Glsl.cpp',
  'Image.cpp',
  'ImageLoader.cpp',
  'RenderStates.cpp',
  'RenderTarget.cpp',
  'RenderTexture.cpp',
  'RenderWindow.cpp',
  'Shader.cpp',
  'Texture.cpp',
  'TextureSaver.cpp',
  'Transform.cpp',
  'Transformable.cpp',
  'Vertex.cpp',
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
  'RenderTextureImpl.cpp',
  'RenderTextureImplDefault.cpp',
  'RenderTextureImplFBO.cpp',
)

graphics_lib = library(
  'sfml-graphics',
  graphics_sources,
  cpp_args: get_option('default_library') != 'static' ? '-DSFML_GRAPHICS_EXPORTS' : '-DSFML_STATIC',
  include_directories: [glad_inc, pub_inc, priv_inc, stb_inc],
  link_with: [window_lib, system_lib],
  dependencies: [gl_dep, freetype_dep],
)
