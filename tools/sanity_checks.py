#!/usr/bin/env python3

# Copyright 2021 Xavier Claessens <xclaesse@gmail.com>

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest
import json
import subprocess
import configparser
import re
import typing as T
import os
import tempfile
import platform
import io
import sys
import shlex

from pathlib import Path
from utils import Version, ci_group, is_ci, is_alpinelike, is_debianlike, is_linux, is_macos, is_windows, is_msys

PERMITTED_FILES = ['generator.sh', 'meson.build', 'meson_options.txt', 'meson.options', 'LICENSE.build']
PER_PROJECT_PERMITTED_FILES = {
    'box2d': [
        'doctest.h'
    ],
    'bzip2': [
        'test.py',
    ],
    'curl': [
        'buildinfo.txt.meson',
        'extract.mk',
        'rewrite.mk',
    ],
    'glbinding': [
        'pch.h',
        'glbinding_api.h',
        'glbinding_features.h',
        'glbinding_export.h',
        'glbinding-aux_api.h',
        'glbinding-aux_features.h',
        'glbinding-aux_export.h'
    ],
    'godot-cpp' : [
         'meson-bindings-generator.py',
     ],
    'gumbo-parser': [
        'tokenizer.cc',
    ],
    'icu': [
        'export_module.py'
    ],
    'lame': [
        'fix_def.py',
    ],
    'libexif': [
        'def.py',
    ],
    'm4': [
        'm4_test_runner.py',
    ],
    'mpdecimal': [
        'gettests.py',
    ],
    'nowide': [
        'test_iostream_interactive.py',
    ],
    'openssl': [
        'bn_conf.h',
        'dso_conf.h',
        'buildinf.h',
        'generate_def.py',
        'generate_gypi.pl.patch',
        'meson.build.tmpl',
        'README.md',
    ],
    'openal-soft': [
        'hexify.py'
    ],
    'openblas': [
        'gen_install_headers.py',
        'prepare_config_last.py',
        'read_config.py',
        'write_to_file.py',
        'test_runner.c',
        'run_fortran.c',
    ],
    'protobuf': [
        'symlink.py',
    ],
    'sdl2': [
        'find-dylib-name.py'
    ],
    'soundtouch': [
        'afxres.h'
    ],
    'taglib': [
        'checked.h'
    ],
    'theora': [
        'check-needed-tex-packages.py',
        'latexmk-wrapper.py',
        'test-tex-packages.py',
        'doxyfile-patcher.py',
        'arm2gnu-wrapper.py',
        'generate_windows_rc.py',
    ],
    'libcap': [
        'gen_cap_names.py',
    ],
    'libffi': [
        'test-cc-supports-hidden-visibility.py',
        'test-ro-eh-frame.py',
        'test-cc-uses-zarch.py',
        'test-unwind-section.py',
        'extract-libtool-version.py',
    ],
    'leptonica': [
        '_skipped_test.c',
    ],
    'libuv': [
        'link_file_in_build_dir.py',
    ],
    'luajit': [
        'unwind_check.sh',
    ],
    'vo-aacenc': [
        'makedef.py',
        'stddef.h.in',
    ],
    'zlib-ng': [
        'get-version.py',
        'process-zconf.py',
    ],
}
FORMAT_CHECK_FILES = ['meson.build', 'meson_options.txt', 'meson.options']
NO_TABS_FILES = ['meson.build', 'meson_options.txt', 'meson.options']
PERMITTED_KEYS = {'versions', 'dependency_names', 'program_names'}


