#!/usr/bin/env python3

# Copyright 2021 Xavier Claessens <xclaesse@gmail.com>

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     https://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import annotations
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
import shutil
import textwrap

from pathlib import Path
from utils import CIConfig, ProjectCIConfig, Releases, Version, ci_group, is_ci, is_alpinelike, is_debianlike, is_macos, is_windows, is_msys, read_wrap, FormattingError, format_meson, format_wrap

PERMITTED_FILES = {'generator.sh', 'meson.build', 'meson_options.txt', 'meson.options', 'LICENSE.build'}
PER_PROJECT_PERMITTED_FILES: dict[str, set[str]] = {
    'aws-c-common': {
        'tests.txt',
        'generate_tests.py',
        'run_test.py',
    },
    'box2d': {
        'doctest.h'
    },
    'bzip2': {
        'test.py',
    },
    'curl': {
        'buildinfo.txt.meson',
        'extract.mk',
        'rewrite.mk',
    },
    'glbinding': {
        'pch.h',
        'glbinding_api.h',
        'glbinding_features.h',
        'glbinding_export.h',
        'glbinding-aux_api.h',
        'glbinding-aux_features.h',
        'glbinding-aux_export.h'
    },
    'godot-cpp' : {
         'meson-bindings-generator.py',
     },
    'gumbo-parser': {
        'tokenizer.cc',
    },
    'icu': {
        'export_module.py'
    },
    'lame': {
        'fix_def.py',
        'sym2ver.py',
    },
    'leptonica': {
        '_skipped_test.c',
    },
    'libcap': {
        'gen_cap_names.py',
    },
    'libcbor': {
        'cbor_export.h',
    },
    'libexif': {
        'def.py',
    },
    'libffi': {
        'test-cc-supports-hidden-visibility.py',
        'test-ro-eh-frame.py',
        'test-cc-uses-zarch.py',
        'test-unwind-section.py',
        'extract-libtool-version.py',
    },
    'libgrapheme': {
        'chdir_wrapper.py',
    },
    'libuv': {
        'link_file_in_build_dir.py',
    },
    'luajit': {
        'unwind_check.sh',
    },
    'm4': {
        'm4_test_runner.py',
    },
    'mpdecimal': {
        'gettests.py',
    },
    'nowide': {
        'test_iostream_interactive.py',
    },
    'openal-soft': {
        'hexify.py'
    },
    'openblas': {
        'gen_install_headers.py',
        'prepare_config_last.py',
        'read_config.py',
        'write_to_file.py',
        'test_runner.c',
        'run_fortran.c',
    },
    'openssl': {
        'bn_conf.h',
        'dso_conf.h',
        'buildinf.h',
        'generate_def.py',
        'generate_gypi.pl.patch',
        'meson.build.tmpl',
        'README.md',
    },
    'pcre': {
        'pcre.def',
        'pcreposix.def'
    },
    'protobuf': {
        'symlink_or_copy.py',
    },
    'sdl2': {
        'find-dylib-name.py'
    },
    'soundtouch': {
        'afxres.h'
    },
    'taglib': {
        'checked.h'
    },
    'theora': {
        'check-needed-tex-packages.py',
        'latexmk-wrapper.py',
        'test-tex-packages.py',
        'doxyfile-patcher.py',
        'arm2gnu-wrapper.py',
        'generate_windows_rc.py',
    },
    'vo-aacenc': {
        'makedef.py',
        'stddef.h.in',
    },
    'zlib-ng': {
        'get-version.py',
        'process-zconf.py',
    },
}
SOURCE_FILENAME_PREFIXES = {
    'icu': 'icu4c',
    'libtomcrypt': 'crypt',
}
MIT_LICENSE_BLOCKS = {'expat', 'freeglut', 'glew', 'google-brotli'}
FORMAT_CHECK_FILES = {'meson.build', 'meson_options.txt', 'meson.options'}
SUBPROJECTS_METADATA_FILES = {'subprojects/.gitignore'}
PERMITTED_KEYS = {'versions', 'dependency_names', 'program_names'}
IGNORE_SETUP_WARNINGS = None  # or re.compile(r'something')


