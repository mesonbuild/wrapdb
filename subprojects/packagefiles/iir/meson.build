project('iir', 'cpp',
        version : '1.9.2',
        license : 'MIT',
        meson_version: '>=0.46.0',
        default_options : ['cpp_std=c++11',
                           'default_library=both',
                           'b_ndebug=if-release',
                           'warning_level=3'])

install_headers('Iir.h')

incdirs = include_directories('.')

subdir('iir')

if get_option('demos')
  subdir('demo')
endif

if get_option('tests')
  subdir('test')
endif

