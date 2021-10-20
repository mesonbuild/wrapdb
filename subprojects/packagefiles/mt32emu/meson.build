project('mt32emu', 'cpp',
        version : '2.5.3',
        license : 'LGPL-2.1-or-later',
        default_options : 'b_ndebug=if-release',
        meson_version : '>=0.49.0')

mt32emu_versions = meson.project_version().split('.')
mt32emu_exports_type = 3

conf_data = configuration_data()
conf_data.set('libmt32emu_VERSION',       meson.project_version())
conf_data.set('libmt32emu_VERSION_MAJOR', mt32emu_versions[0].to_int())
conf_data.set('libmt32emu_VERSION_MINOR', mt32emu_versions[1].to_int())
conf_data.set('libmt32emu_VERSION_PATCH', mt32emu_versions[2].to_int())
conf_data.set('libmt32emu_EXPORTS_TYPE',  mt32emu_exports_type)

conf_data.set('libmt32emu_SHARED_DEFINITION',     '#undef MT32EMU_SHARED')
conf_data.set('libmt32emu_WITH_VERSION_TAGGING',  0)
conf_data.set('libmt32emu_RUNTIME_VERSION_CHECK', 0)

subdir('mt32emu/src')     # all source files
subdir('include/mt32emu') # public interface

mt32emu_lib_includes = include_directories('include/mt32emu')
mt32emu_dep_includes = include_directories('include')

mt32emu_lib = library('mt32emu', mt32emu_sources,
                      include_directories : mt32emu_lib_includes,
                      cpp_args : ['-DMT32EMU_WITH_INTERNAL_RESAMPLER'])

mt32emu_dep = declare_dependency(include_directories : mt32emu_dep_includes,
                                 link_with: mt32emu_lib)
