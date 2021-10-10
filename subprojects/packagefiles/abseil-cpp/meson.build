project('abseil-cpp', 'cpp',
  version : '20210324.1',
  license : 'Apache-2.0',
  default_options : [
    'cpp_std=c++11',
  ])

cpp = meson.get_compiler('cpp')

cpp_flags = [
  '-Wno-sign-compare'
]

if host_machine.cpu_family() == 'x86_64'
  cpp_flags += [ '-maes', '-msse4.1' ]
elif host_machine.cpu_family() == 'aarch64' and cpp.sizeof('void*') == 8
  cpp_flags += [ '-march=armv8-a+crypto' ]
elif host_machine.cpu_family() == 'arm' and cpp.sizeof('void*') == 4
  cpp_flags += [ '-mfpu=neon' ]
endif

flags = cpp.get_supported_arguments(cpp_flags)

if cpp.get_id() == 'msvc'
  flags += ['/DNOMINMAX'] # Don't define min and max macros (windows.h)
endif

add_project_arguments(flags, language: 'cpp')

libatomic = dependency('', required: false)
if cpp.get_id() == 'msvc'
    # VS does not not need args for atomic ops.
elif not cpp.links('''#include <stdint.h>
                      int main() {
                        struct {
                          uint64_t *v;
                        } x;
                        return (int)__atomic_load_n(x.v, __ATOMIC_ACQUIRE) &
                               (int)__atomic_add_fetch(x.v, (uint64_t)1, __ATOMIC_ACQ_REL);
                      }''',
                name : 'GCC atomic builtins')
  libatomic = cpp.find_library('atomic')
endif

absl_include_dir = include_directories('.')

# Group files by the containing library
absl_base_sources = files(
  'absl/base/internal/cycleclock.cc',
  'absl/base/internal/exponential_biased.cc',
  'absl/base/internal/low_level_alloc.cc',
  'absl/base/internal/periodic_sampler.cc',
  'absl/base/internal/raw_logging.cc',
  'absl/base/internal/scoped_set_env.cc',
  'absl/base/internal/spinlock_wait.cc',
  'absl/base/internal/spinlock.cc',
  'absl/base/internal/sysinfo.cc',
  'absl/base/internal/strerror.cc',
  'absl/base/internal/thread_identity.cc',
  'absl/base/internal/throw_delegate.cc',
  'absl/base/internal/unscaledcycleclock.cc',
  'absl/base/log_severity.cc',
)

absl_container_sources = files(
  'absl/container/internal/hashtablez_sampler_force_weak_definition.cc',
  'absl/container/internal/hashtablez_sampler.cc',
  'absl/container/internal/raw_hash_set.cc',
)

absl_debugging_sources = files(
  'absl/debugging/failure_signal_handler.cc',
  'absl/debugging/internal/address_is_readable.cc',
  'absl/debugging/internal/demangle.cc',
  'absl/debugging/internal/elf_mem_image.cc',
  'absl/debugging/internal/examine_stack.cc',
  'absl/debugging/internal/stack_consumption.cc',
  'absl/debugging/internal/vdso_support.cc',
  'absl/debugging/leak_check_disable.cc',
  'absl/debugging/leak_check.cc',
  'absl/debugging/stacktrace.cc',
  'absl/debugging/symbolize.cc',
)

absl_flags_sources = files(
  'absl/flags/commandlineflag.cc',
  'absl/flags/flag.cc',
  'absl/flags/internal/commandlineflag.cc',
  'absl/flags/internal/flag.cc',
  'absl/flags/internal/program_name.cc',
  'absl/flags/internal/private_handle_accessor.cc',
  'absl/flags/internal/usage.cc',
  'absl/flags/marshalling.cc',
  'absl/flags/parse.cc',
  'absl/flags/reflection.cc',
  'absl/flags/usage_config.cc',
  'absl/flags/usage.cc',
)

absl_hash_sources = files(
  'absl/hash/internal/city.cc',
  'absl/hash/internal/hash.cc',
  'absl/hash/internal/wyhash.cc',
)

absl_numeric_sources = files(
  'absl/numeric/int128.cc',
)

