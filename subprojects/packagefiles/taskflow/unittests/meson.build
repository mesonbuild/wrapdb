if get_option('buildtype') == 'debug' or get_option('buildtype') == 'plain'
warning('Unittests not effective when buildtype == debug or plain')
endif

unittest_list = [
    #'utility',
    'tsq',
    #'serializer ',
    'basics',
    'asyncs',
    'subflows',
    'control_flow',
    'semaphores',
    'movable',
    'cancellation',
    'algorithms',
    'compositions',
    'traversals',
    'sorting',
    'pipelines',
    'scalable_pipelines',
    'runtimes',
]

foreach test_group : unittest_list

tf_unittest_exe = executable(test_group,
    sources: [
        test_group + '.cpp',
    ],
    include_directories: '/usr/include/doctest',
    dependencies: [
        doctest_dep,
        taskflow_dep,
    ],
)

test(test_group,
    tf_unittest_exe,
    is_parallel: false,
)

endforeach