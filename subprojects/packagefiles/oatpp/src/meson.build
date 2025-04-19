subdir('oatpp')

inc_dirs += include_directories('.')

deps += dependency('threads')


is_mingw = cpp.get_id() == 'gcc' and host_machine.system() == 'windows'
is_msvc_or_similar = cpp.get_id() == 'msvc' or cpp.get_id() == 'clang-cl'
is_msys2 = (is_mingw
or (host_machine.system() == 'windows'
and cpp.get_id() == 'clang')
)
if is_msvc_or_similar or is_msys2
  deps += cpp.find_library('wsock32')
  deps += cpp.find_library('ws2_32')
elif (host_machine.system() != 'darwin' and host_machine.system() != 'freebsd')
  if get_option('link_atomic')
    deps += cpp.find_library('atomic')
  endif
endif


subdir('oatpp-test')

test_module_inc_dirs += include_directories('.')