absl_random_sources = files(
  'absl/random/discrete_distribution.cc',
  'absl/random/gaussian_distribution.cc',
  'absl/random/internal/chi_square.cc',
  'absl/random/internal/distribution_test_util.cc',
  'absl/random/internal/pool_urbg.cc',
  'absl/random/internal/randen_detect.cc',
  'absl/random/internal/randen_hwaes.cc',
  'absl/random/internal/randen_slow.cc',
  'absl/random/internal/randen_round_keys.cc',
  'absl/random/internal/randen.cc',
  'absl/random/internal/seed_material.cc',
  'absl/random/seed_gen_exception.cc',
  'absl/random/seed_sequences.cc',
)

absl_status_sources = files(
  'absl/status/status_payload_printer.cc',
  'absl/status/status.cc',
  'absl/status/statusor.cc',
)

absl_strings_sources = files(
  'absl/strings/ascii.cc',
  'absl/strings/charconv.cc',
  'absl/strings/cord.cc',
  'absl/strings/escaping.cc',
  'absl/strings/internal/charconv_bigint.cc',
  'absl/strings/internal/charconv_parse.cc',
  'absl/strings/internal/cord_internal.cc',
  'absl/strings/internal/cord_rep_ring.cc',
  'absl/strings/internal/escaping.cc',
  'absl/strings/internal/memutil.cc',
  'absl/strings/internal/ostringstream.cc',
  'absl/strings/internal/pow10_helper.cc',
  'absl/strings/internal/str_format/arg.cc',
  'absl/strings/internal/str_format/bind.cc',
  'absl/strings/internal/str_format/extension.cc',
  'absl/strings/internal/str_format/float_conversion.cc',
  'absl/strings/internal/str_format/output.cc',
  'absl/strings/internal/str_format/parser.cc',
  'absl/strings/internal/utf8.cc',
  'absl/strings/match.cc',
  'absl/strings/numbers.cc',
  'absl/strings/str_cat.cc',
  'absl/strings/str_replace.cc',
  'absl/strings/str_split.cc',
  'absl/strings/string_view.cc',
  'absl/strings/substitute.cc',
)

absl_synchronization_sources = files(
  'absl/synchronization/barrier.cc',
  'absl/synchronization/blocking_counter.cc',
  'absl/synchronization/internal/create_thread_identity.cc',
  'absl/synchronization/internal/graphcycles.cc',
  'absl/synchronization/internal/per_thread_sem.cc',
  'absl/synchronization/internal/waiter.cc',
  'absl/synchronization/mutex.cc',
  'absl/synchronization/notification.cc',
)

absl_time_sources = files(
  'absl/time/civil_time.cc',
  'absl/time/clock.cc',
  'absl/time/duration.cc',
  'absl/time/format.cc',
  'absl/time/internal/cctz/src/civil_time_detail.cc',
  'absl/time/internal/cctz/src/time_zone_fixed.cc',
  'absl/time/internal/cctz/src/time_zone_format.cc',
  'absl/time/internal/cctz/src/time_zone_if.cc',
  'absl/time/internal/cctz/src/time_zone_impl.cc',
  'absl/time/internal/cctz/src/time_zone_info.cc',
  'absl/time/internal/cctz/src/time_zone_libc.cc',
  'absl/time/internal/cctz/src/time_zone_lookup.cc',
  'absl/time/internal/cctz/src/time_zone_posix.cc',
  'absl/time/internal/cctz/src/zone_info_source.cc',
  'absl/time/time.cc',
)

absl_types_sources = files(
  'absl/types/bad_any_cast.cc',
  'absl/types/bad_optional_access.cc',
  'absl/types/bad_variant_access.cc',
)

# Libraries
absl_base_lib = static_library(
  'absl_base',
  absl_base_sources,
  include_directories: absl_include_dir,
  dependencies: [dependency('threads'), libatomic],
)

absl_hash_lib = static_library(
  'absl_hash',
  absl_hash_sources,
  include_directories: absl_include_dir,
)

absl_numeric_lib = static_library(
  'absl_numeric',
  absl_numeric_sources,
  include_directories: absl_include_dir,
)

absl_strings_lib = static_library(
  'absl_strings',
  absl_strings_sources,
  include_directories: absl_include_dir,
  link_with: [
    absl_base_lib,
    absl_numeric_lib,
  ],
)

absl_debugging_lib = static_library(
  'absl_debugging',
  absl_debugging_sources,
  include_directories: absl_include_dir,
  link_with: [
    absl_base_lib,
    absl_strings_lib,
  ],
  dependencies: libatomic,
)

