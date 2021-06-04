h_root_sources_public = [
  'attribute.h',
  'attributedeclaration.h',
  'attributenode.h',
  'document.h',
  'dtd.h',
  'keepblanks.h',
  'noncopyable.h',
  'relaxngschema.h',
  'schemabase.h',
  'xsdschema.h']
h_exceptions_sources_public = [
  'exceptions/exception.h',
  'exceptions/parse_error.h',
  'exceptions/validity_error.h',
  'exceptions/internal_error.h',
  'exceptions/wrapped_exception.h']
h_io_sources_public = [
  'io/istreamparserinputbuffer.h',
  'io/outputbuffer.h',
  'io/ostreamoutputbuffer.h',
  'io/parserinputbuffer.h']
h_nodes_sources_public = [
  'nodes/cdatanode.h',
  'nodes/commentnode.h',
  'nodes/contentnode.h',
  'nodes/element.h',
  'nodes/entitydeclaration.h',
  'nodes/entityreference.h',
  'nodes/node.h',
  'nodes/processinginstructionnode.h',
  'nodes/textnode.h',
  'nodes/xincludeend.h',
  'nodes/xincludestart.h']
h_parsers_sources_public = [
  'parsers/parser.h',
  'parsers/saxparser.h',
  'parsers/domparser.h',
  'parsers/textreader.h']
h_validators_sources_public = [
  'validators/dtdvalidator.h',
  'validators/relaxngvalidator.h',
  'validators/schemavalidatorbase.h',
  'validators/validator.h',
  'validators/xsdvalidator.h']

h_sources_public = ['libxml++.h'] + h_root_sources_public + h_exceptions_sources_public + h_io_sources_public + h_parsers_sources_public + h_validators_sources_public

install_headers('libxml++.h', h_root_sources_public, subdir: 'libxml++')
install_headers(h_exceptions_sources_public, subdir: 'libxml++/exceptions')
install_headers(h_io_sources_public, subdir: 'libxml++/io')
install_headers(h_parsers_sources_public, subdir: 'libxml++/parsers')
install_headers(h_validators_sources_public, subdir: 'libxml++/validators')

cc_sources = [
  'attribute.cc',
  'attributedeclaration.cc',
  'attributenode.cc',
  'document.cc',
  'dtd.cc',
  'keepblanks.cc',
  'noncopyable.cc',
  'relaxngschema.cc',
  'schemabase.cc',
  'xsdschema.cc',
  'exceptions/exception.cc',
  'exceptions/parse_error.cc',
  'exceptions/validity_error.cc',
  'exceptions/internal_error.cc',
  'exceptions/wrapped_exception.cc',
  'io/istreamparserinputbuffer.cc',
  'io/outputbuffer.cc',
  'io/ostreamoutputbuffer.cc',
  'io/parserinputbuffer.cc',
  'nodes/cdatanode.cc',
  'nodes/commentnode.cc',
  'nodes/contentnode.cc',
  'nodes/element.cc',
  'nodes/entitydeclaration.cc',
  'nodes/entityreference.cc',
  'nodes/node.cc',
  'nodes/processinginstructionnode.cc',
  'nodes/textnode.cc',
  'nodes/xincludeend.cc',
  'nodes/xincludestart.cc',
  'parsers/parser.cc',
  'parsers/saxparser.cc',
  'parsers/domparser.cc',
  'parsers/textreader.cc',
  'validators/dtdvalidator.cc',
  'validators/relaxngvalidator.cc',
  'validators/schemavalidatorbase.cc',
  'validators/validator.cc',
  'validators/xsdvalidator.cc']

glibmm_dep = dependency('glibmm-2.4')
libxml_dep = dependency('libxml-2.0')

libxmlpp_lib = library('xml++', cc_sources,
		       soversion: libxmlpp_soversion,
		       version: libxmlpp_version,
		       include_directories: toplevel_inc,
		       dependencies: [glibmm_dep, libxml_dep],
		       install: true)
libxmlpp_dep = declare_dependency(link_with: libxmlpp_lib,
				  include_directories: [toplevel_inc, include_directories('.')],
				  dependencies: [glibmm_dep, libxml_dep])
