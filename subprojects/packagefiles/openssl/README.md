# OpenSSL for Meson

## How this works?
TL;DR: this wrap abuses OpenSSL build system within Node.js.

Node.js has OpenSSL built-in with additional scripting around it to generate configs for GYP build system and thus bypass OpenSSL's native build system.

This wrap abuses that feature by replacing bundled OpenSSL with upstream version, patching mentioned mechanism to also generate a bunch of `meson.build` files for different platforms and uses top-level `meson.build` to wire everything together.

During installation unmodified Node.js tarball will be downloaded, its bundled OpenSSL will be replaced with upstream version and patched with `meson.build` files, enabling ability to build OpenSSL with Meson 🎉.

## How to update to newer release
Unless Node.js changes the mechanism we abuse above (unlikely, but possible, please check the diff between corresponding versions), `generator.sh` file can be used.

Just update OpenSSL version in wrap file, update Node.js version in `generator.sh` file to such that contains matching OpenSSL version bundled with it and run `generator.sh` from the root of the repository:
```
subprojects/packagefiles/openssl/generator.sh
```

Generated files in `generated-config` directory, after which you can try to build it. `create_release.py` will run it as part of the release process, so it doesn't need to be included in Git.

## Acknowledgement
This OpenSSL port wouldn't be possible without [Node.js project](https://github.com/nodejs/node) under [MIT license](https://github.com/nodejs/node/blob/master/LICENSE), whose OpenSSL build system was decomposed and heavily refactored.