class TestReleases(unittest.TestCase):
    ci_config: CIConfig
    fatal_warnings: bool
    annotate_context: bool
    skip_build: bool
    releases: Releases
    skip: list[str]
    tags: set[str]
    timeout_multiplier: float

    @classmethod
    def setUpClass(cls):
        # Take list of git tags.  Ignore tags unreachable from HEAD so we
        # don't fail on tags created after the branch was pushed.
        stdout = subprocess.check_output(['git', 'tag', '--merged'])
        cls.tags = {t.strip() for t in stdout.decode().splitlines()}
        # Ensure we have one of the oldest tags in the repo, and roughly
        # the expected number of tags
        if 'abseil-cpp_20200225.2-1' not in cls.tags or len(cls.tags) < 2000:
            # Repo may have been cloned with --depth=N
            # git fetch --tags is not enough because we ignore tags
            # unreachable from HEAD
            raise Exception("Missing Git tags; try 'git fetch --unshallow'")
        stdout = subprocess.check_output(['git', 'tag', '--no-merged'])
        if stdout.strip():
            print(f'Ignoring unreachable tags: {stdout.decode().splitlines()}')

        try:
            cls.releases = Releases.load()
            cls.ci_config = CIConfig.load()
        except json.decoder.JSONDecodeError as ex:
            raise RuntimeError('metadata is malformed') from ex

        cls.fatal_warnings = os.environ.get('TEST_FATAL_WARNINGS', 'yes') == 'yes'
        cls.annotate_context = os.environ.get('TEST_ANNOTATE_CONTEXT') == 'yes'
        cls.skip_build = os.environ.get('TEST_SKIP_BUILD') == 'yes'
        cls.timeout_multiplier = float(os.environ.get('TEST_TIMEOUT_MULTIPLIER', 1))

    def test_releases_json(self):
        # All tags must be in the releases file
        for t in self.tags:
            name, version = t.rsplit('_', 1)
            # Those are imported tags from v1, they got renamed to sqlite3 and libjpeg-turbo.
            if name in {'sqlite', 'libjpeg'}:
                continue
            self.assertIn(name, self.releases)
            self.assertIn(version, self.releases[name]['versions'], f'for {name}')

        for name, info in self.releases.items():
            for k in info.keys():
                self.assertIn(k, PERMITTED_KEYS)

        try:
            Releases.format(check=True)
        except FormattingError:
            self.fail('releases.json is not formatted.  Run tools/format.py to format it.')

    def get_patch_path(self, wrap_section):
        patch_directory = wrap_section.get('patch_directory')
        if patch_directory:
            return Path('subprojects', 'packagefiles', patch_directory)

        return None

    def ensure_source_dir(self, name: str, wrap: configparser.ConfigParser) -> Path:
        dir = Path('subprojects', wrap['wrap-file']['directory'])
        if not dir.exists():
            # build has not run and unpacked the source; do that
            subprocess.check_call(
                ['meson', 'subprojects', 'download', name]
            )
        return dir

    def check_meson_version(self, name: str, version: str, patch_path: str | None, builddir: str = '_build') -> None:
        with self.subTest(step="check_meson_version"):
            json_file = Path(builddir) / "meson-info/intro-projectinfo.json"
            # don't check if the build was skipped
            if json_file.exists():
                with open(json_file, encoding='utf-8') as project_info_file:
                    project_info = json.load(project_info_file)
                    subproject, = [subproj for subproj in project_info["subprojects"] if subproj["name"] == name]
                    if subproject['version'] != 'undefined' and patch_path:
                        self.assertEqual(subproject['version'], version)

    def get_transitional_provides(self, wrap: configparser.ConfigParser) -> set[str]:
        if 'provide' not in wrap.sections():
            return set()
        keys = set(k.strip() for k in wrap['provide'])
        return keys - {'dependency_names', 'program_names'}

    def test_releases(self) -> None:
        has_new_releases = False
        for name, info in self.releases.items():
            with self.subTest(name=name):
                # We do extra checks in the case a new release is being made. This
                # is because some wraps are not passing all tests but we force making
                # them compliant next time we do a release.
                versions: list[str] = info['versions']
                latest_tag = f'{name}_{versions[0]}'
                extra_checks = latest_tag not in self.tags

                # Make sure we can load wrap file
                config = read_wrap(name)

                # Basic checks
                with self.subTest(step='basic'):
                    self.assertTrue(re.fullmatch('[a-z][a-z-1-9._-]*', name))
                    self.assertEqual(config.sections()[0], 'wrap-file')
                    wrap_section = config['wrap-file']
                    self.assertIn('directory', wrap_section)
                    self.check_has_no_path_separators(wrap_section['directory'])
                    self.assertIn('source_filename', wrap_section)
                    self.check_has_no_path_separators(wrap_section['source_filename'])
                    self.check_source_filename(name, versions[0].split('-')[0], wrap_section['directory'], wrap_section['source_filename'])
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
                        # Don't recheck unchanged projects that may have
                        # been formatted with an older Meson.  Also, format
                        # checks are slow.
                        if extra_checks:
                            self.check_files(name, patch_path)

                # Make sure it has the same deps/progs provided
                with self.subTest(step='have_same_provides'):
                    progs = []
                    deps = []
                    if 'provide' in config.sections():
                        provide = config['provide']
                        progs = [i.strip() for i in provide.get('program_names', '').split(',')]
                        deps = (
                            [i.strip() for i in provide.get('dependency_names', '').split(',')] +
                            list(self.get_transitional_provides(config))
                        )
                    progs = [i for i in progs if i]
                    deps = [i for i in deps if i]
                    self.assertEqual(sorted(progs), sorted(info.get('program_names', [])))
                    self.assertEqual(sorted(deps), sorted(info.get('dependency_names', [])))

                # Downstream ports shouldn't use transitional provides syntax
                # FIXME: Not all wraps currently comply, only check for wraps we modify.
                if extra_checks and patch_path:
                    # Intentional leading whitespace
                    errmsg = textwrap.dedent('''

                        In the meson.build file use `meson.override_dependenc('foo', foo_dep)`
                        for each dependency.

                        In subprojects/foo.wrap, replace `name = name_dep` entries with
                        `dependency_names = foo`

                        See https://mesonbuild.com/Adding-new-projects-to-wrapdb.html#overriding-dependencies-in-the-submitted-project
                        for more information.
                        ''')
                    with self.subTest(step="Ports must not use 'foo = foo_dep' provide syntax"):
                        self.assertEqual(self.get_transitional_provides(config), set(), errmsg)

                # Verify versions are sorted
                with self.subTest(step='sorted versions'):
                    versions = info['versions']
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
                            self.log_context(name)
                            if not self.skip_build:
                                self.check_new_release(name, deps=deps, progs=progs)
                                with self.subTest(f'If this works now, please remove it from broken_{platform.system().lower()}!'):
                                    self.assertNotIn(name, self.ci_config.broken)
                                self.check_meson_version(name, ver, patch_path)
                        if patch_path:
                            self.check_project_args(name, config)
                        else:
                            self.check_nonport_source(name, config)
                    else:
                        with self.subTest(step='version is tagged'):
                            self.assertIn(t, self.tags)

        with self.subTest(step='releases.json updated'):
            if not has_new_releases:
                last_tag = subprocess.check_output(['git', 'describe', '--tags', '--abbrev=0'], text=True, encoding='utf-8').strip()
                changed_files = subprocess.check_output(['git', 'diff', '--name-only', 'HEAD', last_tag], text=True, encoding='utf-8').splitlines()
                if any(f.startswith('subprojects') and f not in SUBPROJECTS_METADATA_FILES for f in changed_files):
                    self.fail('Subprojects files changed but no new release added into releases.json')

    @unittest.skipUnless('TEST_BUILD_ALL' in os.environ, 'Run manually only')
    def test_build_all(self):
        passed = []
        skipped = []
        failed = []
        errored = []
        for name, info in self.releases.items():
            if name in self.ci_config.broken:
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

    def check_source_filename(self, name: str, version: str, directory: str, filename: str) -> None:
        basename = re.sub(r'(\.tar)?\.[a-z0-9]+$', '', filename)
        # Ideally the tarball is named after the top-level directory
        if basename == directory:
            return
        # Top-level directory in Codeberg tag archives doesn't include the
        # version number
        if basename == f'{directory}-{version}':
            return
        # Also allow the tarball to be named after the wrap, for cases where
        # the top-level directory name is unhelpful (if libfuse creates a
        # tag fuse-1.2.3, GitHub will use a directory called
        # libfuse-fuse-1.2.3) or the upstream repo name is ambiguous
        # (quickjs-ng is in a repo called quickjs)
        if basename == f'{name}-{version}':
            return
        # Manual overrides for unusual cases
        alt_name = SOURCE_FILENAME_PREFIXES.get(name)
        if alt_name and basename.startswith(f'{alt_name}-'):
            return
        self.fail(f'Stem of source_filename "{filename}" isn\'t "{directory}", "{directory}-{version}", or "{name}-{version}". If upstream specifies a filename, use that, and update SOURCE_FILENAME_PREFIXES if necessary to allow it. If using an autogenerated Git archive (e.g. from GitHub), select whichever of the listed names is most legible and add the appropriate file extension(s).')

    def check_source_url(self, name: str, wrap_section: configparser.SectionProxy, version: str) -> None:
        source_url = wrap_section['source_url']
        self.assertNotIn('ftp.gnu.org', source_url, 'use ftpmirror.gnu.org instead')

        if name == 'sqlite3':
            segs = version.split('.')
            assert len(segs) == 3
            version = segs[0] + segs[1] + '0' + segs[2]
        elif name == 're2':
            version = f'{version[:4]}-{version[4:6]}-{version[6:8]}'
        elif name == 'x-plane-sdk':
            if version in wrap_section['source_url']:
                # internalize_sources.py replaced the source URL with one
                # that contains the version
                return
            segs = version.split('.')
            self.assertEqual(len(segs), 3)
            version = segs[0] + segs[1] + segs[2]
        elif name in {'netstring-c', 'directxmath', 'luajit'}:
            # There is no specific version for netstring-c
            # DirectXMath source url contains only tag name without version
            # LuaJIT source URL does not contain the version number.
            return
        version_ = version.replace('.', '_')
        self.assertTrue(version in source_url or version_ in source_url,
                        f'Version {version} not found in {source_url}')

    def log_context(self, name: str) -> None:
        if self.annotate_context and name in self.ci_config:
            print(f'\n::notice title={name} config::' + json.dumps(self.ci_config[name], indent=2).replace('\n', '%0A') + '\n')

    def check_new_release(self, name: str, builddir: str = '_build', deps=None, progs=None) -> None:
        print() # Ensure output starts from an empty line (we're running under unittest).
        if is_msys():
            system = 'msys2'
        elif is_alpinelike():
            system = 'alpine'
        else:
            system = platform.system().lower()
        ci = self.ci_config.get(name, {})
        expect_working = ci.get('build_on', {}).get(system, True)

        if deps:
            skip_deps = ci.get('skip_dependency_check', [])
            deps = [d for d in deps if d not in skip_deps]
        if progs:
            skip_progs = ci.get('skip_program_check', [])
            progs = [p for p in progs if p not in skip_progs]

        options = ['-Dpython.install_env=auto', f'-Dwraps={name}']
        options.append('-Ddepnames={}'.format(','.join(deps or [])))
        options.append('-Dprognames={}'.format(','.join(progs or [])))
        fatal_warnings = ci.get('fatal_warnings', expect_working) and self.fatal_warnings
        if fatal_warnings:
            options.append('--fatal-meson-warnings')
        options += self.ci_config.get_option_arguments(name)
        if Path(builddir, 'meson-private', 'cmd_line.txt').exists():
            options.append('--wipe')
        meson_env = self.install_packages(ci)

        def do_setup(builddir, options, meson_env):
            res = subprocess.run(['meson', 'setup', builddir] + options, env=meson_env)
            log_file = Path(builddir, 'meson-logs', 'meson-log.txt')
            logs = log_file.read_text(encoding='utf-8')
            if is_ci():
                with ci_group('==== meson-log.txt ===='):
                    print(logs)
            return res, logs
        res, logs = do_setup(builddir, options, meson_env)
        if res.returncode != 0 and fatal_warnings and IGNORE_SETUP_WARNINGS:
            match = IGNORE_SETUP_WARNINGS.search(logs)
            if match:
                print(f'\nFound spurious warning: "{match.group(0)}"')
                print('Rerunning setup without --fatal-meson-warnings.\n')
                options.remove('--fatal-meson-warnings')
                res, logs = do_setup(builddir, options, meson_env)

        if res.returncode == 0:
            if not expect_working:
                raise Exception(f'Wrap {name} successfully configured but was expected to fail')
        else:
            loglines = logs.splitlines()
            lasterror = [i for i, j in enumerate(loglines) if 'ERROR: ' in j][-1]
            error = ' '.join(loglines[lasterror:])
            if 'unsupported architecture' in error:
                # Architecture is hard to detect here, we can't just use python's
                # platform.machine(). Meson has to make compiler checks to get it
                # right. Just assume that if a project does this error it knows
                # what it is doing.
                print('unsupported architecture')
                return
            if expect_working:
                res.check_returncode()
            else:
                for msg in ['unsupported',
                            'not supported',
                            'does not support',
                            # wayland-protocols upstream
                            'SFD_CLOEXEC is needed to compile Wayland libraries',
                            ]:
                    if msg in error:
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
            if self.timeout_multiplier != 1:
                print(f'TEST_TIMEOUT_MULTIPLIER env var set; extending test timeout by {self.timeout_multiplier}x')
                for i, o in enumerate(test_options):
                    match = re.match(r'--timeout-multiplier=([-\d.e]+)$', o)
                    if match:
                        test_options[i] = f'--timeout-multiplier={self.timeout_multiplier * float(match.group(1))}'
                        break
                    elif i > 0 and test_options[i - 1] in ('-t', '--timeout-multiplier'):
                        test_options[i] = str(self.timeout_multiplier * float(o))
                        break
                else:
                    test_options.append(f'--timeout-multiplier={self.timeout_multiplier}')
            try:
                subprocess.check_call(['meson', 'test', '-C', builddir, '--suite', name, '--print-errorlogs'] + test_options)
            except subprocess.CalledProcessError:
                log_file = Path(builddir, 'meson-logs', 'testlog.txt')
                with ci_group('==== testlog.txt ===='):
                    print(log_file.read_text(encoding='utf-8'))
                raise
        subprocess.check_call(['meson', 'install', '-C', builddir, '--destdir', 'pkg'])

    def install_packages(self, ci: ProjectCIConfig) -> dict[str, str]:
        debian_packages = ci.get('debian_packages', [])
        brew_packages = ci.get('brew_packages', [])
        choco_packages = ci.get('choco_packages', [])
        msys_packages = ci.get('msys_packages', [])
        alpine_packages = ci.get('alpine_packages', [])
        python_packages = ci.get('python_packages', [])
        meson_env = os.environ.copy()
        def do_install(kind, cmd, packages):
            if is_ci():
                with ci_group(f'install {kind} packages'):
                    subprocess.check_call(cmd + packages)
            else:
                s = ', '.join(packages)
                print(f'The following packages could be required: {s}')
        if debian_packages and is_debianlike():
            do_install('Debian', ['sudo', 'apt-get', '-y', 'install', '--no-install-recommends'], debian_packages)
        elif brew_packages and is_macos():
            do_install('Homebrew', ['brew', 'install', '--quiet'], brew_packages)
            if is_ci():
                # Ensure binaries from keg-only formulas are available (e.g. bison).
                out = subprocess.check_output(['brew', '--prefix'] + brew_packages)
                for prefix in out.decode().split('\n'):
                    bindir = Path(prefix) / 'bin'
                    if bindir.exists():
                        meson_env['PATH'] = str(bindir) + ':' + meson_env['PATH']
        elif choco_packages and is_windows():
            do_install('Chocolatey', ['choco', 'install', '-y'], choco_packages)
            if is_ci() and 'nasm' in choco_packages:
                # nasm is not added into PATH by default:
                # https://bugzilla.nasm.us/show_bug.cgi?id=3392224.
                meson_env['PATH'] = 'C:\\Program Files\\NASM;' + meson_env['PATH']
        elif msys_packages and is_msys():
            do_install('MSYS2', ['sh', '-lc', 'pacboy --noconfirm sync $(printf "%s:p " $@)', 'pacboy'], msys_packages)
        elif alpine_packages and is_alpinelike():
            do_install('Alpine', ['sudo', 'apk', 'add'], alpine_packages)
        if python_packages:
            do_install('Python', [sys.executable, '-m', 'pip', 'install'], python_packages)
        return meson_env

    def is_permitted_file(self, subproject: str, filename: str) -> bool:
        if filename in PERMITTED_FILES:
            return True
        if filename.endswith('.h.meson') or filename.endswith('.def'):
            return True
        if subproject in PER_PROJECT_PERMITTED_FILES and filename in PER_PROJECT_PERMITTED_FILES[subproject]:
            return True
        return False

    def check_project_args(self, name: str, wrap: configparser.ConfigParser) -> None:
        dir = self.ensure_source_dir(name, wrap)
        try:
            project_json = subprocess.check_output(
                ['meson', 'rewrite', 'kwargs', 'info', 'project', '/'],
                cwd=dir, text=True, stderr=subprocess.DEVNULL
            )
        except subprocess.CalledProcessError:
            # rewriter fails if any compilers are missing; ignore
            return
        project = json.loads(project_json)['kwargs']['project#/']

        with self.subTest(step='check_license'):
            self.assertIn('license', project)  # project must specify license
            self.assertIs(type(project['license']), str)  # license must not use legacy list syntax
            try:
                import license_expression  # type: ignore[import-untyped]
            except ImportError:
                print('\nno license_expression library; skipping SPDX validation')
            else:
                try:
                    license_expression.get_spdx_licensing().parse(
                        project['license'], validate=True, strict=True
                    )
                except license_expression.ExpressionParseError as exc:
                    raise Exception('Invalid license expression; see https://spdx.github.io/spdx-spec/v3.0.1/annexes/spdx-license-expressions/') from exc
                except license_expression.ExpressionError as exc:
                    raise Exception('Invalid license; see https://spdx.org/licenses/') from exc

        with self.subTest(step='check_default_options'):
            for name in self.get_default_options(project):
                # Before Meson 1.8 these were ignored in subproject
                # default_options, and in any case it's not clear that wraps
                # should have an opinion about them.  We don't check for all
                # non-per-subproject options, just the ones that seem likely
                # to show up in a wrap.
                if name in {'buildtype',
                            'debug',
                            'optimization',
                            'prefer_static',
                            'strip',
                            'unity'}:
                    raise Exception(f'{name} is not permitted in default_options')

    def check_nonport_source(self, name: str, wrap: configparser.ConfigParser) -> None:
        with self.subTest(step='check for meson.override_dependency()'):
            provides = self.get_transitional_provides(wrap)
            if provides:
                dir = self.ensure_source_dir(name, wrap)
                for path in dir.rglob('meson.build'):
                    if 'meson.override_dependency' in path.read_text(encoding='utf-8'):
                        # assume if an upstream converts to
                        # override_dependency it converts completely
                        raise Exception(f"{path.relative_to(dir)} contains meson.override_dependency(); wrap provides should be converted to e.g. 'dependency_names = {', '.join(sorted(provides))}'")

    def get_default_options(self, project: dict[str, T.Any]) -> dict[str, str | None]:
        opts = project.get('default_options')
        if not opts:
            return {}
        elif isinstance(opts, dict):
            return opts
        elif isinstance(opts, str):
            opts = [opts]
        return dict(opt.split('=', 1) for opt in opts if opt is not None)

    def check_files(self, subproject: str, patch_path: Path) -> None:
        not_permitted: list[Path] = []
        check_format: list[Path] = []
        license_blocks: list[Path] = []
        for f in patch_path.rglob('*'):
            if f.is_dir():
                continue
            if f.name in FORMAT_CHECK_FILES:
                check_format.append(f)
            if not self.is_permitted_file(subproject, f.name):
                not_permitted.append(f)
            if self.has_license_block(f):
                license_blocks.append(f)
        if not_permitted:
            not_permitted_str = ', '.join([str(f) for f in not_permitted])
            self.fail(f'Not permitted files found: {not_permitted_str}')
        try:
            format_meson(check_format, check=True)
            format_wrap(subproject, check=True)
        except FormattingError:
            self.fail('Unformatted files found.  Run tools/format.py to format these files.')
        if license_blocks and subproject not in MIT_LICENSE_BLOCKS and not (patch_path / 'LICENSE.build').exists():
            license_blocks_str = ', '.join(str(f) for f in license_blocks)
            self.fail(f"Found files {license_blocks_str} with license headers in a project without a LICENSE.build.  The LICENSE.build file in the patch ZIP defaults to MIT unless the patch directory has its own LICENSE.build, which should state the license for the wrap's build files.")

    def has_license_block(self, path: Path) -> bool:
        for line in path.read_text(encoding='utf-8').splitlines():
            lower = line.strip().lower()
            if lower and not lower.startswith('#'):
                # first non-comment line
                return False
            if 'spdx-license-identifier:' in lower:
                # allow pure MIT, matching the repo default
                if not lower.endswith('spdx-license-identifier: mit'):
                    return True
            elif 'license' in lower:
                return True
        return False

    @unittest.skipUnless('TEST_MESON_VERSION_DEPS' in os.environ, 'Run manually only')
    def test_meson_version_deps(self) -> None:
        for name, info in self.releases.items():
            with self.subTest(name=name):
                if f'{name}_{info["versions"][0]}' not in self.tags:
                    self.report_meson_version_deps(name)

    def report_meson_version_deps(self, name: str, builddir: str = '_build') -> None:
        wrap = read_wrap(name)
        patch_dir = self.get_patch_path(wrap['wrap-file'])
        if not patch_dir:
            # only check projects maintained downstream
            return

        meson_file = patch_dir / 'meson.build'
        meson_file_line = None
        # find first 'meson_version', or else first 'project(', or use line 0
        for i, line in enumerate(meson_file.read_text(encoding='utf-8').splitlines()):
            if 'project(' in line and meson_file_line is None:
                meson_file_line = i
            if 'meson_version' in line:
                meson_file_line = i
                break
        meson_file_line = meson_file_line or 0

        try:
            severity, title, message = self.get_meson_version_deps(name, builddir, wrap)
        except Exception:
            severity = 'error'
            title = 'Minimum Meson version'
            message = 'Could not verify minimum Meson version'
            raise
        finally:
            message = message.replace('\n', '%0A')
            print(f'\n::{severity} file={meson_file},line={meson_file_line + 1},title={title}::{message}\n')

    def get_meson_version_deps(self, name: str, builddir: str, wrap: configparser.ConfigParser) -> tuple[str, str, str]:
        print() # Ensure output starts from an empty line (we're running under unittest).

        # purge any extra options from a previous test_releases() run
        if Path(builddir).exists():
            shutil.rmtree(builddir)
        # ensure we have an unpacked source tree
        source_dir = self.ensure_source_dir(name, wrap)
        # install packages and set PATH
        ci = self.ci_config.get(name, {})
        meson_env = self.install_packages(ci)

        source_meson_file = source_dir / 'meson.build'
        source_meson_contents = source_meson_file.read_bytes()
        try:
            project_args = json.loads(
                subprocess.check_output(
                    ['meson', 'rewrite', 'kwargs', 'info', 'project', '/'],
                    cwd=source_dir, env=meson_env
                )
            )['kwargs']['project#/']
        except subprocess.CalledProcessError:
            project_args = {}
        version_request = project_args.get('meson_version')
        if version_request:
            version_request = version_request.replace(' ', '')
            while version_request.count('.') < 2:
                version_request += '.0'

        options = ['-Dpython.install_env=auto', f'-Dwraps={name}']
        options += self.ci_config.get_option_arguments(name)
        try:
            subprocess.check_call(
                ['meson', 'rewrite', 'kwargs', 'set', 'project', '/', 'meson_version', '>=0'],
                cwd=source_dir, env=meson_env
            )
            subprocess.check_call(
                ['meson', 'setup', builddir] + options, env=meson_env
            )
        finally:
            source_meson_file.write_bytes(source_meson_contents)

        log_file = Path(builddir, 'meson-logs', 'meson-log.txt')
        log_it = iter(enumerate(log_file.read_text(encoding='utf-8').splitlines()))
        features: dict[str, list[str]] = {}
        for i, line in log_it:
            if 'uses features which were added in newer versions' in line:
                for i, line in log_it:
                    match = re.match(r" \* ([0-9.]+): {'(.*)'}$", line)
                    if match:
                        features[match[1]] = match[2].split("', '")
                    elif 'finished.' in line:
                        break
                    else:
                        raise Exception(f'Could not parse feature version report line: {line}')
                else:
                    raise Exception('Did not find end of feature version report')
                break

        default_options = self.get_default_options(project_args)
        for opt in 'c_std', 'cpp_std':
            if opt in default_options:
                features.setdefault('0.63.0', []).append(f'{opt} in subproject default_options')

        versions = sorted(
            features, key=lambda ver: tuple(int(c) for c in ver.split('.'))
        )
        if versions:
            message = '\n'.join(
                f'{ver}: {", ".join(features[ver])}' for ver in versions
            )
            min_version = versions[-1]
        else:
            message = 'No versioned features found.'
            min_version = '0.0.0'
        return (
            'warning' if (version_request or '>=0.0.0') != f'>={min_version}' else 'notice',
            f'Minimum Meson version is {min_version}',
            message
        )


if __name__ == '__main__':
    if is_ci():
        # Avoid jumbled output…
        sys.stdout = io.TextIOWrapper(open(sys.stdout.fileno(), 'wb', 0), write_through=True)
        sys.stderr = sys.stdout
    unittest.main(verbosity=2)
