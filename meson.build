project('zlib', 'c', version : '1.2.11', license : 'zlib')

cc = meson.get_compiler('c')

link_args = []
if cc.get_id() == 'msvc'
  add_project_arguments('-D_CRT_SECURE_NO_DEPRECATE',
    '-D_CRT_NONSTDC_NO_DEPRECATE', language : 'c')
elif cc.get_id() == 'gcc' and host_machine.system() != 'windows'
  vflag = '-Wl,--version-script,@0@/zlib.map'.format(meson.current_source_dir())
  link_args += [vflag]
endif

src = files([
  'adler32.c',
  'crc32.c',
  'deflate.c',
  'infback.c',
  'inffast.c',
  'inflate.c',
  'inftrees.c',
  'trees.c',
  'zutil.c',
  'compress.c',
  'uncompr.c',
  'gzclose.c',
  'gzlib.c',
  'gzread.c',
  'gzwrite.c'])

headers = files(['zconf.h', 'zlib.h'])

if host_machine.system() == 'windows'
  win = import('windows')
  win_args = []
  if cc.get_id() != 'msvc'
    win_args += '-DGCC_WINDRES'
  endif
  src += win.compile_resources('win32/zlib1.rc', args : win_args)
endif

zlib = library('z', src,
  link_args : link_args,
  vs_module_defs : 'win32/zlib.def',
  install : true)

incdir = include_directories('.')

zlib_dep = declare_dependency(
  link_with : zlib,
  include_directories : incdir)

install_headers(headers)

pkg = import('pkgconfig')

pkg.generate(name: 'zlib',
             description: 'zlib compression library',
             libraries: zlib)
