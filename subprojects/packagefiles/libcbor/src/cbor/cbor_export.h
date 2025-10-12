#ifndef CBOR_EXPORT
# if (defined(__GNUC__) && __GNUC__ >= 4) || defined(__ICC)
#  define CBOR_EXPORT __attribute__ ((visibility("default")))
# elif (defined(__SUNPRO_C) || defined(__SUNPRO_CC))
#  define CBOR_EXPORT __global
/* Windows is special and you cannot just define entry points unconditionally. */
# elif defined(_WIN32) && !defined(CBOR_BUILD_STATIC)
#  ifdef CBOR_BUILD
#   define CBOR_EXPORT __declspec(dllexport)
#  else
#   define CBOR_EXPORT __declspec(dllimport)
#  endif
# else
/* nothing else worked, give up and do nothing */
#  define CBOR_EXPORT
# endif
#endif