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

### Getting Started

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

### Wrap Release Meta

Add your release information in `releases.json`. It is a dictionary where the
key is the wrap name and the value is a dictionary containing with the following keys:

| Option            | Description                                                                                                                                                                                |
|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `versions`        | Sorted list (newest first) of release tags in the format `<upstream version>-<revision>` where the revision starts at 1 and is incremented when a change is made in the meson port.         |
| `dependency_names`| (Optional) List of dependency names (e.g. pkg-config name such as `glib-2.0`) provided by the wrap. It must match information from wrap's `[provide]` section.                              |
| `program_names`   | (Optional) List of program names (e.g. `glib-compile-resources`) provided by the wrap. It must match information from wrap's `[provide]` section.                                           |

### CI Configure Meta

Configure CI in `ci_config.json`. It is a dictionary where the key is the wrap
name and the value is a dictionary containing with the following keys:

| Option                  | Description                                                                                                                                                                                                                                                                                          |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `build_options`         | (Optional) List of `<your subproject>:option=value` strings that will be used to build the project on the CI.                                                                                                                                                                                        |
| `build_on`              | (Optional) Dictionary of platforms not supported by the project, written as `{"platform-name": false}`.                                                                                                                                                                                              |
| `alpine_packages`       | (Optional) List of extra packages that will be installed on Alpine Linux CI runners.                                                                                                                                                                                                                 |
| `brew_packages`         | (Optional) List of extra packages that will be installed on MacOS CI runners.                                                                                                                                                                                                                        |
| `choco_packages`        | (Optional) List of extra packages that will be installed on Windows CI runners.                                                                                                                                                                                                                      |
| `debian_packages`       | (Optional) List of extra packages that will be installed on Debian-like CI runners. Dependencies that can be provided by other wraps should not be added here because it's better to test that fallbacks work. When running `tools/sanity_checks.py` locally, this list will be printed but not installed. |
| `msys_packages`         | (Optional) List of extra packages that will be installed on MSYS CI runners.                                                                                                                                                                                                                         |
| `python_packages`       | (Optional) List of extra Python packages that will be installed on all CI runners.                                                                                                                                                                                                                   |
| `fatal_warnings`        | (Optional) If set to `false` removes `--fatal-meson-warnings`. Use this only when there is no other way to fix the warning.                                                                                                                                                                             |
| `has_provides`          | (Optional) If set to `false`, the project will not be expected to declare any dependency or program names, e.g. for projects that only provide plugins for another project.                                                                                                                          |
| `skip_dependency_check` | (Optional) List of platform-specific dependency names that are not always provided by the project.                                                                                                                                                                                                   |
| `skip_program_check`    | (Optional) List of platform-specific program names that are not always provided by the project.                                                                                                                                                                                                      |
| `test_options`          | (Optional) List of arguments that will be passed to `meson test` command (e.g. `--timeout-multiplier`, `--no-suite`).                                                                                                                                                                                |
| `skip_tests`            | (Optional) If set to `true` tests will not be run. This is useful when tests are known to fail because of upstream issues, or require a specific environment hard to set up.                                                                                                                         |
| `ignore_upstream_meson` | (Optional) Allow wrap to override an upstream Meson config, but only in the specified upstream version. This is useful when adding a wrap with buggy upstream Meson code while awaiting upstream fixes.                                                                                              |

### Running sanity test locally

- Test locally by running `tools/sanity_checks.py` script. It will be executed
  on the CI and must always return success before merging any PR.

- Create Pull Request with your changes.

## How to import one of those wraps into my project

Run `meson wrap install <name>` on the top source dir of your project. It
will install `subprojects/<name>.wrap` file used by Meson to download the
dependency. For more information on the wrap command refer to the [documentation](https://mesonbuild.com/Commands.html#wrap).
