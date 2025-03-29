if get_option('lightweight_symtab')
  message('-Dlightweight_symtab=true; parseThat not built')
  subdir_done()
endif

parseThat = executable(
  'parseThat',
  'src/parseThat.C',
  'src/config.C',
  'src/ipc.C',
  'src/record.C',
  'src/strlist.C',
  'src/reglist.C',
  'src/log.C',
  'src/utils.C',
  'src/sha1.C',
  'src/dyninstCore.C',
  'src/dyninstCompat.v5.C',
  override_options: ['b_ndebug=false'],
  c_args: '-DHAVE_BPATCH_PROCESS_H',
  cpp_args: '-DHAVE_BPATCH_PROCESS_H',
  dependencies: [dyninstapi_dep],
  install: true,
)
meson.override_find_program('parseThat', parseThat)
