
// This is a generated file. Do not edit!

#ifndef GLBINDING_AUX_COMPILER_DETECTION_H
#define GLBINDING_AUX_COMPILER_DETECTION_H

#ifdef __cplusplus
# define GLBINDING_AUX_COMPILER_IS_Comeau 0
# define GLBINDING_AUX_COMPILER_IS_Intel 0
# define GLBINDING_AUX_COMPILER_IS_IntelLLVM 0
# define GLBINDING_AUX_COMPILER_IS_PathScale 0
# define GLBINDING_AUX_COMPILER_IS_Embarcadero 0
# define GLBINDING_AUX_COMPILER_IS_Borland 0
# define GLBINDING_AUX_COMPILER_IS_Watcom 0
# define GLBINDING_AUX_COMPILER_IS_OpenWatcom 0
# define GLBINDING_AUX_COMPILER_IS_SunPro 0
# define GLBINDING_AUX_COMPILER_IS_HP 0
# define GLBINDING_AUX_COMPILER_IS_Compaq 0
# define GLBINDING_AUX_COMPILER_IS_zOS 0
# define GLBINDING_AUX_COMPILER_IS_IBMClang 0
# define GLBINDING_AUX_COMPILER_IS_XLClang 0
# define GLBINDING_AUX_COMPILER_IS_XL 0
# define GLBINDING_AUX_COMPILER_IS_VisualAge 0
# define GLBINDING_AUX_COMPILER_IS_NVHPC 0
# define GLBINDING_AUX_COMPILER_IS_PGI 0
# define GLBINDING_AUX_COMPILER_IS_Cray 0
# define GLBINDING_AUX_COMPILER_IS_TI 0
# define GLBINDING_AUX_COMPILER_IS_FujitsuClang 0
# define GLBINDING_AUX_COMPILER_IS_Fujitsu 0
# define GLBINDING_AUX_COMPILER_IS_GHS 0
# define GLBINDING_AUX_COMPILER_IS_SCO 0
# define GLBINDING_AUX_COMPILER_IS_ARMCC 0
# define GLBINDING_AUX_COMPILER_IS_AppleClang 0
# define GLBINDING_AUX_COMPILER_IS_ARMClang 0
# define GLBINDING_AUX_COMPILER_IS_Clang 0
# define GLBINDING_AUX_COMPILER_IS_LCC 0
# define GLBINDING_AUX_COMPILER_IS_GNU 0
# define GLBINDING_AUX_COMPILER_IS_MSVC 0
# define GLBINDING_AUX_COMPILER_IS_ADSP 0
# define GLBINDING_AUX_COMPILER_IS_IAR 0
# define GLBINDING_AUX_COMPILER_IS_MIPSpro 0

#if defined(__COMO__)
# undef GLBINDING_AUX_COMPILER_IS_Comeau
# define GLBINDING_AUX_COMPILER_IS_Comeau 1

#elif defined(__INTEL_COMPILER) || defined(__ICC)
# undef GLBINDING_AUX_COMPILER_IS_Intel
# define GLBINDING_AUX_COMPILER_IS_Intel 1

#elif (defined(__clang__) && defined(__INTEL_CLANG_COMPILER)) || defined(__INTEL_LLVM_COMPILER)
# undef GLBINDING_AUX_COMPILER_IS_IntelLLVM
# define GLBINDING_AUX_COMPILER_IS_IntelLLVM 1

#elif defined(__PATHCC__)
# undef GLBINDING_AUX_COMPILER_IS_PathScale
# define GLBINDING_AUX_COMPILER_IS_PathScale 1

#elif defined(__BORLANDC__) && defined(__CODEGEARC_VERSION__)
# undef GLBINDING_AUX_COMPILER_IS_Embarcadero
# define GLBINDING_AUX_COMPILER_IS_Embarcadero 1

#elif defined(__BORLANDC__)
# undef GLBINDING_AUX_COMPILER_IS_Borland
# define GLBINDING_AUX_COMPILER_IS_Borland 1

#elif defined(__WATCOMC__) && __WATCOMC__ < 1200
# undef GLBINDING_AUX_COMPILER_IS_Watcom
# define GLBINDING_AUX_COMPILER_IS_Watcom 1

