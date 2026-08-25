project(
    'readcon-core',
    'c',
    version: '0.14.8',
    meson_version: '>=1.3.0',
    default_options: [
        'buildtype=debugoptimized',
        'warning_level=3',
        'c_std=c99',
        'b_ndebug=if-release',
    ],
    license: 'MIT',
)

# Shipped C/C++ headers. cbindgen is maintainer-only
# (scripts/regen-capi-headers.sh); wrap and FetchContent consumers never run it.
fs = import('fs')
_msproot = meson.project_source_root()
_mbproot = meson.project_build_root()
_incdir = include_directories('include')

if not fs.is_file(_msproot / 'include' / 'readcon-core.h')
    error(
        'missing shipped header include/readcon-core.h; maintainers run scripts/regen-capi-headers.sh',
    )
endif

cc = meson.get_compiler('c')
cargo_prog = find_program('cargo', required: true)
rustc_prog = find_program('rustc', required: true)
_py = find_program('python3', 'python')
_rv = run_command(rustc_prog, '--version', check: false)
if _rv.returncode() != 0
    # wrapdb qemu Alpine loongarch64/riscv64: rustc --version SIGABRT (scudo).
    # wrapdb treats this exact phrase as an architecture skip.
    error('unsupported architecture')
endif
_rv_bits = _rv.stdout().strip().split()
if _rv_bits.length() < 2 or not _rv_bits[1].version_compare('>= 1.88.0')
    error('readcon-core requires rustc >= 1.88.0')
endif

_rust_sys_deps = []
if host_machine.system() == 'linux'
    _rust_sys_deps += [
        dependency('threads'),
        cc.find_library('dl', required: true),
        cc.find_library('m', required: true),
    ]
elif host_machine.system() == 'darwin'
    _rust_sys_deps += [dependency('threads')]
elif host_machine.system() == 'windows'
    _rust_sys_deps += [
        cc.find_library('ws2_32', required: true),
        cc.find_library('userenv', required: true),
        cc.find_library('bcrypt', required: true),
        cc.find_library('ntdll', required: true),
    ]
endif

if host_machine.system() == 'windows'
    _cargo_shared = 'readcon_core.dll'
    if cc.get_argument_syntax() == 'msvc'
        _cargo_static = 'readcon_core.lib'
    else
        _cargo_static = 'libreadcon_core.a'
    endif
else
    _so = host_machine.system() == 'darwin' ? '.dylib' : '.so'
    _cargo_shared = 'libreadcon_core' + _so
    _cargo_static = 'libreadcon_core.a'
endif

_profile = get_option('buildtype') == 'debug' ? 'debug' : 'release'

_src_rs = run_command(
    _py,
    '-c',
    'from pathlib import Path; print("\\n".join(str(p) for p in sorted(Path("src").rglob("*.rs"))))',
    check: true,
).stdout().strip().split('\n')

readcon_cargo = custom_target(
    'readcon-cargo',
    input: files('Cargo.toml', 'src/lib.rs'),
    depend_files: files('Cargo.lock', 'build.rs') + files(_src_rs),
    output: [_cargo_shared, _cargo_static],
    command: [
        _py,
        files('scripts/meson_cargo_build.py'),
        cargo_prog.full_path(),
        _msproot,
        _mbproot / 'cargo-target',
        _profile,
        _cargo_shared,
        _cargo_static,
        '@OUTPUT0@',
        '@OUTPUT1@',
        get_option('cargo_features'),
    ],
    build_by_default: true,
    install: true,
    install_dir: [get_option('libdir'), get_option('libdir')],
)

install_headers(
    'include/readcon-core.h',
    'include/readcon-core.hpp',
    'include/readcon-metatensor.h',
)

# link_args + sources: Meson must not promote an installed static consumer
# to link_whole (custom_target is not a library target).
_link_idx = get_option('default_library') == 'static' ? 1 : 0
readcon_dep = declare_dependency(
    link_args: [readcon_cargo[_link_idx].full_path()],
    sources: readcon_cargo,
    dependencies: _rust_sys_deps,
    include_directories: _incdir,
    version: meson.project_version(),
)
meson.override_dependency('readcon-core', readcon_dep)

if get_option('with_tests')
    test(
        'cargo-tests',
        cargo_prog,
        args: ['test', '--manifest-path', _msproot / 'Cargo.toml', '--locked'],
        timeout: 300,
    )
    c_golden = executable(
        'test_conformance_goldens',
        files('tests/c/test_conformance_goldens.c'),
        dependencies: readcon_dep,
        include_directories: _incdir,
        build_rpath: meson.project_build_root(),
    )
    test(
        'c-conformance-goldens',
        c_golden,
        args: [_msproot],
        env: {
            'READCON_CORE_ROOT': _msproot,
            'LD_LIBRARY_PATH': meson.project_build_root(),
        },
        timeout: 120,
    )
endif

if get_option('with_examples')
    subdir('examples')
endif

pkg = import('pkgconfig')
pkg.generate(
    name: 'readcon-core',
    filebase: 'readcon-core',
    description: 'CON/convel file reader and writer with FFI, Python, Julia bindings',
    version: meson.project_version(),
    # Raw `-lfoo` strings do not get `-L${libdir}`; wrap consumers then
    # fail at link with "cannot find -lreadcon_core".
    libraries: ['-L${libdir}', '-lreadcon_core'],
    url: 'https://github.com/lode-org/readcon-core',
)
