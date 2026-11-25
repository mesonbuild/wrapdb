#!/bin/bash
set -e

cd "$(dirname "${BASH_SOURCE[0]}")"

# Node.js version should bundle OpenSSL of matching version to one specified in wrap file
node_version=v22.23.3
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

python3 ../../../generate_def.py --fixup-crypto < openssl/util/libcrypto.num > ../../../crypto.def
python3 ../../../generate_def.py < openssl/util/libssl.num > ../../../ssl.def

rm -rf config/archs
LANG=C make -C config

# Copy generated files back into correct place
cmd='mkdir -p ../../../generated-$(dirname "$1"); cp "$1" ../../../generated-"$1"'
find config/archs -name 'meson.build' -exec sh -c "$cmd" _ignored {} \;
find config/archs -name '*.asm' -exec sh -c "$cmd" _ignored {} \;
find config/archs -name '*.c' -exec sh -c "$cmd" _ignored {} \;
find config/archs -name '*.h' -exec sh -c "$cmd" _ignored {} \;
find config/archs -iname '*.s' -exec sh -c "$cmd" _ignored {} \;

# AIX is not supported by Meson
rm -rf ../../../generated-config/archs/aix*
# 32-bit s390x supported in Meson
rm -rf ../../../generated-config/archs/linux32-s390x
# The `asm_avx2` configs are for assemblers too old for the `asm` ones. They
# only differ from the `asm` ones on x86_64 (see `meson.build`), and Windows
# does not use either
for dir in ../../../generated-config/archs/*/asm_avx2; do
  case "$dir" in
    */linux-x86_64/*|*/BSD-x86_64/*|*/darwin64-x86_64-cc/*|*/solaris64-x86_64-gcc/*) ;;
    *) rm -rf "$dir" ;;
  esac
done
# Remove build info files, we use hardcoded deterministic one instead
rm -rf ../../../generated-config/archs/*/*/crypto/buildinf.h

popd

rm -rf node