#elif defined(__WATCOMC__)
# undef GLBINDING_AUX_COMPILER_IS_OpenWatcom
# define GLBINDING_AUX_COMPILER_IS_OpenWatcom 1

#elif defined(__SUNPRO_CC)
# undef GLBINDING_AUX_COMPILER_IS_SunPro
# define GLBINDING_AUX_COMPILER_IS_SunPro 1

#elif defined(__HP_aCC)
# undef GLBINDING_AUX_COMPILER_IS_HP
# define GLBINDING_AUX_COMPILER_IS_HP 1

#elif defined(__DECCXX)
# undef GLBINDING_AUX_COMPILER_IS_Compaq
# define GLBINDING_AUX_COMPILER_IS_Compaq 1

#elif defined(__IBMCPP__) && defined(__COMPILER_VER__)
# undef GLBINDING_AUX_COMPILER_IS_zOS
# define GLBINDING_AUX_COMPILER_IS_zOS 1

#elif defined(__open_xl__) && defined(__clang__)
# undef GLBINDING_AUX_COMPILER_IS_IBMClang
# define GLBINDING_AUX_COMPILER_IS_IBMClang 1

#elif defined(__ibmxl__) && defined(__clang__)
# undef GLBINDING_AUX_COMPILER_IS_XLClang
# define GLBINDING_AUX_COMPILER_IS_XLClang 1

#elif defined(__IBMCPP__) && !defined(__COMPILER_VER__) && __IBMCPP__ >= 800
# undef GLBINDING_AUX_COMPILER_IS_XL
# define GLBINDING_AUX_COMPILER_IS_XL 1

#elif defined(__IBMCPP__) && !defined(__COMPILER_VER__) && __IBMCPP__ < 800
# undef GLBINDING_AUX_COMPILER_IS_VisualAge
# define GLBINDING_AUX_COMPILER_IS_VisualAge 1

#elif defined(__NVCOMPILER)
# undef GLBINDING_AUX_COMPILER_IS_NVHPC
# define GLBINDING_AUX_COMPILER_IS_NVHPC 1

#elif defined(__PGI)
# undef GLBINDING_AUX_COMPILER_IS_PGI
# define GLBINDING_AUX_COMPILER_IS_PGI 1

#elif defined(_CRAYC)
# undef GLBINDING_AUX_COMPILER_IS_Cray
# define GLBINDING_AUX_COMPILER_IS_Cray 1

#elif defined(__TI_COMPILER_VERSION__)
# undef GLBINDING_AUX_COMPILER_IS_TI
# define GLBINDING_AUX_COMPILER_IS_TI 1

#elif defined(__CLANG_FUJITSU)
# undef GLBINDING_AUX_COMPILER_IS_FujitsuClang
# define GLBINDING_AUX_COMPILER_IS_FujitsuClang 1

#elif defined(__FUJITSU)
# undef GLBINDING_AUX_COMPILER_IS_Fujitsu
# define GLBINDING_AUX_COMPILER_IS_Fujitsu 1

#elif defined(__ghs__)
# undef GLBINDING_AUX_COMPILER_IS_GHS
# define GLBINDING_AUX_COMPILER_IS_GHS 1

#elif defined(__SCO_VERSION__)
# undef GLBINDING_AUX_COMPILER_IS_SCO
# define GLBINDING_AUX_COMPILER_IS_SCO 1

#elif defined(__ARMCC_VERSION) && !defined(__clang__)
# undef GLBINDING_AUX_COMPILER_IS_ARMCC
# define GLBINDING_AUX_COMPILER_IS_ARMCC 1

#elif defined(__clang__) && defined(__apple_build_version__)
# undef GLBINDING_AUX_COMPILER_IS_AppleClang
# define GLBINDING_AUX_COMPILER_IS_AppleClang 1

#elif defined(__clang__) && defined(__ARMCOMPILER_VERSION)
# undef GLBINDING_AUX_COMPILER_IS_ARMClang
# define GLBINDING_AUX_COMPILER_IS_ARMClang 1

#elif defined(__clang__)
# undef GLBINDING_AUX_COMPILER_IS_Clang
# define GLBINDING_AUX_COMPILER_IS_Clang 1

