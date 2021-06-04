# When libsrtp is built as a subproject, this gathers all header files into
# 'srtp2' directory that libsrtp2_dep is then able to find through its
# include_directories. It allows the parent project to for example
# #include <srtp2/srtp.h> as it would normally do with a properly installed
# libsrtp that has the header files in /usr/include/srtp2 or a similar location.

foreach header: libsrtp2_headers
  configure_file(input : header, output : '@PLAINNAME@', copy: true)
endforeach
