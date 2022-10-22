project(
    'uchardet',
    ['c', 'cpp'],
    version: '0.0.7',
    license: ['MPL-1.1', 'GPL-2.0-or-later', '  LGPL-2.1-or-later'],
    meson_version: '>=0.53.0',
    default_options: ['cpp_std=c++14'],
)

base_cpp_args = []

cxx = meson.get_compiler('cpp')
host_cpu_family = host_machine.cpu_family()

use_sse2 = not get_option('use_sse2').disabled()

# these cppflags only make sense on the x86 architecture
# and are only available on gcc and toolchains that copy gcc's behavior
if (host_cpu_family == 'x86_64' or host_cpu_family == 'x86') and cxx.get_id() != 'msvc'
    supports_cflag_sse2 = cxx.has_argument('-msse2')
    supports_cflag_sse_math = cxx.has_argument('-mfpmath=sse')
    if use_sse2 and supports_cflag_sse2 and supports_cflag_sse_math
        base_cpp_args += ['-msse2', '-mfpmath=sse']
    else
        base_cpp_args += '-ffloat-store'
    endif
endif

subdir('src')
subdir('test')
