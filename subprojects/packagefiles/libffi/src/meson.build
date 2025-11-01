ffi_c_sources = [
  'prep_cif.c',
  'types.c',
  'raw_api.c',
  'java_raw_api.c',
  'closures.c',
  'tramp.c',
]

ffi_asm_sources = []

if get_option('ffi-debug')
  ffi_c_sources += ['debug.c']
endif

# Translate source files to source paths
foreach f : c_sources
  ffi_c_sources += targetdir / f
endforeach
foreach f : asm_sources
  ffi_asm_sources += targetdir / f
endforeach

ffiinc = include_directories('..', '../include', targetdir)

if is_msvc
  # MSVC, cannot compile assembly files directly. They need to be preprocessed
  # with the C compiler first, then compiled with MASM.
  if meson.version().version_compare('<0.64.0')
    error('Meson >= 0.64 is required with MSVC')
  elif meson.version().version_compare('<1.10.0') and host_cpu_family == 'aarch64'
    # Custom logic to invoke armasm64 with Meson < 1.10.0.
    # Works around an issue with depfile support:
    # https://github.com/mesonbuild/wrapdb/issues/2469
    cl = find_program('cl')
    armasm64 = find_program('armasm64')

    assembler_args = [armasm64, '-o', '@OUTPUT@', '@INPUT@']
    if get_option('buildtype').startswith('debug')
      assembler_args += ['-g']
    endif

    ffi_asm_objs = []
    foreach asm_source : ffi_asm_sources
      incflags = [
        '/I' + join_paths(meson.current_source_dir(), '..'),
        '/I' + join_paths(meson.current_build_dir(), '..'),
        '/I' + join_paths(meson.current_source_dir(), '..', 'include'),
        '/I' + join_paths(meson.current_build_dir(), '..', 'include'),
        '/I' + join_paths(meson.current_source_dir(), targetdir),
        '/I' + join_paths(meson.current_build_dir(), targetdir),
      ]
      preproc_name = asm_source.underscorify() + '.i'
      obj_name = asm_source.underscorify() + '.obj'
      preproc = custom_target(
        preproc_name,
        input: asm_source,
        output: preproc_name,
        command: [
          cl,
          '/nologo',
          '/EP',
          '/P',
          '/Fi@OUTPUT@',
          '-D' + target,
          '@INPUT@',
        ] + incflags,
      )
      ffi_asm_objs += custom_target(
        obj_name,
        input: preproc,
        output: obj_name,
        command: assembler_args,
      )
    endforeach
    ffi_asm_sources = ffi_asm_objs
  else
    ffi_asm_sources = cc.preprocess(
      ffi_asm_sources,
      output: '@BASENAME@.masm',
      include_directories: ffiinc,
    )
    add_languages(
      'masm',
      native: false,
    )
  endif
endif

ffi_link_args = []
ffi_map_file = []

if get_option('ffi-build-versioned')
  libffi_map_in = meson.project_source_root() / 'libffi.map.in'
  arg_prefix = '-Wl,--version-script='
  if cc.has_multi_link_arguments(['-shared', arg_prefix + libffi_map_in])
    if meson.version().version_compare('>=1.3.2')
      ffi_map_file = cc.preprocess(
        libffi_map_in,
        output: '@BASENAME@',
        include_directories: ffiinc,
        compile_args: ['-DGENERATE_LIBFFI_MAP', '-D' + target],
      )
      ffi_map_abs = ffi_map_file[0].full_path()
    else
      ffi_map_file = configure_file(
        output: 'libffi.map',
        command: [
          meson.get_compiler('c'),
          get_option('c_args'),
          '-I' + join_paths(meson.current_build_dir(), '..'),
          '-I' + join_paths(meson.current_build_dir(), '..', 'include'),
          '-I' + join_paths(meson.current_source_dir(), targetdir),
          '-DGENERATE_LIBFFI_MAP',
          '-D' + target,
          '-E',
          '-x',
          'assembler-with-cpp',
          join_paths(meson.current_source_dir(), '../libffi.map.in'),
          '-o',
          '@OUTPUT@',
        ],
      )
      ffi_map_abs = meson.current_build_dir() / 'libffi.map'
    endif
    ffi_link_args += arg_prefix + ffi_map_abs
  endif
endif

public_c_args = []
if get_option('default_library') == 'static'
  public_c_args += ['-DFFI_STATIC_BUILD']
endif

# masm_args is new in Meson 0.64, older versions fails when passing unknown
# keyword arguments. We only need it when using MSVC which already requires
# Meson >= 0.64 above, this tricks avoids passing it to older versions.
extra_kwargs = {}
if meson.version().version_compare('>=0.64.0')
  extra_kwargs += {
    'masm_args': masm_args,
  }
endif

ffi_lib = library(
  'ffi',
  ffi_c_sources,
  ffi_asm_sources,
  c_args: ['-DFFI_BUILDING_DLL', public_c_args, private_c_args],
  include_directories: ffiinc,
  link_args: ffi_link_args,
  link_depends: ffi_map_file,
  version: ffi_version,
  soversion: ffi_soversion,
  darwin_versions: ffi_darwin_versions,
  install: true,
  kwargs: extra_kwargs,
)

pkgconf = import('pkgconfig')
pkgconf.generate(
  ffi_lib,
  description: 'Library supporting Foreign Function Interfaces',
  filebase: 'libffi',
  extra_cflags: public_c_args,
)

ffi_dep = declare_dependency(
  link_with: ffi_lib,
  compile_args: public_c_args,
  include_directories: ffiinc,
)

meson.override_dependency('libffi', ffi_dep)