#elif defined(__LCC__) && (defined(__GNUC__) || defined(__GNUG__) || defined(__MCST__))
# undef GLBINDING_AUX_COMPILER_IS_LCC
# define GLBINDING_AUX_COMPILER_IS_LCC 1

#elif defined(__GNUC__) || defined(__GNUG__)
# undef GLBINDING_AUX_COMPILER_IS_GNU
# define GLBINDING_AUX_COMPILER_IS_GNU 1

#elif defined(_MSC_VER)
# undef GLBINDING_AUX_COMPILER_IS_MSVC
# define GLBINDING_AUX_COMPILER_IS_MSVC 1

#elif defined(_ADI_COMPILER)
# undef GLBINDING_AUX_COMPILER_IS_ADSP
# define GLBINDING_AUX_COMPILER_IS_ADSP 1

#elif defined(__IAR_SYSTEMS_ICC__) || defined(__IAR_SYSTEMS_ICC)
# undef GLBINDING_AUX_COMPILER_IS_IAR
# define GLBINDING_AUX_COMPILER_IS_IAR 1


#endif

#  if GLBINDING_AUX_COMPILER_IS_AppleClang

#    if !(((__clang_major__ * 100) + __clang_minor__) >= 400)
#      error Unsupported compiler version
#    endif

# define GLBINDING_AUX_COMPILER_VERSION_MAJOR (__clang_major__)
# define GLBINDING_AUX_COMPILER_VERSION_MINOR (__clang_minor__)
# define GLBINDING_AUX_COMPILER_VERSION_PATCH (__clang_patchlevel__)
# if defined(_MSC_VER)
   /* _MSC_VER = VVRR */
#  define GLBINDING_AUX_SIMULATE_VERSION_MAJOR (_MSC_VER / 100)
#  define GLBINDING_AUX_SIMULATE_VERSION_MINOR (_MSC_VER % 100)
# endif
# define GLBINDING_AUX_COMPILER_VERSION_TWEAK (__apple_build_version__)

#    if ((__clang_major__ * 100) + __clang_minor__) >= 400 && __has_feature(cxx_thread_local)
#      define GLBINDING_AUX_COMPILER_CXX_THREAD_LOCAL 1
#    else
#      define GLBINDING_AUX_COMPILER_CXX_THREAD_LOCAL 0
#    endif

#    if ((__clang_major__ * 100) + __clang_minor__) >= 400 && __has_feature(cxx_constexpr)
#      define GLBINDING_AUX_COMPILER_CXX_CONSTEXPR 1
#    else
#      define GLBINDING_AUX_COMPILER_CXX_CONSTEXPR 0
#    endif

#    if ((__clang_major__ * 100) + __clang_minor__) >= 501 && __cplusplus > 201103L
#      define GLBINDING_AUX_COMPILER_CXX_ATTRIBUTE_DEPRECATED 1
#    else
#      define GLBINDING_AUX_COMPILER_CXX_ATTRIBUTE_DEPRECATED 0
#    endif

#    if ((__clang_major__ * 100) + __clang_minor__) >= 400 && __has_feature(cxx_noexcept)
#      define GLBINDING_AUX_COMPILER_CXX_NOEXCEPT 1
#    else
#      define GLBINDING_AUX_COMPILER_CXX_NOEXCEPT 0
#    endif

#  elif GLBINDING_AUX_COMPILER_IS_Clang

#    if !(((__clang_major__ * 100) + __clang_minor__) >= 301)
#      error Unsupported compiler version
#    endif

# define GLBINDING_AUX_COMPILER_VERSION_MAJOR (__clang_major__)
# define GLBINDING_AUX_COMPILER_VERSION_MINOR (__clang_minor__)
# define GLBINDING_AUX_COMPILER_VERSION_PATCH (__clang_patchlevel__)
# if defined(_MSC_VER)
   /* _MSC_VER = VVRR */
#  define GLBINDING_AUX_SIMULATE_VERSION_MAJOR (_MSC_VER / 100)
#  define GLBINDING_AUX_SIMULATE_VERSION_MINOR (_MSC_VER % 100)
# endif

#    if ((__clang_major__ * 100) + __clang_minor__) >= 301 && __has_feature(cxx_thread_local)
#      define GLBINDING_AUX_COMPILER_CXX_THREAD_LOCAL 1
#    else
#      define GLBINDING_AUX_COMPILER_CXX_THREAD_LOCAL 0
#    endif

