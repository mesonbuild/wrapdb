project(
    'debug_assert',
    'cpp',
    license: 'Zlib',
    version: '1.3.4',
    meson_version: '>= 0.54.0'
)

debug_assert_inc = include_directories('.')

debug_assert_ca = []

if get_option('no-stdio')
    debug_assert_ca += '-DDEBUG_ASSERT_NO_STDIO'
endif

if get_option('disable')
    debug_assert_ca += '-DDEBUG_ASSERT_DISABLE'
endif

o_m_a = get_option('override-mark-unreachable')
if o_m_a != 'not overridden'
    debug_assert_ca += f'-DDEBUG_ASSERT_MARK_UNREACHABLE=@o_m_a@'
endif

o_f_i = get_option('override-force-inline')
if o_f_i != 'not overridden'
    debug_assert_ca += f'-DDEBUG_ASSERT_FORCE_INLINE=@o_f_i@'
endif

debug_assert_dep = declare_dependency(
    compile_args: debug_assert_ca,
    include_directories: [debug_assert_inc],
)

meson.override_dependency('debug_assert', debug_assert_dep)
