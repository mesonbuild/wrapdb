cdata = configuration_data()

versionstr = meson.project_version()
varr = versionstr.split('.')
major = varr[0]
minor = varr[1]
micro = varr[2]

verint = 10000*major.to_int() + 100*minor.to_int() + micro.to_int()

cdata.set('VERSION', versionstr)
cdata.set('LIBXSLT_VERSION_NUMBER', verint)
cdata.set('WITH_XSLT_DEBUG', 0)
cdata.set('WITH_MEM_DEBUG', 0)
cdata.set('WITH_TRIO', 0)
cdata.set('WITH_DEBUGGER', 0)
cdata.set('WITH_PROFILER', 0)
cdata.set('WITH_MODULES', 0)

configure_file(input: 'xsltconfig.h.in',
  output: 'xsltconfig.h',
  configuration: cdata)
