all_tests = [['232c93d07b74-test', 'c', thread_dep],
             ['35fa71a030ca-test', 'c', thread_dep],
             ['500f9fbadef8-test', 'c', []],
             ['7ad0e4b2f83c-test', 'c', []],
             ['8a9973408177-test', 'c', []],
             ['917257daa0fe-test', 'c', []],
             ['a0908ae19763-test', 'c', []],
             ['a4c0b3decb33-test', 'c', []],
             ['accept-link', 'c', thread_dep],
             ['accept-reuse', 'c', []],
             ['accept-test', 'c', []],
             ['accept', 'c', []],
             ['across-fork', 'c', thread_dep],
             ['b19062a56726-test', 'c', []],
             ['b5837bd5311d-test', 'c', []],
             ['ce593a6c480a-test', 'c', thread_dep],
             ['close-opath', 'c', []],
             ['connect', 'c', []],
             ['cq-full', 'c', []],
             ['cq-overflow', 'c', []],
             ['cq-peek-batch', 'c', []],
             ['cq-ready', 'c', []],
             ['cq-size', 'c', []],
             ['d4ae271dfaae-test', 'c', []],
             ['d77a67ed5f27-test', 'c', []],
             ['defer', 'c', []],
             ['double-poll-crash', 'c', []],
             ['eeed8b54e0df-test', 'c', []],
             ['empty-eownerdead', 'c', []],
             ['eventfd-disable', 'c', []],
             ['eventfd-ring', 'c', []],
             ['eventfd', 'c', []],
             ['fadvise', 'c', []],
             ['fallocate', 'c', []],
             ['fc2a85cb02ef-test', 'c', []],
             ['file-register', 'c', []],
             ['file-update', 'c', []],
             ['files-exit-hang-poll', 'c', []],
             ['files-exit-hang-timeout', 'c', []],
             ['fixed-link', 'c', []],
             ['fsync', 'c', []],
             ['hardlink', 'c', []],
             ['io-cancel', 'c', []],
             ['io_uring_enter', 'c', []],
             ['io_uring_register', 'c', []],
             ['io_uring_setup', 'c', []],
             ['iopoll', 'c', []],
             ['lfs-openat-write', 'c', []],
             ['lfs-openat', 'c', []],
             ['link-timeout', 'c', []],
             ['link', 'c', []],
             ['link_drain', 'c', []],
             ['madvise', 'c', []],
             ['mkdir', 'c', []],
             ['multicqes_drain', 'c', []],
             ['nop-all-sizes', 'c', []],
             ['nop', 'c', []],
             ['open-close', 'c', []],
             ['openat2', 'c', []],
             ['personality', 'c', []],
             ['pipe-eof', 'c', thread_dep],
             ['pipe-reuse', 'c', []],
             ['poll-cancel-ton', 'c', []],
             ['poll-cancel', 'c', []],
             ['poll-link', 'c', thread_dep],
             ['poll-many', 'c', []],
             ['poll-mshot-update', 'c', thread_dep],
             ['poll-ring', 'c', []],
             ['poll-v-poll', 'c', thread_dep],
             ['poll', 'c', []],
             ['probe', 'c', []],
             ['read-write', 'c', []],
             ['register-restrictions', 'c', []],
             ['rename', 'c', []],
             ['ring-leak', 'c', []],
             ['ring-leak2', 'c', thread_dep],
             ['rw_merge_test', 'c', []],
             ['self', 'c', []],
             ['send_recv', 'c', thread_dep],
             ['send_recvmsg', 'c', thread_dep],
             ['shared-wq', 'c', []],
             ['short-read', 'c', []],
             ['shutdown', 'c', []],
             ['sigfd-deadlock', 'c', []],
             ['socket-rw', 'c', []],
             ['socket-rw-eagain', 'c', []],
             ['splice', 'c', []],
             ['sq-full', 'c', []],
             ['sq-poll-dup', 'c', []],
             ['sq-poll-kthread', 'c', []],
             ['sq-poll-share', 'c', []],
             ['sqpoll-disable-exit', 'c', []],
             ['sqpoll-exit-hang', 'c', []],
             ['sqpoll-cancel-hang', 'c', []],
             ['sqpoll-sleep', 'c', []],
             ['sq-space_left', 'c', []],
             ['stdout', 'c', []],
             ['submit-reuse', 'c', thread_dep],
             ['submit-link-fail', 'c', []],
             ['symlink', 'c', []],
             ['teardowns', 'c', []],
             ['thread-exit', 'c', thread_dep],
             ['timeout-new', 'c', thread_dep],
             ['timeout-overflow', 'c', []],
             ['timeout', 'c', []],
             ['unlink', 'c', []],
             ['wakeup-hang', 'c', thread_dep],
             ['sendmsg_fs_cve', 'c', []],
             ['rsrc_tags', 'c', []]]

if has_statx
    all_tests += [['statx', 'c', []]]
endif

if has_cxx
    all_tests += [['sq-full-cpp', 'cc', []]]
endif

runtests_sh = find_program('runtests.sh')
runtests_loop_sh = find_program('runtests-loop.sh')

xcflags = []
if has_stringop_overflow
    xcflags = xcflags + ['-Wstringop-overflow=0']
endif
if has_array_bounds
    xcflags = xcflags + ['-Warray-bounds=0']
endif

foreach t : all_tests
    test_name = t[0]
    test_source = t[0] + '.' + t[1]
    executable(test_name,
               [test_source, 'helpers.c'],
               c_args: xcflags,
               cpp_args: xcflags,
               include_directories : inc,
               link_with : liburing.get_static_lib(),
               dependencies : t[2],
               install : true,
               install_dir : get_option('datadir') / 'liburing-test')

    test(t[0],
         runtests_sh,
         args : t[0],
         workdir : meson.current_build_dir(),
         suite : 'once')

    test(t[0] + '_loop',
         runtests_loop_sh,
         args : t[0],
         workdir : meson.current_build_dir(),
         suite : 'loop')
endforeach

configure_file(input : 'runtests.sh',
               output: 'runtests.sh',
               copy : true)

configure_file(input : 'runtests-loop.sh',
               output: 'runtests-loop.sh',
               copy : true)

configure_file(input : 'config',
               output: 'config.local',
               copy : true)

install_data('runtests.sh',
             'runtests-loop.sh',
             install_dir : get_option('datadir') / 'liburing-test')
