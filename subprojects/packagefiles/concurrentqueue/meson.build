project(
    # moodycamel::ConcurrentQueue
    'concurrentqueue',
    ['cpp'],
    # Dual licensing
    license: ['symplified-BSD', 'Boost 1.0'],
    version: '1.0.3',
)

concurrentqueue_dep = declare_dependency(

    # it should be better if it was in a subdirectory
    # like moodycamel/ConcurrentQueue
    include_directories: [include_directories('.')],
)
