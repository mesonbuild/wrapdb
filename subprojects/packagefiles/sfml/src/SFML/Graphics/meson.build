graphics_sources = files(
    'BlendMode.cpp',
    'Color.cpp',
    'Font.cpp',
    'Glsl.cpp',
    'GLCheck.cpp',
    'GLExtensions.cpp',
    'Image.cpp',
    'ImageLoader.cpp',
    'RenderStates.cpp',
    'RenderTexture.cpp',
    'RenderTarget.cpp',
    'RenderWindow.cpp',
    'Shader.cpp',
    'Texture.cpp',
    'TextureSaver.cpp',
    'Transform.cpp',
    'Transformable.cpp',
    'View.cpp',
    'Vertex.cpp',
)

# GLES not supported yet, so add always.
graphics_sources += files('GLLoader.cpp')

graphics_sources += files(
    'Shape.cpp',
    'CircleShape.cpp',
    'RectangleShape.cpp',
    'ConvexShape.cpp',
    'Sprite.cpp',
    'Text.cpp',
    'VertexArray.cpp',
    'VertexBuffer.cpp',
)

graphics_sources += files(
    'RenderTextureImpl.cpp',
    'RenderTextureImplFBO.cpp',
    'RenderTextureImplDefault.cpp',
)

graphics_lib = library('sfml-graphics',
    graphics_sources,
    cpp_args: get_option('default_library') == 'shared' ? ['-DSFML_GRAPHICS_EXPORTS'] : ['-DSFML_STATIC'],
    include_directories: [pub_inc, priv_inc, stb_inc],
    link_with: [window_lib, system_lib],
    dependencies: [gl_dep, freetype_dep],
)
