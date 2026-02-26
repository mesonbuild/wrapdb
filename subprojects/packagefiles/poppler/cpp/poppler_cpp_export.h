#ifndef POPPLER_CPP_EXPORT_H
#define POPPLER_CPP_EXPORT_H

#ifdef POPPLER_CPP_STATIC_DEFINE
#  define POPPLER_CPP_EXPORT
#  define POPPLER_CPP_NO_EXPORT
#else
#  ifndef POPPLER_CPP_EXPORT
#    ifdef POPPLER_CPP_EXPORTS
        /* We are building this library */
#      if defined(_MSC_VER) || defined(__MINGW32__) || defined(__MSYS__) || defined(__CYGWIN__)
#        define POPPLER_CPP_EXPORT __declspec(dllexport)
#      else
#        define POPPLER_CPP_EXPORT __attribute__((visibility("default")))
#      endif
#    else
        /* We are using this library */
#      if defined(_MSC_VER) || defined(__MINGW32__) || defined(__MSYS__) || defined(__CYGWIN__)
#        define POPPLER_CPP_EXPORT __declspec(dllimport)
#      else
#        define POPPLER_CPP_EXPORT __attribute__((visibility("default")))
#      endif
#    endif
#  endif

#  ifndef POPPLER_CPP_NO_EXPORT
#    if defined(_MSC_VER) || defined(__MINGW32__) || defined(__MSYS__) || defined(__CYGWIN__)
#      define POPPLER_CPP_NO_EXPORT
#    else
#      define POPPLER_CPP_NO_EXPORT __attribute__((visibility("hidden")))
#    endif
#  endif
#endif

#ifndef POPPLER_CPP_DEPRECATED
#  if defined(_MSC_VER) || defined(__MINGW32__) || defined(__MSYS__) || defined(__CYGWIN__)
#    define POPPLER_CPP_DEPRECATED __declspec(deprecated)
#  else
#    define POPPLER_CPP_DEPRECATED __attribute__ ((__deprecated__))
#  endif
#endif

#ifndef POPPLER_CPP_DEPRECATED_EXPORT
#  define POPPLER_CPP_DEPRECATED_EXPORT POPPLER_CPP_EXPORT POPPLER_CPP_DEPRECATED
#endif

#ifndef POPPLER_CPP_DEPRECATED_NO_EXPORT
#  define POPPLER_CPP_DEPRECATED_NO_EXPORT POPPLER_CPP_NO_EXPORT POPPLER_CPP_DEPRECATED
#endif

/* NOLINTNEXTLINE(readability-avoid-unconditional-preprocessor-if) */
#if 0 /* DEFINE_NO_DEPRECATED */
#  ifndef POPPLER_CPP_NO_DEPRECATED
#    define POPPLER_CPP_NO_DEPRECATED
#  endif
#endif

#endif /* POPPLER_CPP_EXPORT_H */
