project(
    'msgpackc-cxx', 'cpp',
    version: '5.0.0',
    meson_version: '>=0.42.0'
)

args = []
if get_option('x3_parse')
    args += ['-DMSGPACK_USE_X3_PARSE']
endif
if host_machine.cpu_family() == 'sparc'
    args += ['-DMSGPACK_ZONE_ALIGN=8']
endif

msgpackc_cxx_dep = declare_dependency(
    compile_args: args,
    include_directories: include_directories('include'),
    dependencies: dependency('boost'),
)

if meson.version().version_compare('>=0.54.0')
    meson.override_dependency('msgpackc-cxx', msgpackc_cxx_dep)
endif

if get_option('tests')
    subdir('test')
endif
