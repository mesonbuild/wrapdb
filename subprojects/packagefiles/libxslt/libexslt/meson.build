cdata = configuration_data()

cdata.set('VERSION', versionstr)
cdata.set('LIBEXSLT_VERSION_NUMBER', verint)
cdata.set('WITH_XSLT_DEBUG', 0)
cdata.set('WITH_MEM_DEBUG', 0)
cdata.set('WITH_TRIO', 0)
cdata.set('WITH_DEBUGGER', 0)
cdata.set('WITH_PROFILER', 0)
cdata.set('WITH_MODULES', 0)

cdata.set('WITH_CRYPTO', 0)

configure_file(input: 'exsltconfig.h.in',
  output: 'exsltconfig.h',
  configuration: cdata)
