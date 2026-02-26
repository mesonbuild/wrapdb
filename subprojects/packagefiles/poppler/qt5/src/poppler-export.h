#ifndef POPPLER_QT5_EXPORT_H
#define POPPLER_QT5_EXPORT_H

#ifdef POPPLER_QT5_STATIC_DEFINE
#  define POPPLER_QT5_EXPORT
#  define POPPLER_QT5_NO_EXPORT
#else
#  ifndef POPPLER_QT5_EXPORT
#    ifdef POPPLER_QT5_EXPORTS
       /* We are building this library */
#      if defined(_MSC_VER) || defined(__MINGW32__) || defined(__MSYS__) || defined(__CYGWIN__)
#        define POPPLER_QT5_EXPORT __declspec(dllexport)
#      else
#        define POPPLER_QT5_EXPORT __attribute__((visibility("default")))
#      endif
#    else
       /* We are using this library */
#      if defined(_MSC_VER) || defined(__MINGW32__) || defined(__MSYS__) || defined(__CYGWIN__)
#        define POPPLER_QT5_EXPORT __declspec(dllimport)
#      else
#        define POPPLER_QT5_EXPORT __attribute__((visibility("default")))
#      endif
#    endif
#  endif

#  ifndef POPPLER_QT5_NO_EXPORT
#    if defined(_MSC_VER) || defined(__MINGW32__) || defined(__MSYS__) || defined(__CYGWIN__)
#      define POPPLER_QT5_NO_EXPORT
#    else
#      define POPPLER_QT5_NO_EXPORT __attribute__((visibility("hidden")))
#    endif
#  endif
#endif

#ifndef POPPLER_QT5_DEPRECATED
#  if defined(_MSC_VER) || defined(__MINGW32__) || defined(__MSYS__) || defined(__CYGWIN__)
#    define POPPLER_QT5_DEPRECATED __declspec(deprecated)
#  else
#    define POPPLER_QT5_DEPRECATED __attribute__ ((__deprecated__))
#  endif
#endif

#ifndef POPPLER_QT5_DEPRECATED_EXPORT
#  define POPPLER_QT5_DEPRECATED_EXPORT POPPLER_QT5_EXPORT POPPLER_QT5_DEPRECATED
#endif

#ifndef POPPLER_QT5_DEPRECATED_NO_EXPORT
#  define POPPLER_QT5_DEPRECATED_NO_EXPORT POPPLER_QT5_NO_EXPORT POPPLER_QT5_DEPRECATED
#endif

/* NOLINTNEXTLINE(readability-avoid-unconditional-preprocessor-if) */
#if 0 /* DEFINE_NO_DEPRECATED */
#  ifndef POPPLER_QT5_NO_DEPRECATED
#    define POPPLER_QT5_NO_DEPRECATED
#  endif
#endif

#endif
