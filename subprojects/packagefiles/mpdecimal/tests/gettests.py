#!python3

import hashlib
import io
import os
import shutil
import sys
import urllib.request
import zipfile

# dectest.zip hash
SHA256 = 'b70a224cd52e82b7a8150aedac5efa2d0cb3941696fd829bdbe674f9f65c3926'

src, dst, *download = sys.argv[1:]

if not os.path.isfile(os.path.join(dst, 'baseconv.decTest')):
    shutil.copytree(src, dst, copy_function=shutil.copyfile, dirs_exist_ok=True)

if download and not os.path.isfile(os.path.join(dst, 'add.decTest')):
    with urllib.request.urlopen('https://speleotrove.com/decimal/dectest.zip') as f:
        data = io.BytesIO(f.read())
        if hashlib.sha256(data.getbuffer()).hexdigest() != SHA256:
            raise AssertionError('downloaded "dectest.zip" hash mismatch')
        with zipfile.ZipFile(data) as z:
            z.extractall(dst)
