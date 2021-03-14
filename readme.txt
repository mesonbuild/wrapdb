This repository contains a Meson build definition for project fluidsynth.

For more information please see http://mesonbuild.com.

For more information about fluidsynth library see https://github.com/FluidSynth/fluidsynth

This wrap DOES NOT provide full functionality of fluidsynth library, only
some features are available for now; see meson_options.txt for details.

To use this wrap:

    $ meson wrap install fluidsynth
    $ echo 'fluidsynth*' >> subprojects/.gitignore

Then create a dependency object in meson.build of your project:

    fluidsynth_dep = dependency('fluidsynth')

For meson < 0.55.0 wrap fallbacks need to be explicitly enabled:

    fluidsynth_dep = dependency('fluidsynth', fallback : ['fluidsynth', 'fluidsynth_dep'])
