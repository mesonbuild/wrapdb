#!/bin/bash
set -e
set -x

cd "$(dirname "${BASH_SOURCE[0]}")"

# Node.js version should bundle OpenSSL of matching version to one specified in wrap file
node_version="$NODE_VERSION"
openssl_version="$OPENSSL_VERSION"

if [ -z "$openssl_version" ]; then
  openssl_version=$(grep 'directory = ' ../../openssl.wrap | grep -oE '[0-9]+\.[0-9]+\.[0-9]+[a-z]?')
  node_version=$(grep 'node_version = ' ../../openssl.wrap | grep -oE 'v[0-9]+\.[0-9]+\.[0-9]+')
fi

if [ ! -d "node" ]; then
  git clone --depth 1 --branch $node_version https://github.com/nodejs/node.git
else
  pushd node
  git checkout -f $node_version
  popd
fi

rm -rf generated-config

pushd node/deps/openssl

# Apply patch that will allow us generate `meson.build` for different targets
patch -u config/Makefile -i ../../../Makefile.patch
patch -u config/generate_gypi.pl -i ../../../generate_gypi.pl.patch
# Copy `meson.build` template file
cp ../../../meson.build.tmpl config/

# Swap bundled OpenSSL in Node.js with upstream
if [ -d "openssl" ]; then
  if [ ! -d "openssl/.git" ]; then
    rm -rf "openssl"
    git clone --depth 1 --branch "openssl-$openssl_version" https://github.com/openssl/openssl.git
  fi
fi

python3 ../../../generate_def.py --fixup-crypto < openssl/util/libcrypto.num > ../../../crypto.def
python3 ../../../generate_def.py < openssl/util/libssl.num > ../../../ssl.def

pushd openssl
pwd
git checkout -f "openssl-$openssl_version" 
# Apply patch to block OpenSSL from renaming the Windows DLLs
patch -p1 -i ../../../../exclude-library-directive-msvc.patch
popd

rm -rf config/archs
LANG=C make -C config

# Copy generated files back into correct place
cmd='mkdir -p ../../../generated-$(dirname "$1"); cp "$1" ../../../generated-"$1"'
find config/archs -name 'meson.build' -exec sh -c "$cmd" _ignored {} \;
find config/archs -name '*.asm' -exec sh -c "$cmd" _ignored {} \;
find config/archs -name '*.c' -exec sh -c "$cmd" _ignored {} \;
find config/archs -name '*.h' -exec sh -c "$cmd" _ignored {} \;
find config/archs -name '*.s' -exec sh -c "$cmd" _ignored {} \;
find config/archs -name '*.rc' -exec sh -c "$cmd" _ignored {} \;

# Remove build info files, we use hardcoded deterministic one instead
rm -rf ../../../generated-config/archs/*/*/crypto/buildinf.h

popd

# Comment this line out when testing, so that it avoids repeated clones
# rm -rf node
