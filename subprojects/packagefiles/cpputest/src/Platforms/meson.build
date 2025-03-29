cpputest_platform = get_option('cpputest_platform')

if cpputest_platform != 'none'
  if cpputest_platform == 'autodetect'
    compiler_id = meson.get_compiler('cpp').get_id()
    if compiler_id == 'gcc' or compiler_id == 'clang'
      cpputest_platform = 'Gcc'
    elif compiler_id == 'msvc' or compiler_id == 'clang-cl'
      cpputest_platform = 'VisualCpp'
    else
      error(
        f'Unknown compiler ID @compiler_id@, cannot autodetect the platform.\n' + 'Define the platform manually or provide your own implementation.',
      )
    endif
  endif

  platform_source_file = files(cpputest_platform / 'UtestPlatform.cpp')
endif
