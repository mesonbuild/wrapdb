add_languages('c', native: false)

utils = {
  'openal-info.c': openal_dep,
}

sndfile_dep = dependency('sndfile', required: false)
if sndfile_dep.found()
  utils += {
    'uhjdecoder.cpp': [openal_dep, sndfile_dep],
    'uhjencoder.cpp': [openal_dep, sndfile_dep],
  }
endif

foreach u, d : utils
  executable(
    u.split('.')[0],
    u,
    dependencies: d,
    link_args: cpp.get_supported_arguments('-municode'),
  )
endforeach
