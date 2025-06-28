project(
  'tkrzw',
  'cpp',
  version: '1.0.32',
  license: 'Apache-2.0',
  meson_version: '>=0.63.0',
  default_options: ['cpp_std=c++17', 'b_ndebug=true'],
)

libversion = '1.75.0'

cpp = meson.get_compiler('cpp')

cpp_args = [
  cpp.get_supported_arguments(
    '-fsigned-char',
    '-Wno-unused-parameter',
    '/EHsc',
    '/wd4244',
    '/wd4267',
    '/wd4334',
  ),
  '-D_GNU_SOURCE=1',
  '-D_POSIX_C_SOURCE=999999L',
  '-D_DARWIN_C_SOURCE',
  '-D_CRT_SECURE_NO_WARNINGS',
  '-D_TKRZW_PKG_VERSION="@0@"'.format(meson.project_version()),
  '-D_TKRZW_LIB_VERSION="@0@"'.format(libversion),
]
if host_machine.endian() == 'big'
  cpp_args += '-D_TKRZW_BIGEND'
endif

deps = []
if host_machine.system() == 'windows'
  libtarget = 'static_library'
else
  libtarget = 'library'
  deps += dependency('threads')
endif

depinfo = [
  ['liblz4', 'lz4', '-D_TKRZW_COMP_LZ4'],
  ['liblzma', 'lzma', '-D_TKRZW_COMP_LZMA'],
  ['zlib', 'zlib', '-D_TKRZW_COMP_ZLIB'],
  ['libzstd', 'zstd', '-D_TKRZW_COMP_ZSTD'],
]
foreach dinfo : depinfo
  dep = dependency(
    dinfo[0],
    required: get_option(dinfo[1]),
  )
  if dep.found()
    cpp_args += dinfo[2]
    deps += dep
  endif
endforeach

libsrc = files(
  'tkrzw_cmd_util.cc',
  'tkrzw_compress.cc',
  'tkrzw_dbm.cc',
  'tkrzw_dbm_async.cc',
  'tkrzw_dbm_baby.cc',
  'tkrzw_dbm_cache.cc',
  'tkrzw_dbm_common_impl.cc',
  'tkrzw_dbm_hash.cc',
  'tkrzw_dbm_hash_impl.cc',
  'tkrzw_dbm_poly.cc',
  'tkrzw_dbm_shard.cc',
  'tkrzw_dbm_skip.cc',
  'tkrzw_dbm_skip_impl.cc',
  'tkrzw_dbm_std.cc',
  'tkrzw_dbm_tiny.cc',
  'tkrzw_dbm_tree.cc',
  'tkrzw_dbm_tree_impl.cc',
  'tkrzw_dbm_ulog.cc',
  'tkrzw_file_mmap.cc',
  'tkrzw_file_poly.cc',
  'tkrzw_file_pos.cc',
  'tkrzw_file_std.cc',
  'tkrzw_file_util.cc',
  'tkrzw_hash_util.cc',
  'tkrzw_langc.cc',
  'tkrzw_lib_common.cc',
  'tkrzw_message_queue.cc',
  'tkrzw_str_util.cc',
  'tkrzw_time_util.cc',
)
tkrzw = build_target(
  'tkrzw',
  libsrc,
  cpp_args: cpp_args,
  darwin_versions: [libversion.split('.')[0], libversion],
  dependencies: deps,
  target_type: libtarget,
  version: libversion,
)
tkrzw_dep = declare_dependency(
  include_directories: '.',
  link_with: tkrzw,
)
meson.override_dependency('tkrzw', tkrzw_dep)

progs = ['tkrzw_dbm_perf', 'tkrzw_dbm_util', 'tkrzw_ulog_util']
foreach prog : progs
  exe = executable(
    prog,
    prog + '.cc',
    cpp_args: cpp_args,
    link_with: tkrzw,
  )
  meson.override_find_program(prog, exe)
endforeach
