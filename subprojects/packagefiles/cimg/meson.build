project(
  'cimg',
  'cpp',
  version: '3.2.3',
  meson_version: '>=0.59.0',
  default_options: ['werror=false']
)

cpp = meson.get_compiler('cpp')

deps = [dependency('threads')]
compile_args = []

if host_machine.system() == 'windows'
  # This helps in certain environments like msys2
  compile_args += '-Dcimg_OS=2'
endif

# Feature option/define name : library name
simple_deps = {
  'opencv'  : 'OpenCV', # CMake module
  'zlib'    : 'zlib',
  'curl'    : 'libcurl',
  'lapack'  : 'lapack',
  'magick'  : 'Magick++',

  'png'     : 'libpng',
  'jpeg'    : 'libjpeg',
  'tiff'    : 'libtiff-4',
  'heif'    : 'libheif',
  'openexr' : 'OpenEXR', # CMake module
}

foreach depname, libname: simple_deps
  library_dep = dependency(libname, required: get_option(depname))
  if library_dep.found()
    deps += library_dep
    compile_args += '-Dcimg_use_@0@'.format(depname)
  endif
endforeach

# Do not define macro to zero if not found - it's broken
openmp_dep = dependency('openmp', required: get_option('openmp'))
if openmp_dep.found()
  deps += openmp_dep
endif

# FFTW3 requires us to link to an additional library
fftw3_dep = dependency('fftw3', required: get_option('fftw3'))
if fftw3_dep.found()
  fftw3_theads_dep = cpp.find_library('fftw3_threads', required: get_option('fftw3'))
  if fftw3_theads_dep.found()
    deps += [fftw3_dep, fftw3_theads_dep]
    compile_args += '-Dcimg_use_fftw3'
  endif
endif

# Windowing system configuration
windowing_opt = get_option('display')
windowing_required = true
windowing_found = false

if windowing_opt == 'auto'
  windowing_opt = host_machine.system() == 'windows' ? 'GDI32' : 'X11'
  windowing_required = false
endif

if windowing_opt == 'X11'
  x11_dep = dependency('x11', required: windowing_required)
  if x11_dep.found()
    deps += x11_dep
    compile_args += '-Dcimg_display=1'
    windowing_found = true

    x11_extras = {
      'xshm' : 'xext',
      'xrandr' : 'xrandr',
    }

    foreach depname, libname: x11_extras
      library_dep = dependency(libname, required: get_option(depname))
      if library_dep.found()
        deps += library_dep
        compile_args += '-Dcimg_use_@0@'.format(depname)
      endif
    endforeach
  endif
elif windowing_opt == 'GDI32'
  gdi32_dep = cpp.find_library('gdi32', required: windowing_required)
  if gdi32_dep.found()
    deps += gdi32_dep
    compile_args += '-Dcimg_display=2'
    windowing_found = true
  endif
endif

if not windowing_found
  compile_args += '-Dcimg_display=0'
endif

# Logging settings

veborsity_opt = get_option('veborsity')

if veborsity_opt == 'quiet'
  compile_args += '-Dcimg_verbosity=0'
elif veborsity_opt == 'normal_console'
  compile_args += '-Dcimg_verbosity=1'
elif veborsity_opt == 'normal_gui'
  compile_args += '-Dcimg_verbosity=2'
elif veborsity_opt == 'veborse_console'
  compile_args += '-Dcimg_verbosity=3'
elif veborsity_opt == 'veborse_gui'
  compile_args += '-Dcimg_verbosity=4'
endif

if host_machine.system() != 'windows' ? get_option('colorize_log').enabled() : get_option('colorize_log').allowed()
  compile_args += '-Dcimg_use_vt100'
endif

depinc = include_directories('.')
cimg_dep = declare_dependency(
  include_directories: depinc,
  dependencies: deps,
  compile_args: compile_args,
)

if get_option('examples')
  subdir('examples')
endif
