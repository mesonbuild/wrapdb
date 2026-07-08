project(
  'openssl',
  'c',
  version: '3.0.17',
  license: 'Apache-2.0',
  meson_version: '>= 0.64',
  default_options: ['warning_level=1'],
)

# Make sure to generate configs in case they are not already
fs = import('fs')
if not fs.exists('generated-config')
  message('Generating OpenSSL configs...')
  env = environment()
  env.set('NODE_VERSION', 'v22.18.0')
  env.set('OPENSSL_VERSION', meson.project_version())
  bash = find_program('bash')
  run_command(
    bash,
    'generator.sh',
    check: true,
    env: env,
  )
endif

include_directories = [
  'include',
  'crypto',
  'crypto/modes',
  'crypto/ec/curve448',
  'crypto/ec/curve448/arch_32',
  'providers/common/include',
  'providers/implementations/include',
]

compiler = meson.get_compiler('c')

dependencies = [
  # TODO: Make this optionally added once we have threading configurable via options
  dependency('threads'),
]
defines = [
  # Compile out hardware engines. Most are stubs that dynamically load
  # the real driver but that poses a security liability when an attacker
  # is able to create a malicious DLL in one of the default search paths.
  'OPENSSL_NO_HW',
]
c_args = []

asm_opt = get_option('asm')

if asm_opt.disabled()
  new_gas_or_nasm = false
else
  # See openssl.gyp, openssl-fipsmodule target
  new_gas = find_program(
    'as',
    required: false,
    version: '>=2.26',
  )
  new_asm = find_program(
    'nasm',
    required: false,
    version: '>=2.11.8',
  )
  new_gas_or_nasm = (new_gas.found() or
  new_asm.found()
)
endif

is_msvc_like = ['msvc', 'clang-cl'].contains(compiler.get_id())
is_bsd = host_machine.system() in ['dragonfly', 'freebsd', 'netbsd', 'openbsd']
is_darwin = host_machine.system() == 'darwin'
is_linux = host_machine.system() in ['linux', 'android']
is_sunos = host_machine.system() == 'sunos'
is_windows = host_machine.system() == 'windows'

is_x86 = host_machine.cpu_family() == 'x86'
is_x86_64 = host_machine.cpu_family() == 'x86_64'
is_aarch64 = host_machine.cpu_family() == 'aarch64'
is_mips64 = host_machine.cpu_family() == 'mips64'
is_s390x = host_machine.cpu_family() == 's390x'
is_arm = host_machine.cpu_family() == 'arm'
is_ppc64 = host_machine.cpu_family() == 'ppc64'
is_riskv64 = host_machine.cpu_family() == 'riscv64'

