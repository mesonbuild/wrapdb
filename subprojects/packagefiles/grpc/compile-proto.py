#!/usr/bin/env python3

import argparse
import sys
from pathlib import Path
import subprocess
import os


def builddir_suffix(proto: Path, source_root: Path) -> str:
	return os.path.relpath(proto.resolve().parent, source_root.resolve())

def symlink(target: Path, alias: Path) -> str:
	rtarget = Path(os.path.relpath(target.resolve(), alias.resolve().parent))
	if alias.is_symlink():
		alias.unlink()
	alias.symlink_to(rtarget)

def compileSources(files: [Path], protoc: Path, grpc_plugin: Path, srcdir: Path, builddir: Path):
	for p in files:
		outdir = builddir / builddir_suffix(p, srcdir)
		outdir.mkdir(parents=True, exist_ok=True)
		cmd = [
			f"{protoc}",
			f"--plugin=protoc-gen-grpc={grpc_plugin.resolve()}",
			f"--cpp_out={outdir}",
			f"--grpc_out={outdir}",
			"--proto_path=" + str(p.parent),
			str(p),
		]
		ecode = subprocess.Popen(cmd).wait()
		assert(ecode == 0)

		basename = p.name.replace(".proto", "")
		for ext in {".pb.h", ".pb.cc", ".grpc.pb.h", ".grpc.pb.cc"}:
			newname = basename + ext
			symlink(outdir / newname, builddir / newname)

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-c", "--protoc", help="path to protoc compiler executable")
	parser.add_argument("-p", "--grpc_plugin", help="path to grpc_cpp_plugin executable")
	parser.add_argument("-s", "--src-dir", help="source root directory")
	parser.add_argument("-o", "--out-dir", help="output directory")
	parser.add_argument("proto_file", nargs="+", help="input .proto files")
	args = parser.parse_args()
	compileSources(list(map(Path, args.proto_file)), Path(args.protoc), Path(args.grpc_plugin), Path(args.src_dir), Path(args.out_dir))

