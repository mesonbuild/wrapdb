project(
  'openjp2',
  'c',
  'cpp',
  version: '2.5.3',
  meson_version: '>= 0.55.0',
  default_options: ['buildtype=debugoptimized', 'c_std=c99'],
)

cc = meson.get_compiler('c')
cxx = meson.get_compiler('cpp')
host_system = host_machine.system()
host_cpu = host_machine.cpu_family()

fs = import('fs')

openjpeg_version_parts = meson.project_version().split('.')
openjpeg_version_major = openjpeg_version_parts[0]
openjpeg_version_minor = openjpeg_version_parts[1]
openjpeg_version_build = openjpeg_version_parts[2]

openjpeg_version_subdir = 'openjpeg-@0@.@1@'.format(
  openjpeg_version_major,
  openjpeg_version_minor,
)

m_dep = cc.find_library('m', required: false)
pthread_dep = dependency('threads', required: false)
rt_dep = cc.find_library('rt', required: false)

wxwidgets_dep = dependency('wxWidgets', required: get_option('build_viewer'))

opj_static_args = []
if host_system == 'windows'
  if get_option('default_library') == 'static'
    opj_static_args += '-DOPJ_STATIC'
    add_project_arguments(opj_static_args, language: 'c')
  else
    add_project_arguments('-DOPJ_EXPORTS', language: 'c')
  endif
endif

#-----------------------------------------------------------------------------
# Build Library
curl_dep = dependency('libcurl', version: '>= 7.55.0', required: get_option('build_jpip_server'))
fcgi_dep = dependency('fcgi', required: get_option('build_jpip_server'))

subdir('src/lib')

#-----------------------------------------------------------------------------
# Build Applications

if get_option('build_codec_apps')
  # OFF: It will only build 3rd party libs if they are not found on the system
  # ON: 3rd party libs will ALWAYS be build, and used
  subdir('src/bin')
endif
