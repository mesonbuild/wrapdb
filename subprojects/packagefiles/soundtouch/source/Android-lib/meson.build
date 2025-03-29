soundtouch_sources_android = files('jni/soundtouch-jni.cpp')

log = cpp.find_library(
  'log',
  required: true,
)

deps += [log]

soundtouch_args += cpp.get_supported_arguments(
  '-fdata-sections',
  '-ffunction-sections',
)
