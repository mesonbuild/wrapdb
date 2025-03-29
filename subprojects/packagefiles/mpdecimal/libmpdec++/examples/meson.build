examples = ['factorial', 'pi']

foreach example : examples
  executable(
    example,
    '@0@.cc'.format(example),
    dependencies: mpdecpp_dep,
  )
endforeach
