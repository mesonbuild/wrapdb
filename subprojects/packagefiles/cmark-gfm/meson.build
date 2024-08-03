project(
    'cmark-gfm',
    'c',
    version: '0.29.0.gfm.13',
    default_options: ['warning_level=3'],
    meson_version: '>=0.49.0',
    license: 'BSD-2-Clause',
)

cc = meson.get_compiler('c')
has_stdbool_header = cc.has_header('stdbool.h')
has_builtin_expect_code = 'int main() { __builtin_expect(0,0); return 0; }'
has_builtin_expect = cc.links(
    has_builtin_expect_code,
    name: 'has __builtin_expect',
)
has_attribute_code = '''
  int f(void) __attribute__ (());
  int main() { return 0; }
'''
has_attribute = cc.compiles(has_attribute_code, name: 'has __attribute__')

cdata = configuration_data(
    {
        'HAVE_STDBOOL_H': has_stdbool_header,
        'HAVE___BUILTIN_EXPECT': has_builtin_expect,
        'HAVE___ATTRIBUTE__': has_attribute,
    },
)

configure_file(
    format: 'cmake@',
    input: 'src/config.h.in',
    output: 'config.h',
    configuration: cdata,
)

varr = meson.project_version().split('.')
vdata = configuration_data(
    {
        'PROJECT_VERSION_MAJOR': varr[0],
        'PROJECT_VERSION_MINOR': varr[1],
        'PROJECT_VERSION_PATCH': varr[2],
        'PROJECT_VERSION_GFM': varr[4],
    },
)

configure_file(
    format: 'cmake@',
    input: 'src/cmark-gfm_version.h.in',
    output: 'cmark-gfm_version.h',
    configuration: vdata,
)

edata = configuration_data(
    {
        'CMARK_GFM_STATIC_DEFINE': get_option('default_library') == 'static' ? 1 : 0,
    },
)

configure_file(
    input: 'cmark-gfm_export.h.meson',
    output: 'cmark-gfm_export.h',
    configuration: edata,
)

configure_file(
    input: 'cmark-gfm-extensions_export.h.meson',
    output: 'cmark-gfm-extensions_export.h',
    configuration: edata,
)

# Required to avoid linker warnings on Windows.
add_project_arguments('-Dlibcmark_gfm_EXPORTS', language: 'c')

cmark_gfm_src = files(
    'src/arena.c',
    'src/blocks.c',
    'src/buffer.c',
    'src/cmark.c',
    'src/cmark_ctype.c',
    'src/commonmark.c',
    'src/footnotes.c',
    'src/houdini_href_e.c',
    'src/houdini_html_e.c',
    'src/houdini_html_u.c',
    'src/html.c',
    'src/inlines.c',
    'src/iterator.c',
    'src/latex.c',
    'src/linked_list.c',
    'src/man.c',
    'src/map.c',
    'src/node.c',
    'src/plaintext.c',
    'src/plugin.c',
    'src/references.c',
    'src/registry.c',
    'src/render.c',
    'src/scanners.c',
    'src/syntax_extension.c',
    'src/utf8.c',
    'src/xml.c',
)

cmark_gfm_extensions_src = files(
    'extensions/autolink.c',
    'extensions/core-extensions.c',
    'extensions/ext_scanners.c',
    'extensions/ext_scanners.h',
    'extensions/strikethrough.c',
    'extensions/table.c',
    'extensions/tagfilter.c',
    'extensions/tasklist.c',
)

# cmark-gfm has many unused parameter warnings, so we disable that warning
# on compilers that support it.
add_project_arguments(
    cc.get_supported_arguments('-Wno-unused-parameter'),
    language: 'c',
)

includes = include_directories('.', 'src', 'extensions')
cmark_gfm_lib = library(
    'cmark-gfm',
    cmark_gfm_src,
    include_directories: includes,
)

cmark_gfm_extensions_lib = library(
    'cmark-gfm-extensions',
    cmark_gfm_extensions_src,
    include_directories: includes,
    link_with: cmark_gfm_lib,
)

cmark_gfm_dep = declare_dependency(
    link_with: [cmark_gfm_lib, cmark_gfm_extensions_lib],
    include_directories: includes,
)
