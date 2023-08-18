if target_machine.system() != 'windows'
    error('Samples only supported on windows')
endif

vulkan = dependency('vulkan')

test(
    'Tests',
    executable(
        'tests',
        'Tests.cpp',
        include_directories: '.',
        dependencies: vma_allocator_dep,
    ),
)
