inc = include_directories('..')
cmph_lib = library('cmph', [
  'hash.c',
  'jenkins_hash.c',
  'vstack.c',
  'vqueue.c',
  'graph.c',
  'cmph.c',
  'cmph_structs.c',
  'chm.c',
  'bmz.c',
  'bmz8.c',
  'bdz.c',
  'bdz_ph.c',
  'brz.c',
  'fch.c',
  'fch_buckets.c',
  'chd.c',
  'chd_ph.c',
  'miller_rabin.c',
  'buffer_manager.c',
  'buffer_entry.c',
  'select.c',
  'compressed_seq.c',
  'compressed_rank.c',
  'linear_string_map.c',
  ],
  include_directories: inc,
  version: meson.project_version(),
  install: not meson.is_subproject() or get_option('default_library') == 'shared',
  dependencies: cc.find_library('m', required: false),
  vs_module_defs: 'cmph.def',
)
cmph_internal_dep = declare_dependency(link_with: cmph_lib, include_directories: inc)

if not meson.is_subproject()
  install_headers([
    'cmph.h',
    'cmph_types.h',
    'cmph_time.h',
    'chd_ph.h',
  ])
endif

executable('cmph', 'main.c', 'wingetopt.c',
  dependencies: cmph_internal_dep,
  install: not meson.is_subproject(),
  build_by_default: not meson.is_subproject(),
)

# XXX cmph_benchmark.c depends on <sys/resource.h> which is not available on Windows
if host_machine.system() != 'windows'
  executable('bm_numbers', 'bm_numbers.c', 'cmph_benchmark.c',
    dependencies: cmph_internal_dep,
    build_by_default: not meson.is_subproject(),
  )
endif