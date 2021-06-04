project('libxml++', 'cpp',
	version: '3.0.1',
	license: 'LGPL 2.1')

libxmlpp_version = meson.project_version()
libxmlpp_soversion = '1:0:0'
version_array = libxmlpp_version.split('.')
libxmlpp_major_version = version_array[0].to_int()
libxmlpp_minor_version = version_array[1].to_int()
libxmlpp_micro_version = version_array[2].to_int()

compiler = meson.get_compiler('cpp')
if (compiler.compute_int('__cplusplus') < 201103)
  error('Compiler does not implement c++11')
endif

if (not compiler.has_header('string') or not compiler.has_header('list') or not compiler.has_header('map'))
  error('Required headers not found')
endif

exception_test_code = '''#include <exception>
void func() {
  try
  {
      throw "custom error";
  }
  catch(...)
  {
      std::exception_ptr ep = std::current_exception();
      std::rethrow_exception(ep);
  }
}'''
exception_test_result = compiler.compiles(exception_test_code,
					  name: 'has exception ptr')

conf_data = configuration_data()
if (get_option('disable_deprecated'))
  conf_data.set10('LIBXMLXX_DISABLE_DEPRECATED', get_option('disable_deprecated'))
endif

if (exception_test_result)
  conf_data.set10('LIBXMLXX_HAVE_EXCEPTION_PTR', exception_test_result)
endif
conf_data.set('LIBXMLXX_MAJOR_VERSION', libxmlpp_major_version)
conf_data.set('LIBXMLXX_MINOR_VERSION', libxmlpp_minor_version)
conf_data.set('LIBXMLXX_MICRO_VERSION', libxmlpp_micro_version)

configure_file(input: 'libxml++config.h.meson',
	       output: 'libxml++config.h',
	       configuration: conf_data,
	       install_dir: 'libxml++')

conf_data = configuration_data()
conf_data.set('LIBXMLXX_DISABLE_DEPRECATED', get_option('disable_deprecated'))
conf_data.set('LIBXMLXX_HAVE_EXCEPTION_PTR', exception_test_result)
conf_data.set('LIBXMLXX_MAJOR_VERSION', libxmlpp_major_version)
conf_data.set('LIBXMLXX_MINOR_VERSION', libxmlpp_minor_version)
conf_data.set('LIBXMLXX_MICRO_VERSION', libxmlpp_micro_version)
conf_data.set('HAVE_CONFIG_H', '1')
configure_file(input: 'libxml++config.h.meson',
	       output: 'config.h',
	       configuration: conf_data)

add_project_arguments('-DLIBXMLPP_BUILD', language: 'cpp')

toplevel_inc = include_directories('.')

subdir('libxml++')
subdir('tests')