absl_random_lib = static_library(
  'absl_random',
  absl_random_sources,
  include_directories: absl_include_dir,
  link_with: [
    absl_base_lib,
    absl_strings_lib,
  ],
  dependencies: libatomic,
)

absl_time_lib = static_library(
  'absl_time',
  absl_time_sources,
  include_directories: absl_include_dir,
  link_with: [
    absl_base_lib,
    absl_numeric_lib,
    absl_strings_lib,
  ],
  # macOS only, upstream: https://github.com/abseil/abseil-cpp/pull/280
  dependencies : [dependency('CoreFoundation', required : false)],
)

absl_types_lib = static_library(
  'absl_types',
  absl_types_sources,
  include_directories: absl_include_dir,
)

absl_synchronization_lib = static_library(
  'absl_synchronization',
  absl_synchronization_sources,
  include_directories: absl_include_dir,
  link_with: [
    absl_base_lib,
    absl_debugging_lib,
    absl_time_lib,
  ],
)

absl_container_lib = static_library(
  'absl_container',
  absl_container_sources,
  include_directories: absl_include_dir,
  link_with: [
    absl_base_lib,
    absl_debugging_lib,
    absl_hash_lib,
    absl_synchronization_lib,
    absl_time_lib,
  ],
)

absl_flags_lib = static_library(
  'absl_flags',
  absl_flags_sources,
  include_directories: absl_include_dir,
  link_with: [
    absl_base_lib,
    absl_container_lib,
    absl_hash_lib,
    absl_strings_lib,
    absl_synchronization_lib,
  ],
  dependencies: libatomic,
)

absl_status_lib = static_library(
  'absl_status',
  absl_status_sources,
  include_directories: absl_include_dir,
  link_with: [
    absl_base_lib,
    absl_strings_lib,
  ],
)

# Dependencies
absl_base_dep = declare_dependency(
  include_directories: absl_include_dir,
  link_with: absl_base_lib,
)

absl_hash_dep = declare_dependency(
  include_directories: absl_include_dir,
  link_with: absl_hash_lib,
)

absl_numeric_dep = declare_dependency(
  include_directories: absl_include_dir,
  link_with: absl_numeric_lib,
)

absl_strings_dep = declare_dependency(
  include_directories: absl_include_dir,
  link_with: absl_strings_lib,
  dependencies: [
    absl_base_dep,
    absl_numeric_dep,
  ],
)

absl_debugging_dep = declare_dependency(
  include_directories: absl_include_dir,
  link_with: absl_debugging_lib,
  dependencies: [
    absl_base_dep,
    absl_strings_dep,
  ],
)

absl_random_dep = declare_dependency(
  include_directories: absl_include_dir,
  link_with: absl_random_lib,
  dependencies: [
    absl_base_dep,
    absl_strings_dep,
  ],
)

absl_time_dep = declare_dependency(
  include_directories: absl_include_dir,
  link_with: absl_time_lib,
  dependencies: [
    absl_base_dep,
    absl_numeric_dep,
    absl_strings_dep,
  ],
)

absl_types_dep = declare_dependency(
  include_directories: absl_include_dir,
  link_with: absl_types_lib,
)

absl_synchronization_dep = declare_dependency(
  include_directories: absl_include_dir,
  link_with: absl_synchronization_lib,
  dependencies: [
    absl_base_dep,
    absl_debugging_dep,
    absl_time_dep,
  ],
)

absl_container_dep = declare_dependency(
  include_directories: absl_include_dir,
  link_with: absl_container_lib,
  dependencies: [
    absl_base_dep,
    absl_debugging_dep,
    absl_hash_dep,
    absl_synchronization_dep,
    absl_time_dep,
  ],
)

absl_flags_dep = declare_dependency(
  include_directories: absl_include_dir,
  link_with: absl_flags_lib,
  dependencies: [
    absl_base_dep,
    absl_container_dep,
    absl_hash_dep,
    absl_strings_dep,
    absl_synchronization_dep,
  ],
)

absl_status_dep = declare_dependency(
  include_directories: absl_include_dir,
  link_with: absl_status_lib,
  dependencies: [
    absl_base_dep,
    absl_strings_dep,
  ],
)