if new_gas_or_nasm
  asm = 'asm'

  # Require AVX512IFMA supported. See
  # https://www.openssl.org/docs/man1.1.1/man3/OPENSSL_ia32cap.html
  # Currently crypto/poly1305/asm/poly1305-x86_64.pl requires AVX512IFMA.
  if host_machine.cpu_family() == 'ppc' and host_machine.system() == 'linux'
    arch_subdir = 'linux-ppc'
  elif host_machine.cpu_family() == 'ppc64' and host_machine.system() == 'linux' and host_machine.endian() == 'little'
    arch_subdir = 'linux-ppc64le'
  elif host_machine.cpu_family() == 'ppc64' and host_machine.system() == 'linux'
    arch_subdir = 'linux-ppc64'
  elif host_machine.cpu_family() == 's390x' and host_machine.system() == 'linux'
    arch_subdir = 'linux64-s390x'
  elif host_machine.cpu_family() == 'arm' and host_machine.system() in [
    'linux',
    'android',
  ]
    arch_subdir = 'linux-armv4'
  elif host_machine.cpu_family() == 'aarch64' and host_machine.system() in [
    'linux',
    'android',
  ]
    arch_subdir = 'linux-aarch64'
  elif host_machine.cpu_family() == 'x86' and host_machine.system() in [
    'dragonfly',
    'freebsd',
    'netbsd',
    'openbsd',
  ]
    arch_subdir = 'BSD-x86'
  elif host_machine.cpu_family() == 'x86' and host_machine.system() in [
    'linux',
    'android',
  ]
    arch_subdir = 'linux-elf'
  elif host_machine.cpu_family() == 'x86' and host_machine.system() == 'darwin'
    arch_subdir = 'darwin-i386-cc'
  elif host_machine.cpu_family() == 'x86' and host_machine.system() == 'sunos'
    arch_subdir = 'solaris-x86-gcc'
  elif host_machine.cpu_family() == 'x86' and host_machine.system() == 'windows'
    if is_msvc_like
      if new_asm.found()
        arch_subdir = 'VC-WIN32'
      else
        asm = 'no_asm'
      endif
    else
      arch_subdir = 'mingw'
    endif
  elif host_machine.cpu_family() == 'x86_64' and host_machine.system() in [
    'dragonfly',
    'freebsd',
    'netbsd',
    'openbsd',
  ]
    arch_subdir = 'BSD-x86_64'
  elif host_machine.cpu_family() == 'x86_64' and host_machine.system() == 'darwin'
    arch_subdir = 'darwin64-x86_64-cc'
  elif host_machine.cpu_family() == 'aarch64' and host_machine.system() == 'darwin'
    arch_subdir = 'darwin64-arm64-cc'
  elif host_machine.cpu_family() == 'x86_64' and host_machine.system() == 'sunos'
    arch_subdir = 'solaris64-x86_64-gcc'
  elif host_machine.cpu_family() == 'x86_64' and host_machine.system() == 'windows'
    if is_msvc_like
      if new_asm.found()
        arch_subdir = 'VC-WIN64A'
      else
        asm = 'no_asm'
      endif
    else
      arch_subdir = 'mingw64'
    endif
  elif host_machine.cpu_family() == 'x86_64' and host_machine.system() in [
    'linux',
    'android',
  ]
    arch_subdir = 'linux-x86_64'
  elif host_machine.cpu_family() == 'mips64' and host_machine.system() == 'linux'
    arch_subdir = 'linux64-mips64'
  else
    asm = 'no-asm'
  endif
elif asm_opt.enabled()
  error(
    'Neither GNU Assembler nor Netwide Assembler were found, cannot use use "asm=enabled" option',
  )
else
  asm = 'no-asm'
endif

if asm == 'no-asm'
  defines += ['OPENSSL_NO_ASM']
  if host_machine.cpu_family() == 'ppc' and host_machine.system() == 'linux'
    arch_subdir = 'linux-ppc'
  elif host_machine.cpu_family() == 'ppc64' and host_machine.system() == 'linux' and host_machine.endian() == 'little'
    arch_subdir = 'linux-ppc64le'
  elif host_machine.cpu_family() == 'ppc64' and host_machine.system() == 'linux'
    arch_subdir = 'linux-ppc64'
  elif host_machine.cpu_family() == 's390x' and host_machine.system() == 'linux'
    arch_subdir = 'linux64-s390x'
  elif host_machine.cpu_family() == 'arm' and host_machine.system() in [
    'linux',
    'android',
  ]
    arch_subdir = 'linux-armv4'
  elif host_machine.cpu_family() == 'aarch64' and host_machine.system() in [
    'linux',
    'android',
  ]
    arch_subdir = 'linux-aarch64'
  elif host_machine.cpu_family() == 'x86' and host_machine.system() in [
    'dragonfly',
    'freebsd',
    'netbsd',
    'openbsd',
  ]
    arch_subdir = 'BSD-x86'
  elif host_machine.cpu_family() == 'x86' and host_machine.system() in [
    'linux',
    'android',
  ]
    arch_subdir = 'linux-elf'
  elif host_machine.cpu_family() == 'x86' and host_machine.system() == 'darwin'
    arch_subdir = 'darwin-i386-cc'
  elif host_machine.cpu_family() == 'x86' and host_machine.system() == 'sunos'
    arch_subdir = 'solaris-x86-gcc'
  elif host_machine.cpu_family() == 'x86' and host_machine.system() == 'windows'
    if is_msvc_like
      arch_subdir = 'VC-WIN32'
    else
      arch_subdir = 'mingw'
    endif
  elif host_machine.cpu_family() == 'x86_64' and host_machine.system() in [
    'dragonfly',
    'freebsd',
    'netbsd',
    'openbsd',
  ]
    arch_subdir = 'BSD-x86_64'
  elif host_machine.cpu_family() == 'x86_64' and host_machine.system() == 'darwin'
    arch_subdir = 'darwin64-x86_64-cc'
  elif host_machine.cpu_family() == 'aarch64' and host_machine.system() == 'darwin'
    arch_subdir = 'darwin64-arm64-cc'
  elif host_machine.cpu_family() == 'x86_64' and host_machine.system() == 'sunos'
    arch_subdir = 'solaris64-x86_64-gcc'
  elif host_machine.cpu_family() == 'x86_64' and host_machine.system() == 'windows'
    if is_msvc_like
      arch_subdir = 'VC-WIN64A'
    else
      arch_subdir = 'mingw64'
    endif
  elif host_machine.cpu_family() == 'aarch64' and host_machine.system() == 'windows'
    arch_subdir = 'VC-WIN64-ARM'
  elif host_machine.cpu_family() == 'x86_64' and host_machine.system() == 'linux'
    arch_subdir = 'linux-x86_64'
  elif host_machine.cpu_family() == 'mips64' and host_machine.system() == 'linux'
    arch_subdir = 'linux64-mips64'
  else
    error(
      'Unsupported arch+OS combo: ' + host_machine.cpu_family() + ' + ' + host_machine.system(),
    )
  endif

  message('OpenSSL is configured without ASM support')