class TestReleases(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Take list of git tags
        stdout = subprocess.check_output(['git', 'tag'])
        cls.tags = [t.strip() for t in stdout.decode().splitlines()]

        try:
            fn = 'releases.json'
            with open(fn, 'r', encoding='utf-8') as f:
                cls.releases = json.load(f)
            fn = 'ci_config.json'
            with open(fn, 'r', encoding='utf-8') as f:
                cls.ci_config = json.load(f)
        except json.decoder.JSONDecodeError:
            raise RuntimeError(f'file {fn} is malformed')

        system = platform.system().lower()
        cls.skip = cls.ci_config[f'broken_{system}']
        cls.fatal_warnings = os.environ.get('TEST_FATAL_WARNINGS', 'yes') == 'yes'

    def test_releases_json(self):
        # All tags must be in the releases file
        for t in self.tags:
            name, version = t.rsplit('_', 1)
            # Those are imported tags from v1, they got renamed to sqlite3 and libjpeg-turbo.
            if name in {'sqlite', 'libjpeg'}:
                continue
            self.assertIn(name, self.releases)
            self.assertIn(version, self.releases[name]['versions'], f'for {name}')

        # Verify keys are sorted
        self.assertEqual(sorted(self.releases.keys()), list(self.releases.keys()))

        for name, info in self.releases.items():
            for k in info.keys():
                self.assertIn(k, PERMITTED_KEYS)

    def get_patch_path(self, wrap_section):
        patch_directory = wrap_section.get('patch_directory')
        if patch_directory:
            return Path('subprojects', 'packagefiles', patch_directory)

        return None

    def check_meson_version(self, name: str, version: str, patch_path: str, builddir: str = '_build'):
        with self.subTest(step="check_meson_version"):
            json_file = Path(builddir) / "meson-info/intro-projectinfo.json"
            # don't check if the build was skipped
            if json_file.exists():
                with open(json_file, encoding='utf-8') as project_info_file:
                    project_info = json.load(project_info_file)
                    subproject, = [subproj for subproj in project_info["subprojects"] if subproj["name"] == name]
                    if subproject['version'] != 'undefined' and patch_path:
                        self.assertEqual(subproject['version'], version)

    def test_releases(self):
        has_new_releases = False
        for name, info in self.releases.items():
            with self.subTest(name=name):
                # We do extra checks in the case a new release is being made. This
                # is because some wraps are not passing all tests but we force making
                # them compliant next time we do a release.
                versions: T.List[str] = info['versions']
                latest_tag = f'{name}_{versions[0]}'
                extra_checks = latest_tag not in self.tags

                # Make sure we can load wrap file
                config = configparser.ConfigParser(interpolation=None)
                config.read(f'subprojects/{name}.wrap', encoding='utf-8')

                # Basic checks
                with self.subTest(step='basic'):
                    self.assertTrue(re.fullmatch('[a-z][a-z-1-9._-]*', name))
                    self.assertEqual(config.sections()[0], 'wrap-file')
                    wrap_section = config['wrap-file']
                    self.assertIn('directory', wrap_section)
                    self.check_has_no_path_separators(wrap_section['directory'])
                    self.assertIn('source_filename', wrap_section)
                    self.check_has_no_path_separators(wrap_section['source_filename'])
                    self.assertIn('source_url', wrap_section)
                    self.assertIn('source_hash', wrap_section)
                    self.assertEqual('meson', wrap_section.get('method', 'meson').strip(),
                                     'WrapDB only accepts wraps that use the "meson" method for compiling.')

                # FIXME: Not all wraps currently comply, only check for wraps we modify.
                if extra_checks and self.ci_config.get(name, {}).get('has_provides', True):
                    with self.subTest(step='provide'):
                        self.assertIn('provide', config.sections())
                        self.assertTrue(config.items('provide'))

                patch_path = self.get_patch_path(wrap_section)
                if patch_path:
                    with self.subTest(step='patch_directory'):
                        self.assertTrue(patch_path.is_dir())
                        # FIXME: Not all wraps currently complies, only check for wraps we modify.
                        if extra_checks:
                            self.check_files(name, patch_path)

                # Make sure it has the same deps/progs provided
                with self.subTest(step='have_same_provides'):
                    progs = []
                    deps = []
                    if 'provide' in config.sections():
                        provide = config['provide']
                        progs = [i.strip() for i in provide.get('program_names', '').split(',')]
                        deps = [i.strip() for i in provide.get('dependency_names', '').split(',')]
                        for k in provide:
                            if k not in {'dependency_names', 'program_names'}:
                                deps.append(k.strip())
                    progs = [i for i in progs if i]
                    deps = [i for i in deps if i]
                    self.assertEqual(sorted(progs), sorted(info.get('program_names', [])))
                    self.assertEqual(sorted(deps), sorted(info.get('dependency_names', [])))

                # Verify versions are sorted
                with self.subTest(step='sorted versions'):
                    versions: T.List[str] = info['versions']
                    self.assertGreater(len(versions), 0)
                    versions_obj = [Version(v) for v in versions]
                    self.assertEqual(sorted(versions_obj, reverse=True), versions_obj)

                # The first version could be a new release, all others must have
                # a corresponding tag already.
                for i, v in enumerate(versions):
                    t = f'{name}_{v}'
                    ver, rev = v.rsplit('-', 1)
                    with self.subTest(step='valid release name'):
                        self.assertTrue(re.fullmatch('[a-z0-9._]+', ver))
                        self.assertTrue(re.fullmatch('[0-9]+', rev))
                    if i == 0:
                        with self.subTest(step='check_source_url'):
                            self.check_source_url(name, wrap_section, ver)
                    if i == 0 and t not in self.tags:
                        with self.subTest(step='check_new_release'):
                            has_new_releases = True
                            self.check_new_release(name, deps=deps, progs=progs)
                            with self.subTest(f'If this works now, please remove it from broken_{platform.system().lower()}!'):
                                self.assertNotIn(name, self.skip)
                            self.check_meson_version(name, ver, patch_path)
                    else:
                        with self.subTest(step='version is tagged'):
                            self.assertIn(t, self.tags)

        with self.subTest(step='releases.json updated'):
            if not has_new_releases:
                last_tag = subprocess.check_output(['git', 'describe', '--tags', '--abbrev=0'], text=True, encoding='utf-8').strip()
                changed_files = subprocess.check_output(['git', 'diff', '--name-only', 'HEAD', last_tag], text=True, encoding='utf-8').splitlines()
                if any(f.startswith('subprojects') for f in changed_files):
                    self.fail('Subprojects files changed but no new release added into releases.json')

    @unittest.skipUnless('TEST_BUILD_ALL' in os.environ, 'Run manually only')
    def test_build_all(self):
        passed = []
        skipped = []
        failed = []
        errored = []
        for name, info in self.releases.items():
            if name in self.skip:
                skipped.append(name)
                continue
            try:
                with tempfile.TemporaryDirectory() as d:
                    self.check_new_release(name, d)
                    passed.append(name)
            except unittest.SkipTest:
                passed.append(name)
            except subprocess.CalledProcessError:
                failed.append(name)
            except Exception:
                errored.append(name)
        print(f'{len(passed)} passed:', ', '.join(passed))
        print(f'{len(skipped)} skipped:', ', '.join(skipped))
        print(f'{len(failed)} failed:', ', '.join(failed))
        print(f'{len(errored)} errored:', ', '.join(errored))
        self.assertFalse(failed)
        self.assertFalse(errored)

    def check_has_no_path_separators(self, value: str) -> None:
        self.assertNotIn('/', value)
        self.assertNotIn('\\', value)

    def check_source_url(self, name: str, wrap_section: configparser.SectionProxy, version: str):
        if name == 'sqlite3':
            segs = version.split('.')
            assert len(segs) == 3
            version = segs[0] + segs[1] + '0' + segs[2]
        elif name == 're2':
            version = f'{version[:4]}-{version[4:6]}-{version[6:8]}'
        elif name == 'x-plane-sdk':
            segs = version.split('.')
            self.assertEqual(len(segs), 3)
            version = segs[0] + segs[1] + segs[2]
        elif name in {'netstring-c', 'directxmath', 'luajit'}:
            # There is no specific version for netstring-c
            # DirectXMath source url contains only tag name without version
            # LuaJIT source URL does not contain the version number.
            return True
        source_url = wrap_section['source_url']
        version_ = version.replace('.', '_')
        self.assertTrue(version in source_url or version_ in source_url,
                        f'Version {version} not found in {source_url}')
        return True

    def check_new_release(self, name: str, builddir: str = '_build', deps=None, progs=None):
        print() # Ensure output starts from an empty line (we're running under unittest).
        if is_msys():
            system = 'msys2'
        elif is_alpinelike():
            system = 'alpine'
        else:
            system = platform.system().lower()
        ci = self.ci_config.get(name, {})
        # kept for backwards compatibility
        expect_working = True
        if ci.get('linux_only', False) and not is_linux():
            expect_working = False
        elif not ci.get('build_on', {}).get(system, True):
            expect_working = False

        if deps:
            skip_deps = ci.get('skip_dependency_check', [])
            deps = [d for d in deps if d not in skip_deps]

        options = ['-Dpython.install_env=auto', f'-Dwraps={name}']
        options.append('-Ddepnames={}'.format(','.join(deps or [])))
        options.append('-Dprognames={}'.format(','.join(progs or [])))
        if ci.get('fatal_warnings', expect_working) and self.fatal_warnings:
            options.append('--fatal-meson-warnings')
        options += [f'-D{o}' for o in ci.get('build_options', [])]
        if Path(builddir, 'meson-private', 'cmd_line.txt').exists():
            options.append('--wipe')
        debian_packages = ci.get('debian_packages', [])
        brew_packages = ci.get('brew_packages', [])
        choco_packages = ci.get('choco_packages', [])
        msys_packages = ci.get('msys_packages', [])
        alpine_packages = ci.get('alpine_packages', [])
        python_packages = ci.get('python_packages', [])
        meson_env = os.environ.copy()
        def install_packages(kind, cmd, packages):
            if is_ci():
                with ci_group(f'install {kind} packages'):
                    subprocess.check_call(cmd + packages)
            else:
                s = ', '.join(packages)
                print(f'The following packages could be required: {s}')
        if debian_packages and is_debianlike():
            install_packages('Debian', ['sudo', 'apt-get', '-y', 'install', '--no-install-recommends'], debian_packages)
        elif brew_packages and is_macos():
            install_packages('Homebrew', ['brew', 'install', '--quiet'], brew_packages)
            if is_ci():
                # Ensure binaries from keg-only formulas are available (e.g. bison).
                out = subprocess.check_output(['brew', '--prefix'] + brew_packages)
                for prefix in out.decode().split('\n'):
                    bindir = Path(prefix) / 'bin'
                    if bindir.exists():
                        meson_env['PATH'] = str(bindir) + ':' + meson_env['PATH']
        elif choco_packages and is_windows():
            install_packages('Chocolatey', ['choco', 'install', '-y'], choco_packages)
            if is_ci() and 'nasm' in choco_packages:
                # nasm is not added into PATH by default:
                # https://bugzilla.nasm.us/show_bug.cgi?id=3392224.
                meson_env['PATH'] = 'C:\\Program Files\\NASM;' + meson_env['PATH']
        elif msys_packages and is_msys():
            install_packages('MSYS2', ['sh', '-lc', 'pacboy --noconfirm sync $(printf "%s:p " $@)', 'pacboy'], msys_packages)
        elif alpine_packages and is_alpinelike():
            install_packages('Alpine', ['sudo', 'apk', 'add'], alpine_packages)
        if python_packages:
            install_packages('Python', [sys.executable, '-m', 'pip', 'install'], python_packages)

        res = subprocess.run(['meson', 'setup', builddir] + options, env=meson_env)
        log_file = Path(builddir, 'meson-logs', 'meson-log.txt')
        logs = log_file.read_text(encoding='utf-8')
        if is_ci():
            with ci_group('==== meson-log.txt ===='):
                print(logs)
        if res.returncode == 0:
            if not expect_working:
                raise Exception(f'Wrap {name} successfully configured but was expected to fail')
        else:
            if expect_working:
                res.check_returncode()
            else:
                loglines = logs.splitlines()
                lasterror = [i for i, j in enumerate(loglines) if 'ERROR: ' in j][-1]
                error = ' '.join(loglines[lasterror:])
                if 'unsupported' in error or 'not supported' in error or 'does not support' in error:
                    print('unsupported, as expected')
                    return
                if 'ERROR: Could not execute Vala compiler: valac' in error:
                    print('cannot verify in wrapdb due to missing dependency')
                    return
                if 'ERROR: failed to unpack archive with error: ' in error:
                    print('cannot verify in wrapdb because the archive cannot be unpacked')
                    return
                if any(f'ERROR: {x}' in error for x in ['Dependency', 'Program', 'Pkg-config binary', 'CMake binary']):
                    if 'not found' in error:
                        print('cannot verify in wrapdb due to missing dependency')
                        return
            raise Exception(f'Wrap {name} failed to configure due to bugs in the wrap, rather than due to being unsupported')
        subprocess.check_call(['meson', 'compile', '-C', builddir], env=meson_env)
        if not ci.get('skip_tests', False):
            test_options = ci.get('test_options', [])
            try:
                subprocess.check_call(['meson', 'test', '-C', builddir, '--suite', name, '--print-errorlogs'] + test_options)
            except subprocess.CalledProcessError:
                log_file = Path(builddir, 'meson-logs', 'testlog.txt')
                with ci_group('==== testlog.txt ===='):
                    print(log_file.read_text(encoding='utf-8'))
                raise
        subprocess.check_call(['meson', 'install', '-C', builddir, '--destdir', 'pkg'])

    def is_permitted_file(self, subproject: str, filename: str):
        if filename in PERMITTED_FILES:
            return True
        if filename.endswith('.h.meson') or filename.endswith('.def'):
            return True
        if subproject in PER_PROJECT_PERMITTED_FILES and filename in PER_PROJECT_PERMITTED_FILES[subproject]:
            return True
        return False

    def is_formatted_correctly(self, file: Path) -> bool:
        res = subprocess.run(
            [
                "meson",
                "format",
                "--check-only",
                "--configuration",
                "./meson.format",
                file.absolute(),
            ]
        )
        return res.returncode == 0

    def check_files(self, subproject: str, patch_path: Path) -> None:
        tabs: T.List[Path] = []
        not_permitted: T.List[Path] = []
        unformatted: T.List[Path] = []
        for f in patch_path.rglob('*'):
            if f.is_dir():
                continue
            if f.name in FORMAT_CHECK_FILES and not self.is_formatted_correctly(f):
                unformatted.append(f)
            if not self.is_permitted_file(subproject, f.name):
                not_permitted.append(f)
            elif f.name in NO_TABS_FILES and '\t' in f.read_text(encoding='utf-8'):
                tabs.append(f)
        if tabs:
            tabs_str = ', '.join([str(f) for f in tabs])
            self.fail(f'Tabs in meson files are not allowed: {tabs_str}')
        if not_permitted:
            not_permitted_str = ', '.join([str(f) for f in not_permitted])
            self.fail(f'Not permitted files found: {not_permitted_str}')
        if unformatted:
            unformatted_str = ', '.join([str(f) for f in unformatted])
            unformatted_files_for_command = ' '.join([shlex.quote(str(f)) for f in unformatted])
            self.fail(
                f'''Not formatted files found: {unformatted_str}
Run the following command to format these files:
meson format --inplace {unformatted_files_for_command}''')


if __name__ == '__main__':
    if is_ci():
        # Avoid jumbled output…
        sys.stdout = io.TextIOWrapper(open(sys.stdout.fileno(), 'wb', 0), write_through=True)
        sys.stderr = sys.stdout
    unittest.main(verbosity=2)
