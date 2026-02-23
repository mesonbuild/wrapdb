project(
  'aws-c-common',
  'c',
  version: '0.12.6',
  meson_version: '>=0.63.0',
  license: 'Apache-2.0',
  default_options: ['warning_level=3'],
)

cc = meson.get_compiler('c')

tests_opt = get_option('tests').disable_auto_if(meson.is_subproject())

libcbor = dependency('libcbor')
cjson = dependency('libcjson')
threads = dependency('threads')
m = cc.find_library(
  'm',
  required: false,
)
# linking to dl is required on Amazon Linux 2
dl = cc.find_library(
  'dl',
  required: false,
)
bcrypt = cc.find_library(
  'bcrypt',
  required: host_machine.system() == 'windows',
)
shlwapi = cc.find_library(
  'shlwapi',
  required: host_machine.system() == 'windows',
)
foundation = dependency(
  'appleframeworks',
  modules: ['CoreFoundation'],
  required: host_machine.system() == 'darwin',
)

fs = import('fs')
pkg = import('pkgconfig')

subdir('include/aws/common')

generic_src = files(
  'source/allocator.c',
  'source/allocator_sba.c',
  'source/array_list.c',
  'source/assert.c',
  'source/byte_buf.c',
  'source/cache.c',
  'source/cbor.c',
  'source/codegen.c',
  'source/command_line_parser.c',
  'source/common.c',
  'source/condition_variable.c',
  'source/date_time.c',
  'source/device_random.c',
  'source/encoding.c',
  'source/error.c',
  'source/fifo_cache.c',
  'source/file.c',
  'source/hash_table.c',
  'source/host_utils.c',
  'source/json.c',
  'source/lifo_cache.c',
  'source/linked_hash_table.c',
  'source/log_channel.c',
  'source/log_formatter.c',
  'source/log_writer.c',
  'source/logging.c',
  'source/lru_cache.c',
  'source/math.c',
  'source/memtrace.c',
  'source/priority_queue.c',
  'source/process_common.c',
  'source/ref_count.c',
  'source/ring_buffer.c',
  'source/statistics.c',
  'source/string.c',
  'source/system_info.c',
  'source/task_scheduler.c',
  'source/thread_scheduler.c',
  'source/thread_shared.c',
  'source/uri.c',
  'source/uuid.c',
  'source/xml_parser.c',
)

c_args = ['-DAWS_COMMON_EXPORTS=1']

# AWS_COMMON_USE_IMPORT_EXPORT should not be defined for static libraries on Windows
public_c_args = []
if (
  get_option('default_library') == 'shared'
  and host_machine.system() == 'windows'
) or host_machine.system() != 'windows'
  public_c_args += ['-DAWS_COMMON_USE_IMPORT_EXPORT=1']
endif

if host_machine.cpu_family() in ['x86', 'x86_64']
  if cc.get_argument_syntax() == 'msvc'
    arch_src = files('source/arch/intel/msvc/cpuid.c')
  else
    arch_src = files('source/arch/intel/asm/cpuid.c')
  endif
  arch_src += files('source/arch/intel/cpuid.c')
elif host_machine.cpu_family() == 'aarch64'
  if host_machine.system() == 'linux'
    arch_src = files('source/arch/arm/auxv/cpuid.c')
  elif host_machine.system() == 'darwin'
    arch_src = files('source/arch/arm/darwin/cpuid.c')
  elif host_machine.system() == 'windows'
    arch_src = files('source/arch/arm/windows/cpuid.c')
  else
    arch_src = files('source/arch/generic/cpuid.c')
  endif
else
  arch_src = files('source/arch/generic/cpuid.c')
endif

posix_src = files(
  'source/posix/clock.c',
  'source/posix/condition_variable.c',
  'source/posix/cross_process_lock.c',
  'source/posix/device_random.c',
  'source/posix/environment.c',
  'source/posix/file.c',
  'source/posix/mutex.c',
  'source/posix/process.c',
  'source/posix/rw_lock.c',
  'source/posix/system_info.c',
  'source/posix/system_resource_utils.c',
  'source/posix/thread.c',
  'source/posix/time.c',
)

if host_machine.system() == 'darwin'
  platform_src = posix_src + files(
    'source/platform_fallback_stubs/file_direct_io.c',
    'source/platform_fallback_stubs/system_info.c',
  )
  c_args += ['-DAWS_AFFINITY_METHOD=AWS_AFFINITY_METHOD_NONE']
elif host_machine.system() == 'linux'
  platform_src = posix_src + files(
    'source/linux/file_direct_io.c',
    'source/linux/system_info.c',
  )
  if cc.has_function(
    'pthread_attr_setaffinity_np',
    prefix: '#include <pthread.h>',
  )
    c_args += ['-DAWS_AFFINITY_METHOD=AWS_AFFINITY_METHOD_PTHREAD_ATTR']
  else
    c_args += ['-DAWS_AFFINITY_METHOD=AWS_AFFINITY_METHOD_PTHREAD']
  endif
elif host_machine.system() == 'windows'
  platform_src = files(
    'source/platform_fallback_stubs/file_direct_io.c',
    'source/platform_fallback_stubs/system_info.c',
    'source/windows/clock.c',
    'source/windows/condition_variable.c',
    'source/windows/cross_process_lock.c',
    'source/windows/device_random.c',
    'source/windows/environment.c',
    'source/windows/file.c',
    'source/windows/mutex.c',
    'source/windows/process.c',
    'source/windows/rw_lock.c',
    'source/windows/system_info.c',
    'source/windows/system_resource_utils.c',
    'source/windows/thread.c',
    'source/windows/time.c',
  )
  c_args += [
    '-DAWS_AFFINITY_METHOD=AWS_AFFINITY_METHOD_NONE',
    '-DWINDOWS_KERNEL_LIB=kernel32',
  ]
