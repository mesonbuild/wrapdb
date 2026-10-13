#ifndef CPR_EXPORT_H
#define CPR_EXPORT_H

#ifdef CPR_STATIC_DEFINE
#  define CPR_EXPORT
#  define CPR_NO_EXPORT
#else
#  ifndef CPR_EXPORT
#    ifdef cpr_EXPORTS
#      if defined _WIN32 || defined __CYGWIN__
#         define CPR_EXPORT __declspec(dllexport)
#       else
#         define CPR_EXPORT __attribute__((visibility("default")))
#       endif
#    else
#      if defined _WIN32 || defined __CYGWIN__
#        define CPR_EXPORT __declspec(dllimport)
#      else
#        define CPR_EXPORT __attribute__((visibility("default")))
#       endif
#    endif
#  endif

#  ifndef CPR_NO_EXPORT
#    if defined _WIN32 || defined __CYGWIN__
#      define CPR_NO_EXPORT
#     else
#       define CPR_NO_EXPORT __attribute__((visibility("hidden")))
#     endif
#  endif
#endif

#endif /* CPR_EXPORT_H */
