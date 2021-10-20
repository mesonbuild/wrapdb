# Meson Wrap Database

This is a collection of projects that use Meson as their build system, or have
a meson port maintained by the Meson team. They can be used as subproject to
any Meson project that needs them as dependency.

## How to test a wrap

Clone this repository locally, and set the `wraps` option with a comma separated
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

- It is often easier to develop in `subprojects/my-project` directory and update
  packagefiles directory at the end. This can be done using
  `tools/update-packagefiles.py` script.

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

- Configure CI in `ci_config.json`. It is a dictionary where the key is the wrap
  name and the value is a dictionary containing with the following keys:
  - `build_options`: (Optional) List of `option=value` strings that will be used
    to build the project on the CI.
  - `debian_packages`: (Optional) List of extra packages that will be installed
    on debian-like CI runners. Dependencies that can be provided by other wraps
    should not be added here because it's better to test that fallbacks works.
    When running `tools/sanity_checks.py` locally, this list will be printed
    but not installed.
  - `linux_only`: (Optional) If set to `true`, indicates the wrap should be tested
    only on Linux CI.
  - `fatal_warnings`: (Optional) If set to `false` removes --fatal-meson-warning.
    Use this only when there is no other way to fix the warning.

- Test locally by running `tools/sanity_checks.py` script. It will be executed
  on the CI and must always return success before merging any PR.

- Create Pull Request with your changes.

## How to import one of those wraps into my project

Run `meson wrap install <name>` on the top source dir of your project. It
will install `subprojects/<name>.wrap` file used by Meson to download the
dependency.