elif host_machine.system() == 'emscripten'
  platform_src = posix_src + files(
    'source/platform_fallback_stubs/system_info.c',
  )
  c_args += ['-DAWS_AFFINITY_METHOD=AWS_AFFINITY_METHOD_NONE']
else
  error('Unsupported platform: ' + host_machine.system())
endif

inc = include_directories('include')

libaws_c_common = library(
  'aws-c-common',
  generic_src,
  platform_src,
  arch_src,
  dependencies: [libcbor, cjson, threads, m, dl, bcrypt, shlwapi, foundation],
  c_args: c_args + public_c_args,
  include_directories: inc,
  install: true,
  version: meson.project_version(),
  gnu_symbol_visibility: 'hidden',
)

aws_c_common_dep = declare_dependency(
  link_with: libaws_c_common,
  include_directories: inc,
  compile_args: public_c_args,
)

meson.override_dependency('aws-c-common', aws_c_common_dep)

pkg.generate(
  libaws_c_common,
  extra_cflags: public_c_args,
  description: 'Core c99 package for AWS SDK for C. Includes cross-platform primitives, configuration, data structures, and error handling.',
)

generate_tests = find_program(
  'generate_tests.py',
  required: tests_opt,
)
run_test = find_program(
  'run_test.py',
  required: tests_opt,
)
if generate_tests.found() and run_test.found()
  test_src = files(
    'tests/alloc_test.c',
    'tests/array_list_test.c',
    'tests/assert_test.c',
    'tests/atomics_test.c',
    'tests/byte_buf_test.c',
    'tests/byte_cursor_find_test.c',
    'tests/byte_order_test.c',
    'tests/cache_test.c',
    'tests/calloc_test.c',
    'tests/cbor_test.c',
    'tests/clock_test.c',
    'tests/command_line_parser_test.c',
    'tests/condition_variable_test.c',
    'tests/cpuid_test.c',
    'tests/cross_process_lock_tests.c',
    'tests/cursor_test.c',
    'tests/date_time_test.c',
    'tests/device_random_test.c',
    'tests/encoding_test.c',
    'tests/environment_test.c',
    'tests/error_test.c',
    'tests/file_test.c',
    'tests/hash_table_test.c',
    'tests/host_util_test.c',
    'tests/json_test.c',
    'tests/linked_hash_table_test.c',
    'tests/linked_list_test.c',
    'tests/math_test.c',
    'tests/memtrace_test.c',
    'tests/mutex_test.c',
    'tests/priority_queue_test.c',
    'tests/process_test.c',
    'tests/realloc_test.c',
    'tests/ring_buffer_test.c',
    'tests/rw_lock_test.c',
    'tests/split_test.c',
    'tests/string_test.c',
    'tests/system_info_tests.c',
    'tests/system_resource_util_test.c',
    'tests/task_scheduler_test.c',
    'tests/thread_scheduler_test.c',
    'tests/thread_test.c',
    'tests/uri_test.c',
    'tests/uuid_test.c',
    'tests/xml_parser_test.c',
    'tests/zero_test.c',
  )

  logging_cases = files(
    'tests/logging/log_channel_test.c',
    'tests/logging/log_formatter_test.c',
    'tests/logging/log_writer_test.c',
    'tests/logging/logging_filter_debug_static_test.c',
    'tests/logging/logging_filter_error_static_test.c',
    'tests/logging/logging_filter_fatal_static_test.c',
    'tests/logging/logging_filter_info_static_test.c',
    'tests/logging/logging_filter_none_static_test.c',
    'tests/logging/logging_filter_trace_static_test.c',
    'tests/logging/logging_filter_warn_static_test.c',
    'tests/logging/logging_general_test.c',
    'tests/logging/logging_misc.c',
    'tests/logging/logging_test_utilities.c',
    'tests/logging/pipeline_logger_test.c',
    'tests/logging/test_logger.c',
  )

  libtestcases = static_library(
    'aws_c_common_testcases',
    test_src,
    logging_cases,
    dependencies: [aws_c_common_dep, threads, m, foundation],
    c_args: ['-DAWS_UNSTABLE_TESTING_API=1'],
    include_directories: inc,
    build_by_default: false,
  )

  # aws-c-common uses an obscure cmake feature `create_test_sourcelist` to generate test harnesses
  # this is a best effort approximation of that behavior
  test_harness_src = custom_target(
    'generate_test_harness',
    input: 'tests.txt',
    output: 'test_harness.c',
    command: [generate_tests, '@INPUT@', '@OUTPUT@'],
  )

  test_harness = executable(
    'aws-c-common-tests',
    test_harness_src,
    dependencies: [aws_c_common_dep, threads, m, foundation],
    link_with: [libtestcases],
    c_args: ['-DAWS_UNSTABLE_TESTING_API=1'],
    include_directories: inc,
    build_by_default: false,
  )

  names = fs.read('tests.txt').split('\n')

  foreach name : names
    test(
      name,
      run_test,
      args: [test_harness, name],
      workdir: meson.current_source_dir() / 'tests/resources',
      timeout: 600,
    )
  endforeach
endif
