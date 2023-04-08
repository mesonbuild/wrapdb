// Modified manually for Meson wrap

#ifndef GLBINDING_API_H
#define GLBINDING_API_H

#ifdef GLBINDING_STATIC_DEFINE
#  define GLBINDING_API
#  define GLBINDING_NO_EXPORT
#else
#  ifndef GLBINDING_API
#    ifdef _MSC_VER
#      ifdef glbinding_EXPORTS
          /* We are building this library */
#        define GLBINDING_API __declspec(dllexport)
#      else
          /* We are using this library */
#        define GLBINDING_API __declspec(dllimport)
#      endif
#    else
#      define GLBINDING_API __attribute__((visibility("default")))
#    endif
#  endif

#  ifndef GLBINDING_NO_EXPORT
#    ifdef _MSC_VER
#      define GLBINDING_NO_EXPORT __attribute__((visibility("hidden")))
#    else
#      define GLBINDING_NO_EXPORT
#    endif
#  endif
#endif

#ifndef GLBINDING_DEPRECATED
#  ifndef _MSC_VER
#    define GLBINDING_DEPRECATED __attribute__ ((__deprecated__))
#  else
#    define GLBINDING_DEPRECATED __declspec(deprecated)
#  endif
#endif

#ifndef GLBINDING_DEPRECATED_EXPORT
#  define GLBINDING_DEPRECATED_EXPORT GLBINDING_API GLBINDING_DEPRECATED
#endif

#ifndef GLBINDING_DEPRECATED_NO_EXPORT
#  define GLBINDING_DEPRECATED_NO_EXPORT GLBINDING_NO_EXPORT GLBINDING_DEPRECATED
#endif

#if 0 /* DEFINE_NO_DEPRECATED */
#  ifndef GLBINDING_NO_DEPRECATED
#    define GLBINDING_NO_DEPRECATED
#  endif
#endif

#endif /* GLBINDING_API_H */
