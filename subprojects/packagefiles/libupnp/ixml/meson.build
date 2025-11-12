headers = files('inc/ixml.h', 'inc/ixmldebug.h')

libixml = static_library(
  'ixml',
  'src/attr.c',
  'src/document.c',
  'src/element.c',
  'src/ixml.c',
  'src/ixmldebug.c',
  'src/ixmlmembuf.c',
  'src/ixmlparser.c',
  'src/namedNodeMap.c',
  'src/node.c',
  'src/nodeList.c',
  include_directories: ['src/inc', libupnp_incdir],
  override_options: cstd,
  pic: true,
)


