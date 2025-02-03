"""
format or check all meson.build file in projects

arguments:

--check: do check without formatting
--dirty: do not format/check all files, only process files changed (only valid in git repo)
"""

import os
import sys
import shlex
import pathlib
import subprocess
from shutil import which
from itertools import chain
from multiprocessing.pool import ThreadPool

is_check = "--check" in sys.argv
only_dirty = "--dirty" in sys.argv

meson = which("meson")
if not meson:
    print("failed to find meson")
    sys.exit(1)

base_command = [meson, "fmt", "--editor-config"]
if is_check:
    base_command.append("--check-only")
else:
    base_command.append("--inplace")

project_root = pathlib.Path(__file__).parent.parent


def get_file_list_from_git(cmd):
    out = subprocess.check_output(
        cmd,
        cwd=str(project_root),
    )
    return [
        project_root.joinpath(file)
        for file in out.decode().splitlines()
        if file.endswith("meson.build")
    ]


if only_dirty:
    all_meson_files = get_file_list_from_git(shlex.split("git diff --name-only HEAD"))
else:
    all_meson_files = sorted(
        chain(
            [project_root.joinpath("meson.build")],
            project_root.glob("subprojects/packagefiles/**/meson.build"),
        )
    )


def process_file(meson_file: pathlib.Path) -> tuple[bool, pathlib.Path]:
    try:
        subprocess.check_call(base_command + [str(meson_file)], cwd=str(project_root))
    except subprocess.CalledProcessError:
        return False, meson_file
    return True, meson_file


with ThreadPool(processes=(os.cpu_count() or 4) + 1) as pool:
    err = False
    for ok, meson_file in pool.imap_unordered(process_file, all_meson_files):
        readable_filename = meson_file.relative_to(project_root).as_posix()
        if not ok:
            err = True
            if is_check:
                print("{} is not formatted".format(readable_filename))
            else:
                print("failed to format {}".format(readable_filename))
            break

if err:
    sys.exit(1)
