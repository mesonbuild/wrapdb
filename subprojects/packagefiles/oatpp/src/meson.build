subdir('oatpp')

inc_dirs += include_directories('.')

deps += dependency('threads')


is_mingw = cpp.get_id() == 'gcc' and host_machine.system() == 'windows'
is_msvc_or_similar = cpp.get_id() == 'msvc' or cpp.get_id() == 'clang-cl'
is_msys2 = (
    is_mingw
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


cmake = import('cmake')


oatpp_modules = ['oatp', 'oatpp-test']

oatpp_modules_flat = ''
foreach index : range(oatpp_modules.length())
    oatpp_module = oatpp_modules.get(index)
    if index >= 1
        oatpp_modules_flat += ''
    endif
    oatpp_modules_flat += oatpp_module
endforeach


foreach oatpp_module : oatpp_modules
    conf = configuration_data()
    conf.set_quoted('OATPP_THIS_MODULE_NAME', 'oatpp') ## name of the module (also name of folders in installation dirs)
    conf.set_quoted('OATPP_THIS_MODULE_VERSION', meson.project_version()) ## version of the module (also sufix of folders in installation dirs)
    conf.set_quoted('OATPP_THIS_MODULE_LIBRARIES', oatpp_modules_flat) ## list of libraries to find when find_package is called
    conf.set_quoted('OATPP_THIS_MODULE_TARGETS', oatpp_modules_flat) ## list of targets to install
    conf.set_quoted('OATPP_THIS_MODULE_DIRECTORIES', oatpp_modules_flat) ## list of directories to install

    conf.set_quoted('OATPP_MODULE_NAME', oatpp_module)

    cmake.configure_package_config_file(
        name: oatpp_module + 'Config.cmake',
        input: '../cmake/module-config.cmake.in',
        configuration: conf,
    )
endforeach