else
  message('OpenSSL is configured with ASM support')
endif

subdir('generated-config/archs' / arch_subdir / asm)

if asm != 'no-asm'
  if is_msvc_like
    add_languages(
      'nasm',
      required: true,
    )
  endif
  libcrypto_sources += libcrypto_asm
endif

windows = import('windows')

if host_machine.system() == 'windows'
  if libcrypto_rc != ''
    libcrypto_sources += windows.compile_resources(libcrypto_rc)
  endif
  if libssl_rc != ''
    libssl_sources += windows.compile_resources(libssl_rc)
  endif
endif

# Build options specific to OS, engines are disabled on purpose for the same reasons as `OPENSSL_NO_HW` above
if is_windows
  defines += [
    ## default of Win. See INSTALL in openssl repo.
    'OPENSSLDIR="C:\\Program Files\\Common Files\\SSL"',
    'ENGINESDIR="NUL"',
    'OPENSSL_SYS_WIN32',
    'WIN32_LEAN_AND_MEAN',
    'L_ENDIAN',
    '_CRT_SECURE_NO_DEPRECATE',
    'UNICODE',
    '_UNICODE',
  ]
  if compiler.get_id() == 'msvc'
    c_args += ['-wd4090', '-Gs0', '-GF', '-Gy', '-nologo']
  elif compiler.get_id() == 'clang'
    c_args += [
      # Silence the defines coming from the architecture folders.
      '-Wno-unused-command-line-argument',
    ]
  endif
elif is_darwin
  defines += [
    'OPENSSLDIR="/System/Library/OpenSSL/"',
    'ENGINESDIR="/dev/null"',
    'MODULESDIR="/dev/null"',
  ]
  c_args += [
    '-Wno-missing-field-initializers',
    '-Wno-unused-command-line-argument',
  ]
elif is_sunos
  defines += [
    'OPENSSLDIR="/etc/ssl"',
    'ENGINESDIR="/dev/null"',
    'MODULESDIR="/dev/null"',
    '__EXTENSIONS__',
  ]
else
  # Linux and others
  defines += [
    'OPENSSLDIR="/etc/ssl"',
    'ENGINESDIR="/dev/null"',
    'MODULESDIR="/dev/null"',
  ]
  c_args += ['-Wno-missing-field-initializers']
  if compiler.get_id() != 'clang'
    c_args += ['-Wno-old-style-declaration']
  else
    c_args += ['-Wno-unused-command-line-argument']
  endif