#    if ((__clang_major__ * 100) + __clang_minor__) >= 301 && __has_feature(cxx_constexpr)
#      define GLBINDING_AUX_COMPILER_CXX_CONSTEXPR 1
#    else
#      define GLBINDING_AUX_COMPILER_CXX_CONSTEXPR 0
#    endif

#    if ((__clang_major__ * 100) + __clang_minor__) >= 304 && __cplusplus > 201103L
#      define GLBINDING_AUX_COMPILER_CXX_ATTRIBUTE_DEPRECATED 1
#    else
#      define GLBINDING_AUX_COMPILER_CXX_ATTRIBUTE_DEPRECATED 0
#    endif

#    if ((__clang_major__ * 100) + __clang_minor__) >= 301 && __has_feature(cxx_noexcept)
#      define GLBINDING_AUX_COMPILER_CXX_NOEXCEPT 1
#    else
#      define GLBINDING_AUX_COMPILER_CXX_NOEXCEPT 0
#    endif

#  elif GLBINDING_AUX_COMPILER_IS_GNU

#    if !((__GNUC__ * 100 + __GNUC_MINOR__) >= 404)
#      error Unsupported compiler version
#    endif

# if defined(__GNUC__)
#  define GLBINDING_AUX_COMPILER_VERSION_MAJOR (__GNUC__)
# else
#  define GLBINDING_AUX_COMPILER_VERSION_MAJOR (__GNUG__)
# endif
# if defined(__GNUC_MINOR__)
#  define GLBINDING_AUX_COMPILER_VERSION_MINOR (__GNUC_MINOR__)
# endif
# if defined(__GNUC_PATCHLEVEL__)
#  define GLBINDING_AUX_COMPILER_VERSION_PATCH (__GNUC_PATCHLEVEL__)
# endif

#    if (__GNUC__ * 100 + __GNUC_MINOR__) >= 408 && __cplusplus >= 201103L
#      define GLBINDING_AUX_COMPILER_CXX_THREAD_LOCAL 1
#    else
#      define GLBINDING_AUX_COMPILER_CXX_THREAD_LOCAL 0
#    endif

#    if (__GNUC__ * 100 + __GNUC_MINOR__) >= 406 && (__cplusplus >= 201103L || (defined(__GXX_EXPERIMENTAL_CXX0X__) && __GXX_EXPERIMENTAL_CXX0X__))
#      define GLBINDING_AUX_COMPILER_CXX_CONSTEXPR 1
#    else
#      define GLBINDING_AUX_COMPILER_CXX_CONSTEXPR 0
#    endif

#    if (__GNUC__ * 100 + __GNUC_MINOR__) >= 409 && __cplusplus > 201103L
#      define GLBINDING_AUX_COMPILER_CXX_ATTRIBUTE_DEPRECATED 1
#    else
#      define GLBINDING_AUX_COMPILER_CXX_ATTRIBUTE_DEPRECATED 0
#    endif

#    if (__GNUC__ * 100 + __GNUC_MINOR__) >= 406 && (__cplusplus >= 201103L || (defined(__GXX_EXPERIMENTAL_CXX0X__) && __GXX_EXPERIMENTAL_CXX0X__))
#      define GLBINDING_AUX_COMPILER_CXX_NOEXCEPT 1
#    else
#      define GLBINDING_AUX_COMPILER_CXX_NOEXCEPT 0
#    endif

#  elif GLBINDING_AUX_COMPILER_IS_MSVC

#    if !(_MSC_VER >= 1600)
#      error Unsupported compiler version
#    endif

  /* _MSC_VER = VVRR */
# define GLBINDING_AUX_COMPILER_VERSION_MAJOR (_MSC_VER / 100)
# define GLBINDING_AUX_COMPILER_VERSION_MINOR (_MSC_VER % 100)
# if defined(_MSC_FULL_VER)
#  if _MSC_VER >= 1400
    /* _MSC_FULL_VER = VVRRPPPPP */
#   define GLBINDING_AUX_COMPILER_VERSION_PATCH (_MSC_FULL_VER % 100000)
#  else
    /* _MSC_FULL_VER = VVRRPPPP */
