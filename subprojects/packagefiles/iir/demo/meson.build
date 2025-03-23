demos = ['iirdemo', 'ecg50hzfilt']

foreach demo : demos
  executable(
    demo,
    demo + '.cpp',
    dependencies: libiir_dep,
  )
endforeach
