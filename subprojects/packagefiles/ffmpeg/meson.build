project('FFMpeg', 'c')

mod = import('unstable-external_project')

p = mod.add_project('configure',
  configure_options : ['--prefix=@PREFIX@'],
)

libavcodec_dep = p.dependency('avcodec')
libavdevice_dep = p.dependency('avdevice')
libavfilter_dep = p.dependency('avfilter')
libavformat_dep = p.dependency('avformat')
libavutil_dep = p.dependency('avutil')
libpostproc_dep = p.dependency('postproc')
libswresample_dep = p.dependency('swresample')
libswscale_dep = p.dependency('swscale')
meson.override_dependency('avcodec', libavcodec_dep)
meson.override_dependency('avdevice', libavdevice_dep)
meson.override_dependency('avfilter', libavfilter_dep)
meson.override_dependency('avformat', libavformat_dep)
meson.override_dependency('avutil', libavutil_dep)
meson.override_dependency('postproc', libpostproc_dep)
meson.override_dependency('swresample', libswresample_dep)
meson.override_dependency('swscale', libswscale_dep)
