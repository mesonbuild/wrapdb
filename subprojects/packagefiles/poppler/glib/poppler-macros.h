#ifndef POPPLER_PUBLIC_H
#define POPPLER_PUBLIC_H

#ifdef POPPLER_GLIB_STATIC_DEFINE
#  define POPPLER_PUBLIC
#  define POPPLER_GLIB_NO_EXPORT
#else
#  ifndef POPPLER_PUBLIC
#    ifdef poppler_glib_EXPORTS
       /* We are building this library */
#      if defined(_MSC_VER) || defined(__MINGW32__) || defined(__MSYS__) || defined(__CYGWIN__)
#        define POPPLER_PUBLIC __declspec(dllexport)
#      else
#        define POPPLER_PUBLIC __attribute__((visibility("default")))
#      endif
#    else
       /* We are using this library */
#      if defined(_MSC_VER) || defined(__MINGW32__) || defined(__MSYS__) || defined(__CYGWIN__)
#        define POPPLER_PUBLIC __declspec(dllimport)
#      else
#        define POPPLER_PUBLIC __attribute__((visibility("default")))
#      endif
#    endif
#  endif

#  ifndef POPPLER_GLIB_NO_EXPORT
#    if defined(_MSC_VER) || defined(__MINGW32__) || defined(__MSYS__) || defined(__CYGWIN__)
#      define POPPLER_GLIB_NO_EXPORT
#    else
#      define POPPLER_GLIB_NO_EXPORT __attribute__((visibility("hidden")))
#    endif
#  endif
#endif

#ifndef POPPLER_GLIB_DEPRECATED
#  if defined(_MSC_VER) || defined(__MINGW32__) || defined(__MSYS__) || defined(__CYGWIN__)
#    define POPPLER_GLIB_DEPRECATED __declspec(deprecated)
#  else
#    define POPPLER_GLIB_DEPRECATED __attribute__ ((__deprecated__))
#  endif
#endif

#ifndef POPPLER_GLIB_DEPRECATED_EXPORT
#  define POPPLER_GLIB_DEPRECATED_EXPORT POPPLER_GLIB_EXPORT POPPLER_GLIB_DEPRECATED
#endif

#ifndef POPPLER_GLIB_DEPRECATED_NO_EXPORT
#  define POPPLER_GLIB_DEPRECATED_NO_EXPORT POPPLER_GLIB_NO_EXPORT POPPLER_GLIB_DEPRECATED
#endif

/* NOLINTNEXTLINE(readability-avoid-unconditional-preprocessor-if) */
#if 0 /* DEFINE_NO_DEPRECATED */
#  ifndef POPPLER_GLIB_NO_DEPRECATED
#    define POPPLER_GLIB_NO_DEPRECATED
#  endif
#endif

#endif
