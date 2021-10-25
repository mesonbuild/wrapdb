project('libpng', 'c', version : '1.6.37', license : 'libpng')

png_versions = meson.project_version().split('.')
png_major_version = png_versions[0]
png_minor_version = png_versions[1]
png_micro_version = png_versions[2]
png_libname = 'png@0@@1@'.format(png_major_version, png_minor_version)
png_libversion = '@0@@1@.@2@.0'.format(png_major_version, png_minor_version, png_micro_version)

cc = meson.get_compiler('c')

include = include_directories('.')

if cc.get_define('__ANDROID__') != ''
  zlib_dep = cc.find_library('z')
else
  zlib_dep = dependency('zlib')
endif

c_args = []

if host_machine.system() == 'windows' and get_option('default_library') != 'static'
  c_args += ['-DPNG_BUILD_DLL']
endif

libpng_deps = [
        zlib_dep,
        cc.find_library('m', required : false),
]

png_src = files([
        'png.c',
        'pngerror.c',
        'pngget.c',
        'pngmem.c',
        'pngpread.c',
        'pngread.c',
        'pngrio.c',
        'pngrtran.c',
        'pngrutil.c',
        'pngset.c',
        'pngtrans.c',
        'pngwio.c',
        'pngwrite.c',
        'pngwtran.c',
        'pngwutil.c'
])


if host_machine.cpu_family() == 'aarch64' or cc.get_define('__ARM_NEON') != ''
    png_src += files([
        'arm/arm_init.c',
        'arm/filter_neon_intrinsics.c',
        'arm/palette_neon_intrinsics.c',
        
    ])
    if cc.get_id() == 'msvc'
        cl = find_program('cl')
        msvc_preprocessed_asm_files = custom_target(
            'MSVC assembly preprocessing',
            output : ['@BASENAME@.i'],
            input : 'arm/filter_neon.S',
            command : [cl, '/Fi@OUTPUT@', '/P', '@INPUT@', '-I@OUTDIR@', c_args]
        )
        msvc_armasm = find_program('armasm64')
        png_src += custom_target(
            'MSVC assembly compilation',
            output : ['@BASENAME@.obj'],
            input : msvc_preprocessed_asm_files,
            command : [msvc_armasm, '@INPUT@', '/Fo@OUTPUT@', '-I@OUTDIR@'],
        )
        # The additional __aarch64__ flag is a work-around to get the same
        # behavior for arm64 on Windows as on Linux.
        # This work-around should be eliminated if the this issue is fixed:
        # https://github.com/glennrp/libpng/issues/398
        c_args += ['-D__aarch64__']
    else
        png_src += files(['arm/filter_neon.S'])    
    endif

    c_args += ['-DPNG_ARM_NEON_OPT=2']
endif

libpng = library(png_libname,
    png_src,
    version : png_libversion,
    dependencies : libpng_deps,
    c_args: c_args,
    install: true,
)

pngincsubdir = 'lib' + png_libname
pngincludedir = join_paths(get_option('includedir'), pngincsubdir)

configure_file(
    input : 'scripts/pnglibconf.h.prebuilt',
    output : 'pnglibconf.h',
    copy: true,
    install_dir : pngincludedir,
    install: true
)

install_headers('png.h', 'pngconf.h', subdir : pngincsubdir)

cdata = configuration_data()
cdata.set('prefix', get_option('prefix'))
cdata.set('exec_prefix', get_option('prefix'))
cdata.set('libdir', '${prefix}/' + get_option('libdir'))
cdata.set('includedir', '${prefix}/' + get_option('includedir'))
cdata.set('PNGLIB_MAJOR', png_major_version)
cdata.set('PNGLIB_MINOR', png_minor_version)
cdata.set('PNGLIB_VERSION', meson.project_version())
# FIXME: should auto-generate pkg-config file to get this right
cdata.set('LIBS', '-lz')

configure_file(
    input : 'libpng.pc.in',
    output : 'libpng16.pc',
    configuration : cdata,
    install_dir : join_paths(get_option('libdir'), 'pkgconfig'),
    install : true,
)

# FIXME: this should be a symlink to libpng16.pc
configure_file(
    input : 'libpng.pc.in',
    output : 'libpng.pc',
    configuration : cdata,
    install_dir : join_paths(get_option('libdir'), 'pkgconfig'),
    install : true,
)

libpng_dep = declare_dependency(
    include_directories : include,
    link_with : libpng,
    dependencies : libpng_deps,
)
# Keep the older dependency name for backwards-compat with old-style
# dependency(..., fallback ['libpng': 'png_dep'])
png_dep = libpng_dep

png_test = executable('pngtest', 'pngtest.c', dependencies : libpng_dep)
test('pngtest', png_test, args : files('pngtest.png'))
