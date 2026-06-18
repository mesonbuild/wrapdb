resources = files(
  'partitions.json',
  'sample_partitions.json',
  'sample_partitions_bad_regex.json',
  'sample_ruleset.json',
)

foreach name : resources
  copied += fs.copyfile(name)
endforeach

test_harness = executable(
  'aws-c-sdkutils-tests',
  test_harness_src,
  dependencies: [aws_c_sdkutils_dep],
  link_with: [libtestcases],
  c_args: ['-DAWS_UNSTABLE_TESTING_API=1'],
  include_directories: inc,
  build_by_default: false,
)
