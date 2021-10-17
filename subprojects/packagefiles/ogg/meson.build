project('libogg', 'c', version : '1.3.5', license : 'bsd-like')

# See configure.ac and CMakeLists.txt
lib_current = 8
lib_revision = 5
lib_age = 8
lib_soversion = lib_current - lib_age
lib_version = '@0@.@1@.@2@'.format(lib_soversion, lib_age, lib_revision)

incdir = include_directories('include')
subdir('include/ogg')
subdir('src')
