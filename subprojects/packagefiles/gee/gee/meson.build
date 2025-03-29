gee_files = files(
  'abstractbidirlist.vala',
  'abstractbidirsortedmap.vala',
  'abstractbidirsortedset.vala',
  'abstractcollection.vala',
  'abstractlist.vala',
  'abstractmap.vala',
  'abstractmultimap.vala',
  'abstractmultiset.vala',
  'abstractqueue.vala',
  'abstractset.vala',
  'abstractsortedmap.vala',
  'abstractsortedset.vala',
  'arraylist.vala',
  'arrayqueue.vala',
  # Don't build assemblyinfo.vala because it's empty.
  # See https://gitlab.gnome.org/GNOME/vala/-/issues/1457.
  #'assemblyinfo.vala',
  'bidiriterator.vala',
  'bidirlist.vala',
  'bidirlistiterator.vala',
  'bidirmapiterator.vala',
  'bidirsortedmap.vala',
  'bidirsortedset.vala',
  'collection.vala',
  'comparable.vala',
  'concurrentlist.vala',
  'concurrentset.vala',
  'deque.vala',
  'functions.vala',
  'future.vala',
  'hashable.vala',
  'hashmap.vala',
  'hashmultimap.vala',
  'hashmultiset.vala',
  'hashset.vala',
  'hazardpointer.vala',
  'iterable.vala',
  'iterator.vala',
  'lazy.vala',
  'lightmapfuture.vala',
  'linkedlist.vala',
  'list.vala',
  'listiterator.vala',
  'map.vala',
  'mapiterator.vala',
  'multimap.vala',
  'multiset.vala',
  'priorityqueue.vala',
  'promise.vala',
  'queue.vala',
  'readonlybidirlist.vala',
  'readonlybidirsortedmap.vala',
  'readonlybidirsortedset.vala',
  'readonlycollection.vala',
  'readonlylist.vala',
  'readonlymap.vala',
  'readonlymultimap.vala',
  'readonlymultiset.vala',
  'readonlyset.vala',
  'readonlysortedmap.vala',
  'readonlysortedset.vala',
  'set.vala',
  'sortedmap.vala',
  'sortedset.vala',
  'streamiterator.vala',
  'task.vala',
  'teeiterator.vala',
  'timsort.vala',
  'traversable.vala',
  'treemap.vala',
  'treemultimap.vala',
  'treemultiset.vala',
  'treeset.vala',
  'unfolditerator.vala',
  'unrolledlinkedlist.vala',
)

gee_name = 'gee-' + api_version
gee_gir = 'Gee-' + api_version + '.gir'
gee_typelib = 'Gee-' + api_version + '.typelib'
gee_deps = [glib_dep, gobject_dep, gio_dep]
gee_c_args = []
if host_machine.system() == 'windows'
  gee_c_args += meson.get_compiler('c').get_supported_arguments(
    [
      '/Za',  # Stop stdlib.h from #defining min/max macros.
    ],
  )
endif
gee_c_args += meson.get_compiler('c').get_supported_arguments(
  [
    '-Wno-incompatible-function-pointer-types',  # In clang 16+, this is an error by default.
  ],
)

gee_lib = library(
  gee_name,
  gee_files,
  soversion: '2.6.1',
  version: meson.project_version(),
  c_args: gee_c_args,
  vala_header: 'gee.h',
  vala_vapi: gee_name + '.vapi',
  vala_gir: gee_gir,
  dependencies: [gee_deps, geeutils_dep],
  install: true,
  install_dir: [
    true,
    join_paths(get_option('includedir'), gee_name),
    true,
    true,
  ],
)

gee_dep = declare_dependency(
  link_with: gee_lib,
  dependencies: gee_deps,
  include_directories: include_directories('.'),
)
meson.override_dependency('gee-0.8', gee_dep)
