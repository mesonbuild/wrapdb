# Meson Wrap Database

This is a collection of projects that use Meson as their build system, or have
a meson port maintained by the Meson team. They can be used as subproject to
any Meson project that needs them as dependency.

## How to test a wrap

Clone this repository locally, and set the `wraps` option with a coma separated
list of wraps that needs to be built.

For example to test libjpeg-turbo and zlib:
```sh
meson setup builddir -Dwraps=libjpeg-turbo,zlib
meson compile -C builddir
```

## How to contribute new wraps

- Write [`my-project.wrap`](https://mesonbuild.com/Wrap-dependency-system-manual.html)
  file and add it in `subprojects/` directory.

- If upstream project's build system is not Meson, a port can be added in
  `subprojects/packagefiles/my-project/meson.build` and
  `patch_directory = my-subproject` should be added into the wrap file.
  Note that the whole `subprojects/packagefiles/my-project` subtree will be
  copied onto the upstream's source tree, but it is generally not accepted to
  override upstream files.

- Add your release information in `releases.json`. It is a dictionary where the
  key is the wrap name and the value is a dictionary containing with the following
  keys:
  - `versions`: Sorted list (newest first) of release tags in the format
    `<upstream version>-<revision>` where the revision starts at 1 and is
    incremented when a changed is made in the meson port.
  - `dependency_names`: (Optional) List of dependency names (e.g. pkg-config name
    such as `glib-2.0`) provided by the wrap. It must match information from wrap's
    `[provide]` section.
  - `program_names`: (Optional) List of program names (e.g. `glib-compile-resources`)
    provided by the wrap. It must match information from wrap's `[provide]` section.
  - `skip_ci`: (Optional) If set to `true` indicates that the wrap cannot be built
    as part of the CI, for example if specific environment or dependencies are
    required.
  - `skip_ci`: (Optional) If set to `true` indicates that the wrap cannot be built
    as part of the CI, for example if specific environment or dependencies are
    required.
  - `build_options`: (Optional) List of `option=value` strings that will be used
    to build the project on the CI.

- Create Pull Request with your changes.

## How to import one of those wraps into my project

Run `meson wrap install <name>` on the top source dir of your project. It
will install `subprojects/<name>.wrap` file used by meson to download the
dependency.
