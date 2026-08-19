resources = files(
  'aws-region.json',
  'custom_object_condition.json',
  'custom_partition.json',
  'default-values.json',
  'deprecated-param.json',
  'eventbridge.json',
  'fns.json',
  'get-attr-type-inference.json',
  'headers.json',
  'is-virtual-hostable-s3-bucket.json',
  'minimal-ruleset.json',
  'parse-arn.json',
  'parse-url.json',
  'partition-fn.json',
  'region-override.json',
  'string_array.json',
  'substring.json',
  'uri-encode.json',
  'valid-hostlabel.json',
)

foreach name : resources
  copied += fs.copyfile(name)
endforeach
