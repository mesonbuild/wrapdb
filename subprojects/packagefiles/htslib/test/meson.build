# tests rely on -fvisibility=hidden symbols
htslib_test_lib = static_library(
  'statichts', [
    htslib_config_h,
    htslib_config_vars_h,
    htslib_version_h],
  objects: htslib_lib.extract_all_objects(recursive : false),
  include_directories: '..',
  install : false,
  dependencies : [
    libm_dep,
    thread_dep,
    zlib_dep])

test('hts_endian',
  executable(
    'hts_endian', [
      htslib_config_h,
      files(['hts_endian.c'])],
    link_with : htslib_test_lib,
    include_directories: '..',
    install : false))

test('test_expr',
  executable(
    'test_expr', [
      htslib_config_h,
      files(['test_expr.c'])],
    link_with : htslib_test_lib,
    include_directories: '..',
    install : false))

test('test_kfunc',
  executable(
    'test_kfunc', [
      htslib_config_h,
      files(['test_kfunc.c'])],
    link_with : htslib_test_lib,
    include_directories: '..',
    install : false))

test('test_kstring',
  executable(
    'test_kstring', [
      htslib_config_h,
      files(['test_kstring.c'])],
    link_with : htslib_test_lib,
    include_directories: '..',
    install : false))

test('test_str2int',
  executable(
    'test_str2int', [
      htslib_config_h,
      files(['test_str2int.c'])],
    link_with : htslib_test_lib,
    include_directories: '..',
    install : false))

test('test_fieldarith',
  executable(
    'fieldarith', [
      htslib_config_h,
      files(['fieldarith.c'])],
    link_with : htslib_test_lib,
    include_directories: '..',
    install : false),
  args : files(['fieldarith.sam']))

test('test_hfile',
  executable(
    'test_hfile', [
      htslib_config_h,
      files(['hfile.c'])],
    link_with : htslib_test_lib,
    include_directories: '..',
    install : false),
  workdir : htslib_source_root)

test('test_bgzf',
  executable(
    'test_bgzf', [
      htslib_config_h,
      files(['test_bgzf.c'])],
    link_with : htslib_test_lib,
    include_directories: '..',
    install : false),
  args : files(['bgziptest.txt']))

test('test-parse-reg',
  executable(
    'test-parse-reg', [
      htslib_config_h,
      files(['test-parse-reg.c'])],
    link_with : htslib_test_lib,
    include_directories: '..',
    install : false),
  args : ['-t', files(['colons.bam'])])

test('test-sam',
  executable(
    'test-sam', [
      htslib_config_h,
      files(['sam.c'])],
    link_with : htslib_test_lib,
    include_directories: '..',
    install : false),
  env : {'REF_PATH' : ':'},
  args : files(['ce.fa', 'faidx.fa', 'fastqs.fq']),
  workdir : htslib_source_root)

test('test-regidx',
  executable(
    'test-regidx', [
      htslib_config_h,
      files(['test-regidx.c'])],
    link_with : htslib_test_lib,
    include_directories: '..',
    install : false))
