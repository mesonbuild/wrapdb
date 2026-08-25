#!/usr/bin/env python3
"""Build the readcon-core C ABI via cargo rustc and copy artifacts.

Used by meson.build. Headers are shipped; this script never invokes cbindgen.
"""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path

_SHARED_ALIASES = (
    "readcon_core.dll",
    "libreadcon_core.dll",
    "libreadcon_core.so",
    "libreadcon_core.dylib",
)
_STATIC_ALIASES = (
    "readcon_core.lib",
    "libreadcon_core.a",
    "libreadcon_core.lib",
    "readcon_core.dll.lib",
)


def _copy_artifact(
    built: Path, wanted: str, dest: str, aliases: tuple[str, ...]
) -> None:
    candidates = [built / wanted]
    for name in aliases:
        path = built / name
        if path not in candidates:
            candidates.append(path)
        dep = built / "deps" / name
        if dep not in candidates:
            candidates.append(dep)
    for path in candidates:
        if path.is_file():
            shutil.copy2(path, dest)
            return
    listing = sorted(p.name for p in built.iterdir()) if built.is_dir() else []
    raise FileNotFoundError(
        f"cargo artifact {wanted!r} not in {built} (tried {[str(p) for p in candidates]}); "
        f"directory listing: {listing}"
    )


def main(argv: list[str]) -> int:
    if len(argv) not in (9, 10):
        print(
            "usage: meson_cargo_build.py CARGO SRC_ROOT TARGET_DIR PROFILE "
            "SHARED_NAME STATIC_NAME OUT_SHARED OUT_STATIC [FEATURES]",
            file=sys.stderr,
        )
        return 2
    (
        cargo,
        src_root,
        target_dir,
        profile,
        shared_name,
        static_name,
        out_shared,
        out_static,
    ) = argv[1:9]
    features = argv[9] if len(argv) == 10 else ""
    src_root_p = Path(src_root)
    cmd = [
        cargo,
        "rustc",
        "--lib",
        "--manifest-path",
        str(src_root_p / "Cargo.toml"),
        "--target-dir",
        target_dir,
    ]
    if (src_root_p / "Cargo.lock").is_file():
        cmd.append("--locked")
    if (src_root_p / "vendor").is_dir():
        cmd.append("--offline")
    if profile == "release":
        cmd.append("--release")
    if features.strip():
        cmd.extend(["--features", features.strip()])
    env = os.environ.copy()
    rustc_extra: list[str] = []
    if sys.platform.startswith("linux"):
        rustc_extra.append(f"-Clink-arg=-Wl,-soname,{shared_name}")
    elif sys.platform == "darwin":
        rustc_extra.append(f"-Clink-arg=-Wl,-install_name,@rpath/{shared_name}")
    # One crate-type per rustc invocation. MSVC cdylib+staticlib in one
    # call can omit readcon_core.lib while still writing the DLL.
    for crate_type, extra in (("cdylib", rustc_extra), ("staticlib", [])):
        crate_cmd = cmd + ["--", f"--crate-type={crate_type}", *extra]
        subprocess.check_call(crate_cmd, cwd=src_root, env=env)
    built = Path(target_dir) / profile
    _copy_artifact(built, shared_name, out_shared, _SHARED_ALIASES)
    _copy_artifact(built, static_name, out_static, _STATIC_ALIASES)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
