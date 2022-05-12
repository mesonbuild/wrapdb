#!/bin/bash
set -e

cd "$(dirname "${BASH_SOURCE[0]}")"

# Node.js version should bundle OpenSSL of matching version to one specified in wrap file
node_version=v17.7.1
openssl_version="$OPENSSL_VERSION"

if [ -z "$openssl_version" ]; then
  openssl_version=$(grep 'directory = ' ../../openssl.wrap | grep -oE '[0-9]+\.[0-9]+\.[0-9]+')
fi

rm -rf node
git clone --depth 1 --branch $node_version https://github.com/nodejs/node.git

rm -rf generated-config

pushd node/deps/openssl

# Apply patch that will allow us generate `meson.build` for different targets
patch -u config/generate_gypi.pl -i ../../../generate_gypi.pl.patch
# Copy `meson.build` template file
cp ../../../meson.build.tmpl config/

# Swap bundled OpenSSL in Node.js with upstream
rm -rf openssl
git clone --depth 1 --branch "openssl-$openssl_version" https://github.com/openssl/openssl.git

rm -rf config/archs
LANG=C make -C config

# Copy generated files back into correct place
find config/archs -name 'meson.build' | xargs -I % sh -c 'mkdir -p ../../../generated-$(dirname %); cp % ../../../generated-%'
find config/archs -name '*.asm' | xargs -I % sh -c 'mkdir -p ../../../generated-$(dirname %); cp % ../../../generated-%'
find config/archs -name '*.c' | xargs -I % sh -c 'mkdir -p ../../../generated-$(dirname %); cp % ../../../generated-%'
find config/archs -name '*.h' | xargs -I % sh -c 'mkdir -p ../../../generated-$(dirname %); cp % ../../../generated-%'
find config/archs -iname '*.s' | xargs -I % sh -c 'mkdir -p ../../../generated-$(dirname %); cp % ../../../generated-%'

# AIX is not supported by Meson
rm -rf ../../../generated-config/archs/aix*
# 32-bit s390x supported in Meson
rm -rf ../../../generated-config/archs/linux32-s390x
# Linux ELF is useless in Meson
rm -rf ../../../generated-config/archs/linux-elf
# This is for old gas/nasm versions, we do not care about them
rm -rf ../../../generated-config/archs/*/asm_avx2
# Remove build info files, we use hardcoded deterministic one instead
rm -rf ../../../generated-config/archs/*/*/crypto/buildinf.h

popd

rm -rf node
