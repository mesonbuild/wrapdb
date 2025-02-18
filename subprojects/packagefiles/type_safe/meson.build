project(
    'type_safe',
    'cpp',
    license: 'MIT',
    version: '0.2.4',
    meson_version: '>= 0.59.0',
)

da_dep = dependency('debug_assert')

b_ndebug = get_option('b_ndebug')
if (
    b_ndebug == 'true'
    or (
        b_ndebug == 'if-release'
        and get_option('buildtype') in ['release', 'plain']
    )
)
    ndebug = true
else
    ndebug = false
endif

assertions_opt = get_option('assertions')
enable_assertions = assertions_opt.disable_auto_if(ndebug).allowed() ? 1 : 0
precond_checks = get_option('preconditions') ? 1 : 0
enable_wrappers = get_option('wrappers') ? 1 : 0

arithmetic_policy_s = get_option('arithmetic-policy')
if arithmetic_policy_s == 'default'
    arithmetic_policy = 0
elif arithmetic_policy_s == 'ub'
    arithmetic_policy = 1
elif arithmetic_policy_s == 'checked'
    arithmetic_policy = 2
else
    error('a new option for arithmetic-policy must have been added without changing meson.build')
endif

comp_args = [
    f'-DTYPE_SAFE_ENABLE_ASSERTIONS=@enable_assertions@',
    f'-DTYPE_SAFE_ENABLE_PRECONDITION_CHECKS=@precond_checks@',
    f'-DTYPE_SAFE_ENABLE_WRAPPER=@enable_wrappers@',
    f'-DTYPE_SAFE_ARITHMETIC_POLICY=@arithmetic_policy@',
]

cxx = meson.get_compiler('cpp')
if cxx.get_id() == 'msvc'
    comp_args += '/wd4800'
endif

type_safe_dep = declare_dependency(
    compile_args: comp_args,
    dependencies: [da_dep],
    include_directories: include_directories('include'),
)

meson.override_dependency('type_safe', type_safe_dep)
