This repository contains a Meson build definition for project mt32emu.

For more information please see http://mesonbuild.com.

For more information about mt32emu library see https://github.com/munt/munt.

To use this wrap:

    $ meson wrap install mt32emu
    $ echo 'munt-libmt32emu*' >> subprojects/.gitignore

Then create a dependency object in meson.build of your project:

    mt32emu_dep = dependency('mt32emu')

For meson < 0.55.0 wrap fallbacks need to be explicitly enabled:

    mt32emu_dep = dependency('mt32emu', fallback : ['mt32emu', 'mt32emu_dep'])
