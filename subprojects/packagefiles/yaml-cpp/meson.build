project(
  'yaml-cpp',
  'cpp',
  version: '0.8.0',
  default_options: ['cpp_std=c++11'],
  meson_version: '>=0.63.0',
  license: 'MIT',
)

inc = include_directories('include')

yaml_cpp_headers = files(
  'include/yaml-cpp/anchor.h',
  'include/yaml-cpp/binary.h',
  'include/yaml-cpp/contrib/anchordict.h',
  'include/yaml-cpp/contrib/graphbuilder.h',
  'include/yaml-cpp/depthguard.h',
  'include/yaml-cpp/dll.h',
  'include/yaml-cpp/emitfromevents.h',
  'include/yaml-cpp/emitter.h',
  'include/yaml-cpp/emitterdef.h',
  'include/yaml-cpp/emittermanip.h',
  'include/yaml-cpp/emitterstyle.h',
  'include/yaml-cpp/eventhandler.h',
  'include/yaml-cpp/exceptions.h',
  'include/yaml-cpp/mark.h',
  'include/yaml-cpp/node/convert.h',
  'include/yaml-cpp/node/detail/impl.h',
  'include/yaml-cpp/node/detail/iterator.h',
  'include/yaml-cpp/node/detail/iterator_fwd.h',
  'include/yaml-cpp/node/detail/memory.h',
  'include/yaml-cpp/node/detail/node.h',
  'include/yaml-cpp/node/detail/node_data.h',
  'include/yaml-cpp/node/detail/node_iterator.h',
  'include/yaml-cpp/node/detail/node_ref.h',
  'include/yaml-cpp/node/emit.h',
  'include/yaml-cpp/node/impl.h',
  'include/yaml-cpp/node/iterator.h',
  'include/yaml-cpp/node/node.h',
  'include/yaml-cpp/node/parse.h',
  'include/yaml-cpp/node/ptr.h',
  'include/yaml-cpp/node/type.h',
  'include/yaml-cpp/noexcept.h',
  'include/yaml-cpp/null.h',
  'include/yaml-cpp/ostream_wrapper.h',
  'include/yaml-cpp/parser.h',
  'include/yaml-cpp/stlemitter.h',
  'include/yaml-cpp/traits.h',
  'include/yaml-cpp/yaml.h',
)

yaml_cpp_sources = files(
  'src/binary.cpp',
  'src/convert.cpp',
  'src/depthguard.cpp',
  'src/directives.cpp',
  'src/emit.cpp',
  'src/emitfromevents.cpp',
  'src/emitter.cpp',
  'src/emitterstate.cpp',
  'src/emitterutils.cpp',
  'src/exceptions.cpp',
  'src/exp.cpp',
  'src/memory.cpp',
  'src/node.cpp',
  'src/node_data.cpp',
  'src/nodebuilder.cpp',
  'src/nodeevents.cpp',
  'src/null.cpp',
  'src/ostream_wrapper.cpp',
  'src/parse.cpp',
  'src/parser.cpp',
  'src/regex_yaml.cpp',
  'src/scanner.cpp',
  'src/scanscalar.cpp',
  'src/scantag.cpp',
  'src/scantoken.cpp',
  'src/simplekey.cpp',
  'src/singledocparser.cpp',
  'src/stream.cpp',
  'src/tag.cpp',
)

yaml_cpp_contrib_sources = files(
  'src/contrib/graphbuilder.cpp',
  'src/contrib/graphbuilderadapter.cpp',
)

yaml_cpp_lib = library(
  'yaml-cpp',
  [yaml_cpp_sources, yaml_cpp_contrib_sources],
  include_directories: inc,
  install: true,
)

install_headers(
  yaml_cpp_headers,
  subdir: 'yaml-cpp',
)
yaml_cpp_dep = declare_dependency(
  include_directories: inc,
  link_with: yaml_cpp_lib,
)

pkg_mod = import('pkgconfig')
pkg_mod.generate(
  yaml_cpp_lib,
  name: 'Yaml-cpp',
  filebase: 'yaml-cpp',
)
