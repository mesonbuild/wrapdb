"""
format or check all meson.build file in projects

arguments:

--check: do check without formatting
--dirty: do not format/check all files, only process files changed (only valid in git repo)
"""

import sys
import shlex
import pathlib
import subprocess
from shutil import which
from itertools import chain

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

for i, meson_file in enumerate(all_meson_files):
    readable_filename = meson_file.relative_to(project_root).as_posix()
    print("processing {}/{}: {}".format(i + 1, len(all_meson_files), readable_filename))
    try:
        subprocess.check_call(base_command + [str(meson_file)], cwd=str(project_root))
    except subprocess.CalledProcessError as e:
        if is_check:
            print("{} is not formatted".format(readable_filename))
            sys.exit(e.returncode)
        else:
            print("failed to format {}".format(readable_filename))
