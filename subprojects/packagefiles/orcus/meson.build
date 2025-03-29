project(
  'liborcus',
  'cpp',
  version: '0.19.2',
  default_options: 'cpp_std=c++17',
)

varr = meson.project_version().split('.')
version_major = varr[0]
version_minor = varr[1]
version_micro = varr[2]

boost_dep = dependency('boost')
boost_fs_dep = dependency(
  'boost',
  modules: ['filesystem'],
)
boost_ios_dep = dependency(
  'boost',
  modules: ['iostreams'],
)

thread_dep = dependency('threads')
mdds_dep = dependency('mdds-2.1')
zlib_dep = dependency('zlib')

subdir('src')

liborcus_dep = declare_dependency(
  include_directories: 'include',
  link_with: [parser_lib, orcus_lib],
)
