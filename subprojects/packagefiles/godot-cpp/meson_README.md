# godot-cpp for Meson

godot-cpp version `4.5-stable` was the last version where godot-cpp and Godot were released with matching versions.
Now the two are versioned independently.
For example, godot-cpp `10.0.0` is able to generate cpp bindings for target Godot versions {`4.3`, `4.4`, `4.5`, `4.6`, and `4.7`}.

The meson option `api_version` is used to specify the Godot target version for generation.
The option's default is the lastest version available.

## How It Works

### Source Generation
In this wrap, per-version source generation is performed by invoking a python script (`meson-bindings-generator.py`) which in turn uses godot-cpp's own python file (`binding_generator.py`).
Generation requires two json files which can both be found in the subdir `gdextension` of the package:
  - `extension_api-{version}.json` for the specific target version.
  - `gdextension_interface.json` common for all versions.

The sources generated are then placed under a version-named directory.
This is to avoid mixing generated sources between versions should the user decide to generate different ones.
The wrap simply checks if the version-named directory already exists, and if it does not, generation of the required source files is triggered.

### Source Lists
The subdirectory `meson_sources` contains separate meson.build files that list the expected sources for each version which are combined into a per-version map.
Since the lists are long (~1K files for each target version), they have been placed in different files for ease of readability and maintenance.


## How To Update To A Newer Release
Besides updating the wrapfile, `releases.json`, and main `meson.build` with the new godot-cpp version:

1. Modify `meson_options.txt`. Look inside the package's `gdextension` directory to find the available generation jsons and:
    - Update the set of available options.
    - Set the latest version available as default.
2. Check and update the contents of the `meson_sources` directory:
    - Update the `generated_sources_map` in `meson_sources/meson.build` with the set of versions of the previous step
    - Check and update if necessary the `common_sources` list.
    E.g. by running the following from inside the package directory (Linux)
        ```
        find ./src -type f -printf '%P,\n' | sort
        ``` 
    - For each version subdirectory, check and update the expected per-version sources lists.
      This can be achieved by generating through setting up the wrap, then running the following from inside the package directory (Linux):
      ```
      find ./{insert-version-string-here} -type f -printf '%P,\n' | sort
      ```
3. Setup and check successful compilation __for all__ `api_version` option possibilities.
    From the wrapdb root:
    ```
    meson setup builddir -Dwraps=godot-cpp -Dgodot-cpp:api_version={insert-version-string-here}
    meson compile -C builddir
    ```
    In addition, remove `-Dgodot-cpp:api_version={insert-version-string-here}` and check whether the default option value is set correctly to the latest available version.

## Acknowledgement
- `v-for-vandal` for the initial wrap creation, updates, and useful tips. They mentioned that they got the original wrap file from somewhere in the internet and they don't know the original author.