endif

foreach library : openssl_libraries
  # MSVC fails with "ERROR: C static library 'ws2_32' not found" when `static` is specified at all
  if host_machine.system() == 'windows'
    dependencies += [compiler.find_library(library)]
  else
    dependencies += [
      compiler.find_library(
        library,
        static: get_option('default_library') == 'static',
      ),
    ]
  endif
endforeach

# We may need to add some defines for static builds
if get_option('default_library') == 'static'
  defines += [
    'OSSL_CRYPTO_DSO_CONF_H',
    'DSO_NONE',
    'DSO_EXTENSION=".so"',
    'OPENSSL_NO_DSO',
  ]
endif

foreach define : defines + openssl_defines
  c_args += ['-D' + define]
endforeach

c_args += openssl_cflags

include_directories += openssl_include_directories

openssl_library_version = meson.project_version().substring(0, -1)

version_components = openssl_library_version.split('.')

openssl_so_version = '.'.join([version_components[0], version_components[1]])

if is_msvc_like
  openssl_library_prefix = 'lib'
else
  openssl_library_prefix = []
endif

if is_msvc_like
  msvc_version = compiler.get_define('_MSC_VER')
  # Block build if the linker gets a renaming directive.
  if msvc_version.version_compare('>=1930')
    link_args = ['/WX:4070']
  else
    link_args = ['/WX']
  endif
else
  link_args = []
endif

libcrypto_lib = library(
  'crypto',
  dependencies: dependencies,
  sources: libcrypto_sources,
  include_directories: include_directories,
  c_args: c_args,
  link_args: link_args,
  name_prefix: openssl_library_prefix,
  version: openssl_library_version,
  soversion: openssl_so_version,
  vs_module_defs: 'crypto.def',
  install: true,
)

libcrypto_dep = declare_dependency(
  include_directories: include_directories,
  dependencies: dependencies,
  link_with: libcrypto_lib,
)

libssl_lib = library(
  'ssl',
  dependencies: dependencies + [libcrypto_dep],
  sources: libssl_sources,
  include_directories: include_directories,
  c_args: c_args,
  link_args: link_args,
  name_prefix: openssl_library_prefix,
  version: openssl_library_version,
  soversion: openssl_so_version,
  vs_module_defs: 'ssl.def',
  install: true,
)

libssl_dep = declare_dependency(
  include_directories: include_directories,
  dependencies: dependencies + [libcrypto_dep],
  link_with: libssl_lib,
)

openssl_dep = declare_dependency(
  dependencies: [libcrypto_dep, libssl_dep],
)

openssl_cli_directories = include_directories + ['apps/include']

cli_opt = get_option('build_cli')

openssl_cli = executable(
  'openssl',
  build_by_default: cli_opt,
  dependencies: dependencies + [openssl_dep],
  sources: openssl_cli_sources,
  include_directories: openssl_cli_directories,
  c_args: c_args,
  install: cli_opt,
)

install_headers(
  openssl_headers + openssl_arch_headers,
  subdir: 'openssl',
)

pkg = import('pkgconfig')
openssl_pc = pkg.generate(
  name: 'OpenSSL',
  description: 'Secure Sockets Layer and cryptography libraries and tools',
  libraries: [libssl_lib, libcrypto_lib],
)

python3 = import('python').find_installation()


headers = run_command(
  python3,
  '-c',
  '''import sys
from pathlib import Path
srcdir = Path(sys.argv[1])
headers = list(f for f in Path(srcdir, 'include', 'openssl').glob('*.h') if not f.name.startswith('__DECC_'))
for p in headers:
  print(p.relative_to(srcdir).as_posix())
genasmdir = Path(sys.argv[2])
headers = list(f for f in Path(genasmdir, 'include', 'openssl').glob('*.h'))
for p in headers:
  print(p.relative_to(srcdir).as_posix())
''',
  meson.current_source_dir(),
  meson.current_source_dir() / 'generated-config/archs' / arch_subdir / asm,
  check: true,
  capture: true,
).stdout().strip().split('\n')

install_headers(
  headers,
  subdir: 'openssl',
)
