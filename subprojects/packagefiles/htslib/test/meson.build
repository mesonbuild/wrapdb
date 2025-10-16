if not get_option('tests')
  subdir_done()
endif

# tests rely on -fvisibility=hidden symbols
htslib_test_lib = static_library(
  'statichts',
  objects: htslib_lib.extract_all_objects(
    recursive: false,
  ),
  include_directories: '..',
  install: false,
  dependencies: [libm_dep, regex_dep, thread_dep, ws_dep, zlib_dep],
)

htslib_test_lib_dep = declare_dependency(
  include_directories: '..',
  link_with: htslib_test_lib,
)

tests = {
  'fieldarith': files('fieldarith.sam'),
  'hfile': [],
  'hts_endian': [],
  'sam': files('ce.fa', 'faidx/faidx.fa', 'faidx/fastqs.fq'),
  'test_bgzf': files('bgziptest.txt'),
  'test_expr': [],
  'test_kfunc': [],
  'test_kstring': [],
  'test-parse-reg': ['-t', files('colons.bam')],
  'test_str2int': [],
  'test-regidx': [],
}

foreach t, a : tests
  test(
    t,
    executable(
      t,
      t + '.c',
      dependencies: htslib_test_lib_dep,
    ),
    args: a,
    workdir: htslib_source_root,
  )
endforeach
