cfg_data = configuration_data()

gcc_overflow_math_extensions = '''
#include <stdbool.h>
bool foo(int a, int b, int *c) {
    return __builtin_mul_overflow(a, b, c);
}

int main() {
    int out;
    if (foo(1, 2, &out)) {
        return 0;
    }

    return 0;
}
'''

cfg_data.set(
  'AWS_HAVE_GCC_OVERFLOW_MATH_EXTENSIONS',
  cc.links(
    gcc_overflow_math_extensions,
    name: 'gcc_overflow_math_extensions',
  ),
)

gcc_inline_asm = '''
int main() {
    int foo = 42, bar = 24;
    __asm__ __volatile__(\"\":\"=r\"(foo):\"r\"(bar):\"memory\");
}
'''

cfg_data.set(
  'AWS_HAVE_GCC_INLINE_ASM',
  cc.compiles(
    gcc_inline_asm,
    name: 'gcc_inline_asm',
  ),
)

msvc_intrinsics_x64 = '''
#include <intrin.h>
int main() {
    unsigned __int64 a = 0x0fffffffffffffffI64;
    unsigned __int64 b = 0xf0000000I64;
    unsigned __int64 c, d;
    d = _umul128(a, b, &c);
    return 0;
}
'''

cfg_data.set(
  'AWS_HAVE_MSVC_INTRINSICS_X64',
  cc.links(
    msvc_intrinsics_x64,
    name: 'msvc_intrinsics_x64',
  ),
)
cfg_data.set('AWS_HAVE_POSIX_LARGE_FILE_SUPPORT', true)
cfg_data.set(
  'AWS_HAVE_EXECINFO',
  cc.has_function(
    'backtrace',
    prefix: '#include <execinfo.h>',
  ),
)

winapi_desktop = '''
#include <windows.h>
#if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
int main() {
    return 0;
}
#else
it's not windows desktop
#endif
'''

cfg_data.set(
  'AWS_HAVE_WINAPI_DESKTOP',
  cc.compiles(
    winapi_desktop,
    name: 'winapi_desktop',
  ),
)
cfg_data.set('AWS_HAVE_LINUX_IF_LINK_H', cc.has_header('linux/if_link.h'))

avx2_intrinsics = '''
#include <immintrin.h>
#include <emmintrin.h>
#include <string.h>

int main() {
    __m256i vec;
    memset(&vec, 0, sizeof(vec));

    _mm256_shuffle_epi8(vec, vec);
    _mm256_set_epi32(1,2,3,4,5,6,7,8);
    _mm256_permutevar8x32_epi32(vec, vec);

    return 0;
}
'''

cfg_data.set(
  'AWS_HAVE_AVX2_INTRINSICS',
  cc.links(
    avx2_intrinsics,
    name: 'avx2_intrinsics',
  ),
)

avx512_intrinsics = '''
#include <immintrin.h>

int main() {
    __m512 a = _mm512_setzero_ps();
    return 0;
}
'''

cfg_data.set(
  'AWS_HAVE_AVX512_INTRINSICS',
  cc.links(
    avx512_intrinsics,
    name: 'avx512_intrinsics',
  ),
)

mm256_extract_epi64 = '''
#include <immintrin.h>
#include <string.h>

int main() {
    __m256i vec;
    memset(&vec, 0, sizeof(vec));
    return (int)_mm256_extract_epi64(vec, 2);
}
'''

cfg_data.set(
  'AWS_HAVE_MM256_EXTRACT_EPI64',
  cc.links(
    mm256_extract_epi64,
    name: 'mm256_extract_epi64',
  ),
)

clmul = '''
#include <wmmintrin.h>
#include <emmintrin.h>
int main() {
    __m128i a = _mm_setzero_si128();
    __m128i b = _mm_setzero_si128();
    __m128i result = _mm_clmulepi64_si128(a, b, 0x00);
    (void)result;
    return 0;
}
'''

