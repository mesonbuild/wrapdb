#!/usr/bin/env python3

import os
import subprocess
import json
import shutil
import textwrap
import argparse
import tempfile

from pathlib import Path

ASMS = ['asm', 'asm_avx2', 'no-asm']

ASM_ARCHS = [
    # aix is not supported by Meson
    #'aix-gcc',
    #'aix64-gcc',
    'BSD-x86',
    'BSD-x86_64',
    'darwin64-x86_64-cc',
    'darwin-i386-cc',
    'darwin64-arm64-cc',
    'linux-aarch64',
    'linux-armv4',
    'linux-elf',
    'linux-x86_64',
    'linux-ppc',
    'linux-ppc64',
    'linux-ppc64le',
    'linux64-s390x',
    'linux64-mips64',
    'solaris-x86-gcc',
    'solaris64-x86_64-gcc',
    'VC-WIN64A',
    'VC-WIN32',
]

NO_ASM_ARCHS = [
    'VC-WIN64-ARM',
]

COPTS = ['no-comp']


def gen_arch(outdir, arch, asm):
    # Windows archs can only be generated on Windows with nmake instead of GNU make.
    is_win = arch.startswith('VC-WIN')
    make = 'nmake' if is_win else 'make'
    if not shutil.which(make):
        print(f'{make} not found, cannot generate for arch {arch}')
        return

    # Configure OpenSSL for this arch
    cmd = ['perl', 'Configure'] + COPTS + [arch]
    env = os.environ.copy()
    env['CONFIGURE_CHECKER_WARN'] = '1'
    env['CC'] = 'gcc'
    if asm == 'no-asm':
        cmd.append(asm)
    elif asm == 'asm_avx2':
        env['CC'] = 'fake_gcc.py'
    subprocess.check_call(cmd, env=env)

    # Convert configdata.pm to json, then load it in python
    def configdata(varname):
        code = f'print encode_json(\%{varname});'
        stdout = subprocess.check_output(['perl', '-MJSON', '-I.', '-Mconfigdata', '-e', code])
        return json.loads(stdout)
    unified_info = configdata('unified_info')
    target = configdata('target')

    rel_base_dir = Path('generated-config', 'archs', arch, asm)
    base_dir = Path(outdir, rel_base_dir)

    # Generate a target and copy it into outdir
    env = os.environ.copy()
    env['CC'] = 'gcc'
    env['ASM'] = 'nasm'
    def _generate(target):
        subprocess.check_call([make, target], env=env)
        dest = Path(base_dir, target)
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(target, dest)

    # Generate common dependencies
    for d in unified_info['depends']['']:
        if d in unified_info['generate']:
            _generate(d)

    class Target:
        def __init__(self, name):
            self.name = name
            self.includes = unified_info['includes'].get(name, [])
            self.defines = unified_info['defines'].get(name, []) + target['defines']
            self.sources = set()
            self.winres = set()
            self.windef = ''
            self.ld_script = ''
            self._add_sources(name, set())

        # Recursively collect all source files. It does not build intermediary
        # static libraries.
        def _add_sources(self, target, visited):
            if target in visited:
                return
            visited.add(target)

            # Those are shared libraries, only add its sources if it's outself.
            if '.' not in target and target != self.name:
                return

            if target in unified_info['generate']:
                # On Windows configdata.pm seems to be using unix filenames
                # which don't match nmake target name.
                if is_win and target.lower().endswith('.s'):
                    target = target[:-2] + '.asm'
                if is_win and target.lower().endswith('.ld'):
                    target = target[:-3] + '.def'
                _generate(target)
                self._add_target(Path(rel_base_dir, target).as_posix())
                return

            for d in unified_info['depends'].get(target, []):
                self._add_sources(d, visited)

            sources = unified_info['sources'].get(target, [])
            sources += unified_info['shared_sources'].get(target, [])
            if sources:
                for src in sources:
                    self._add_sources(src, visited)
            else:
                self._add_target(target)

        def _add_target(self, target):
            if any(target.endswith(i) for i in ('.c', '.s', '.S', '.asm')):
                self.sources.add(target)
            elif target.endswith('.rc') or target.endswith('.res'):
                self.winres.add(target)
            elif target.endswith('.ld'):
                self.ld_script = target
            elif target.endswith('.def'):
                self.windef = target
            elif target.endswith('.h'):
                pass
            else:
                raise Exception('Unexpected target type: ' + target)

    libraries = []
    for lib in target.get('ex_libs', '').split():
        if not lib or lib == '-pthread':
            continue
        if lib.startswith('-l'):
            lib = lib[2:]
        if lib.endswith('.lib'):
            lib = lib[:-4]
        libraries.append(lib)

    def write_list(f, name, items, paths=False):
        if paths and is_win:
            items = [Path(i).as_posix() for i in items]
        f.write(f'{name} = [\n')
        for i in items:
            f.write(f'  {i!r},\n')
        f.write(']\n')

    base_dir.mkdir(parents=True, exist_ok=True)
    with Path(base_dir, 'meson.build').open('w', encoding='utf-8') as f:
        write_list(f, f'openssl_libraries', libraries)
        for name in ['libcrypto', 'libssl', os.path.join('apps', 'openssl')]:
            t = Target(name)
            includes = []
            for i in t.includes:
                includes.append(i)
                if Path(base_dir, i).exists():
                    includes.append(Path(rel_base_dir, i).as_posix())
            includes.append(Path(rel_base_dir, 'crypto').as_posix())
            includes.append(Path(rel_base_dir, 'apps').as_posix())
            cargs = [f'-D{i}' for i in t.defines]
            basename = os.path.basename(name)
            write_list(f, f'{basename}_sources', t.sources, paths=True)
            write_list(f, f'{basename}_includes', includes, paths=True)
            write_list(f, f'{basename}_c_args', cargs)
            write_list(f, f'{basename}_winres', t.winres, paths=True)
            link_args = f'-Wl,--version-script,{outdir / t.ld_script}' if t.ld_script else ''
            f.write(f'{basename}_link_args = {link_args!r}\n')
            f.write(f'{basename}_vs_module_defs = {t.windef!r}\n')

    # Cleanup
    subprocess.check_call([make, 'clean'])
    subprocess.check_call([make, 'distclean'])

def run():
    parser = argparse.ArgumentParser(description='OpenSSL arch generator.')
    parser.add_argument('outdir', nargs='?', default='.', type=Path)
    parser.add_argument('--arch', choices=ASM_ARCHS + NO_ASM_ARCHS)
    parser.add_argument('--asm', choices=ASMS)
    args = parser.parse_args()

    # By default gen all asm for all archs, unless specific asm/arch is specified.
    gen_archs = ASM_ARCHS
    gen_asms = ASMS
    if args.arch is not None:
        gen_archs = [args.arch]
    if args.asm is not None:
        if args.arch in NO_ASM_ARCHS and args.asm != 'no-asm':
            raise Exception(f'ASM {args.asm} not supported for arch {arg.arch}.')
        gen_asms = [args.asm]

    for arch in gen_archs:
        for asm in gen_asms:
            if arch in NO_ASM_ARCHS and asm != 'no-asm':
                continue
            gen_arch(args.outdir.resolve(), arch, asm)

    return 0

if __name__ == '__main__':
    exit(run())