#   define GLBINDING_AUX_COMPILER_VERSION_PATCH (_MSC_FULL_VER % 10000)
#  endif
# endif
# if defined(_MSC_BUILD)
#  define GLBINDING_AUX_COMPILER_VERSION_TWEAK (_MSC_BUILD)
# endif

#    if _MSC_VER >= 1900
#      define GLBINDING_AUX_COMPILER_CXX_THREAD_LOCAL 1
#    else
#      define GLBINDING_AUX_COMPILER_CXX_THREAD_LOCAL 0
#    endif

#    if _MSC_VER >= 1900
#      define GLBINDING_AUX_COMPILER_CXX_CONSTEXPR 1
#    else
#      define GLBINDING_AUX_COMPILER_CXX_CONSTEXPR 0
#    endif

#    if _MSC_VER >= 1900
#      define GLBINDING_AUX_COMPILER_CXX_ATTRIBUTE_DEPRECATED 1
#    else
#      define GLBINDING_AUX_COMPILER_CXX_ATTRIBUTE_DEPRECATED 0
#    endif

#    if _MSC_VER >= 1900
#      define GLBINDING_AUX_COMPILER_CXX_NOEXCEPT 1
#    else
#      define GLBINDING_AUX_COMPILER_CXX_NOEXCEPT 0
#    endif

#  else
#    error Unsupported compiler
#  endif

#  if defined(GLBINDING_AUX_COMPILER_CXX_THREAD_LOCAL) && GLBINDING_AUX_COMPILER_CXX_THREAD_LOCAL
#    define GLBINDING_AUX_THREAD_LOCAL thread_local
#  elif GLBINDING_AUX_COMPILER_IS_GNU || GLBINDING_AUX_COMPILER_IS_Clang || GLBINDING_AUX_COMPILER_IS_AppleClang
#    define GLBINDING_AUX_THREAD_LOCAL __thread
#  elif GLBINDING_AUX_COMPILER_IS_MSVC
#    define GLBINDING_AUX_THREAD_LOCAL __declspec(thread)
#  else
// GLBINDING_AUX_THREAD_LOCAL not defined for this configuration.
#  endif


#  if defined(GLBINDING_AUX_COMPILER_CXX_CONSTEXPR) && GLBINDING_AUX_COMPILER_CXX_CONSTEXPR
#    define GLBINDING_AUX_CONSTEXPR constexpr
#  else
#    define GLBINDING_AUX_CONSTEXPR 
#  endif


#  ifndef GLBINDING_AUX_DEPRECATED
#    if defined(GLBINDING_AUX_COMPILER_CXX_ATTRIBUTE_DEPRECATED) && GLBINDING_AUX_COMPILER_CXX_ATTRIBUTE_DEPRECATED
#      define GLBINDING_AUX_DEPRECATED [[deprecated]]
#      define GLBINDING_AUX_DEPRECATED_MSG(MSG) [[deprecated(MSG)]]
#    elif GLBINDING_AUX_COMPILER_IS_GNU || GLBINDING_AUX_COMPILER_IS_Clang
#      define GLBINDING_AUX_DEPRECATED __attribute__((__deprecated__))
#      define GLBINDING_AUX_DEPRECATED_MSG(MSG) __attribute__((__deprecated__(MSG)))
#    elif GLBINDING_AUX_COMPILER_IS_MSVC
#      define GLBINDING_AUX_DEPRECATED __declspec(deprecated)
#      define GLBINDING_AUX_DEPRECATED_MSG(MSG) __declspec(deprecated(MSG))
#    else
#      define GLBINDING_AUX_DEPRECATED
#      define GLBINDING_AUX_DEPRECATED_MSG(MSG)
#    endif
#  endif


#  if defined(GLBINDING_AUX_COMPILER_CXX_NOEXCEPT) && GLBINDING_AUX_COMPILER_CXX_NOEXCEPT
#    define GLBINDING_AUX_NOEXCEPT noexcept
#    define GLBINDING_AUX_NOEXCEPT_EXPR(X) noexcept(X)
#  else
#    define GLBINDING_AUX_NOEXCEPT
#    define GLBINDING_AUX_NOEXCEPT_EXPR(X)
#  endif

#endif

#endif