cfg_data.set(
  'AWS_HAVE_CLMUL',
  cc.links(
    clmul,
    name: 'clmul',
  ),
)

arm32_crc = '''
#include <arm_acle.h>
int main() {
    int crc = __crc32d(0, 1);
    return 0;
}
'''

cfg_data.set(
  'AWS_HAVE_ARM32_CRC',
  cc.links(
    arm32_crc,
    name: 'arm32_crc',
  ),
)

armv8_1 = '''
#include <stdatomic.h>
int main() {
    _Atomic int var = 0;
    atomic_fetch_add_explicit(&var, 1, memory_order_relaxed);
    return 0;
}
'''

cfg_data.set(
  'AWS_HAVE_ARMv8_1',
  cc.links(
    armv8_1,
    name: 'armv8_1',
  ),
)

cfg_data.set('AWS_ARCH_INTEL', host_machine.cpu_family() in ['x86', 'x86_64'])
cfg_data.set('AWS_ARCH_INTEL64', host_machine.cpu_family() == 'x86_64')

cfg_data.set('AWS_ARCH_ARM64', host_machine.cpu_family() == 'aarch64')

configure_file(
  input: 'config.h.in',
  output: 'config.h',
  configuration: cfg_data,
  install: true,
  install_dir: get_option('includedir') / 'aws/common',
  format: 'cmake',
)
headers = [
  'allocator.h',
  'array_list.h',
  'array_list.inl',
  'assert.h',
  'atomics.h',
  'atomics.inl',
  'atomics_fallback.inl',
  'atomics_gnu.inl',
  'atomics_gnu_old.inl',
  'atomics_msvc.inl',
  'byte_buf.h',
  'byte_order.h',
  'byte_order.inl',
  'cache.h',
  'cbor.h',
  'clock.h',
  'clock.inl',
  'command_line_parser.h',
  'common.h',
  'condition_variable.h',
  'config.h.in',
  'cpuid.h',
  'cross_process_lock.h',
  'date_time.h',
  'device_random.h',
  'encoding.h',
  'encoding.inl',
  'environment.h',
  'error.h',
  'error.inl',
  'exports.h',
  'fifo_cache.h',
  'file.h',
  'hash_table.h',
  'host_utils.h',
  'json.h',
  'lifo_cache.h',
  'linked_hash_table.h',
  'linked_list.h',
  'linked_list.inl',
  'log_channel.h',
  'log_formatter.h',
  'log_writer.h',
  'logging.h',
  'lru_cache.h',
  'macros.h',
  'math.cbmc.inl',
  'math.fallback.inl',
  'math.gcc_arm64_asm.inl',
  'math.gcc_builtin.inl',
  'math.gcc_overflow.inl',
  'math.gcc_x64_asm.inl',
  'math.h',
  'math.inl',
  'math.msvc_x64.inl',
  'mutex.h',
  'package.h',
  'platform.h',
  'posix/common.inl',
  'predicates.h',
  'priority_queue.h',
  'private/array_list.h',
  'private/byte_buf.h',
  'private/dlloads.h',
  'private/external_module_impl.h',
  'private/hash_table_impl.h',
  'private/lookup3.inl',
  'private/system_info_priv.h',
  'private/thread_shared.h',
  'private/xml_parser_impl.h',
  'process.h',
  'ref_count.h',
  'ring_buffer.h',
  'ring_buffer.inl',
  'rw_lock.h',
  'shutdown_types.h',
  'statistics.h',
  'stdbool.h',
  'stdint.h',
  'string.h',
  'string.inl',
  'system_info.h',
  'system_resource_util.h',
  'task_scheduler.h',
  'thread.h',
  'thread_scheduler.h',
  'time.h',
  'uri.h',
  'uuid.h',
  'xml_parser.h',
  'zero.h',
  'zero.inl',
]

install_headers(
  headers,
  preserve_path: true,
  install_dir: get_option('includedir') / 'aws/common',
)
