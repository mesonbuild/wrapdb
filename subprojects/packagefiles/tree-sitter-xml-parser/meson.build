project('tree-sitter-xml-parser', 'c')

tree_sitter_xml_parser = static_library('tree-sitter-xml-parser', [
    'src/parser.c',
  ],
  dependencies: tree_sitter_dep,
)

tree_sitter_xml_dep = declare_dependency(
  link_with: tree_sitter_xml_parser,
)
