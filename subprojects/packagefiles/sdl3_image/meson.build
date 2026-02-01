# Rough PR Comments:
# - Mostly 1:1 recreation of the logic used in the SDL_image/CMakeLists.txt (exceptions listed below)
# - Meson best practices always preferred over the CMake logic
# - CPack excluded because yknow, it aint CMake
# - Vendored dependencies excluded as they're not directly included in the source
# -
#

# list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_LIST_DIR}/cmake")

project('sdl3_image', 'c',
  meson_version: '>= 1.1.0',
  version: '3.4.0',
  default_options: 'c_std=c99')

major_version = meson.project_version().split('.')[0]
minor_version = meson.project_version().split('.')[1]
micro_version = meson.project_version().split('.')[2]

feature_args = []

sdl3_dep = dependency('sdl3', version: '>=3.4.0') # Minimum allowed SDL3 version, not SDL3_IMAGE version
libpng_dep = dependency('libpng', required: get_option('SDLIMAGE_PNG_LIBPNG'))
libavif_dep = dependency('libavif', version: '>=0.1.0', required: get_option('SDLIMAGE_AVIF')) # Absent from wrapdb as of Feb 1 2026
libjxl_dep = dependency('libjxl', required: get_option('SDLIMAGE_JXL')) # Absent from wrapdb as of Feb 1 2026
libtiff_dep = dependency('libtiff', required: get_option('SDLIMAGE_TIF'))
libwebp_dep = dependency('libwebp', required: get_option('SDLIMAGE_WEBP'))

deps = [sdl3_dep, libpng_dep, libavif_dep, libjxl_dep]

# include("${CMAKE_CURRENT_LIST_DIR}/cmake/GetGitRevisionDescription.cmake")
# include("${CMAKE_CURRENT_LIST_DIR}/cmake/PrivateSdlFunctions.cmake")
# include("${CMAKE_CURRENT_LIST_DIR}/cmake/sdlcpu.cmake")
# include("${CMAKE_CURRENT_LIST_DIR}/cmake/sdlplatform.cmake")
# include("${CMAKE_CURRENT_LIST_DIR}/cmake/sdlmanpages.cmake")
# sdl_calculate_derived_version_variables(${MAJOR_VERSION} ${MINOR_VERSION} ${MICRO_VERSION})

sdlimage_rootproject = not meson.is_subproject()

# if(NOT DEFINED CMAKE_FIND_PACKAGE_PREFER_CONFIG)
#     set(CMAKE_FIND_PACKAGE_PREFER_CONFIG ON)
# endif()

# include(CMakeDependentOption)
# include(CMakePackageConfigHelpers)
# include(GNUInstallDirs)

platform_supports_shared = target_machine.system() == 'emscripten' ? false : true

get_option('POSITION_INDEPENDENT_CODE').require(platform_supports_shared, error_message: 'Target "' + target_machine.system() + '" does not support shared libraries')

# SDL3_image-3.4.0, CMakeLists.txt, line 65
get_option('SDLIMAGE_INSTALL').require(not subproject('sdl3').found(), error_message: 'Cannot install SDL3_image when SDL3 is built in same build')
get_option('SDLIMAGE_INSTALL').require(sdlimage_rootproject, error_message: 'Cannot install SDL3_image when it is a subproject')

# cmake_dependent_option(SDLIMAGE_INSTALL_MAN "Install man pages for SDL3_image" OFF "SDLIMAGE_INSTALL" OFF)
# cmake_dependent_option(SDLIMAGE_DEPS_SHARED "Load dependencies dynamically" ON PLATFORM_SUPPORTS_SHARED OFF)
# cmake_dependent_option(SDLIMAGE_RELOCATABLE "Create relocatable SDL_image package" "${MSVC}" SDLIMAGE_INSTALL OFF)
# option(SDLIMAGE_WERROR "Treat warnings as errors" OFF)

get_option('SDLIMAGE_SAMPLES').enable_auto_if(sdlimage_rootproject)
get_option('SDLIMAGE_SAMPLES').disable_auto_if(target_machine.system() == 'android')
get_option('SDLIMAGE_SAMPLES_INSTALL').enable_auto_if(get_option('SDLIMAGE_SAMPLES').enabled() and get_option('SDLIMAGE_INSTALL').enabled())

get_option('SDLIMAGE_BACKEND_WIC').require(target_machine.system() == 'windows', error_message : 'Windows required')
get_option('SDLIMAGE_BACKEND_IMAGEIO').require(target_machine.system() == 'darwin', error_message: 'Darwin required')
get_option('SDLIMAGE_PNG_LIBPNG').enable_auto_if(libpng_dep.found())

get_option('SDLIMAGE_ANI_SAVE').enable_auto_if(get_option('SDLIMAGE_ANI').enabled())
get_option('SDLIMAGE_AVIF_SAVE').enable_auto_if(get_option('SDLIMAGE_AVIF').enabled())
get_option('SDLIMAGE_BMP_SAVE').enable_auto_if(get_option('SDLIMAGE_BMP').enabled())
get_option('SDLIMAGE_GIF_SAVE').enable_auto_if(get_option('SDLIMAGE_GIF').enabled())
get_option('SDLIMAGE_JPG_SAVE').enable_auto_if(get_option('SDLIMAGE_JPG').enabled())
get_option('SDLIMAGE_PNG_SAVE').enable_auto_if(get_option('SDLIMAGE_PNG').enabled())
get_option('SDLIMAGE_TGA_SAVE').enable_auto_if(get_option('SDLIMAGE_TGA').enabled())
get_option('SDLIMAGE_WEBP_SAVE').enable_auto_if(get_option('SDLIMAGE_WEBP').enabled())
get_option('SDLIMAGE_PNG_LIBPNG').enable_auto_if(get_option('SDLIMAGE_PNG').enabled())

subdir('src')

add_project_arguments('-DSDL_BUILD_MAJOR_VERSION=' + major_version, language: 'c')
add_project_arguments('-DSDL_BUILD_MAJOR_VERSION=' + minor_version, language: 'c')
add_project_arguments('-DSDL_BUILD_MAJOR_VERSION=' + micro_version, language: 'c')

if get_option('SDLIMAGE_BACKEND_STB').enabled()
  add_project_arguments('-DUSE_STBIMAGE', language: 'c')
endif

if target_machine.system() == 'darwin'
  add_language('objc', required: get_option('SDLIMAGE_BACKEND_IMAGEIO'))
  if get_option('SDLIMAGE_PNG').enabled() and not get_option('SDLIMAGE_BACKEND_STB').enabled()
    add_project_arguments('-DPNG_USES_IMAGEIO', language: 'objc')
  endif
  if get_option('SDLIMAGE_JPG').enabled() and not get_option('SDLIMAGE_BACKEND_STB').enabled()
    add_project_arguments('-DJPG_USES_IMAGEIO', language: 'objc')
  endif
else
  add_project_arguments('-DSDL_IMAGE_USE_COMMON_BACKEND', language: 'objc')
endif

if get_option('SDLIMAGE_BACKEND_WIC').enabled()
  add_project_arguments('-DSDL_IMAGE_USE_WIC_BACKEND', language: 'c')
endif




if get_option('SDLIMAGE_AVIF').enabled()
  add_project_arguments('-DLOAD_AVIF', language: 'c')
  add_project_arguments('-DSAVE_AVIF=' + get_option('SDLIMAGE_AVIF_SAVE').enabled(), language: 'c')
endif

# list(APPEND SDLIMAGE_BACKENDS ANI)
# set(SDLIMAGE_ANI_ENABLED FALSE)
# if(SDLIMAGE_ANI)
#     set(SDLIMAGE_ANI_ENABLED TRUE)
#     if(SDLIMAGE_ANI_ENABLED)
#         target_compile_definitions(${sdl3_image_target_name} PRIVATE
#             LOAD_ANI
#             SAVE_ANI=$<BOOL:${SDLIMAGE_ANI_SAVE}>
#         )
#     else()
#         # Variable is used by test suite
#         set(SDLIMAGE_ANI_SAVE OFF)
#     endif()
# endif()

# list(APPEND SDLIMAGE_BACKENDS BMP)
# set(SDLIMAGE_BMP_ENABLED FALSE)
# if(SDLIMAGE_BMP)
#     set(SDLIMAGE_BMP_ENABLED TRUE)
#     if(SDLIMAGE_BMP_ENABLED)
#         target_compile_definitions(${sdl3_image_target_name} PRIVATE
#             LOAD_BMP
#             SAVE_BMP=$<BOOL:${SDLIMAGE_BMP_SAVE}>
#         )
#     else()
#         # Variable is used by test suite
#         set(SDLIMAGE_BMP_SAVE OFF)
#     endif()
# endif()

# list(APPEND SDLIMAGE_BACKENDS GIF)
# set(SDLIMAGE_GIF_ENABLED FALSE)
# if(SDLIMAGE_GIF)
#     set(SDLIMAGE_GIF_ENABLED TRUE)
#     if(SDLIMAGE_GIF_ENABLED)
#         target_compile_definitions(${sdl3_image_target_name} PRIVATE
#             LOAD_GIF
#             SAVE_GIF=$<BOOL:${SDLIMAGE_GIF_SAVE}>
#         )
#     else()
#         # Variable is used by test suite
#         set(SDLIMAGE_GIF_SAVE OFF)
#     endif()
# endif()

# list(APPEND SDLIMAGE_BACKENDS JPG)
# set(SDLIMAGE_JPG_ENABLED FALSE)
# if(SDLIMAGE_JPG)
#     if(SDLIMAGE_BACKEND_STB OR SDLIMAGE_BACKEND_WIC OR SDLIMAGE_BACKEND_IMAGEIO)
#         set(SDLIMAGE_JPG_ENABLED TRUE)
#     else()
#         if(SDLIMAGE_JPG_VENDORED)
#             set(SDLIMAGE_JPG_ENABLED TRUE)
#             message(STATUS "${PROJECT_NAME}: Using vendored libjpeg")
#             sdl_check_project_in_subfolder(external/jpeg libjpeg SDLIMAGE_VENDORED)
#             set(BUILD_SHARED_LIBS ${SDLIMAGE_JPG_SHARED})
#             add_subdirectory(external/jpeg external/jpeg-build EXCLUDE_FROM_ALL)
#             register_license(jpeg external/jpeg/COPYING)
#             if(SDLIMAGE_JPG_SHARED OR NOT SDLIMAGE_BUILD_SHARED_LIBS)
#                 list(APPEND INSTALL_EXTRA_TARGETS jpeg)
#             endif()
#             set_target_properties(jpeg PROPERTIES EXPORT_NAME external_libjpeg)
#             add_library(SDL3_image::external_libjpeg ALIAS jpeg)
#             if(NOT SDLIMAGE_JPG_SHARED)
#                 list(APPEND PC_LIBS -l$<TARGET_FILE_BASE_NAME:jpeg>)
#             endif()
#         elseif(SDLIMAGE_JPG_SHARED AND DEFINED SDLIMAGE_DYNAMIC_JPEG AND EXISTS "${SDLIMAGE_DYNAMIC_JPEG}")
#             message(STATUS "${PROJECT_NAME}: Using libjpeg from CMake variable")
#             set(SDLIMAGE_JPG_ENABLED TRUE)
#         else()
#             find_package(JPEG ${required})
#             if(JPEG_FOUND)
#                 message(STATUS "${PROJECT_NAME}: Using system libjpeg")
#                 set(SDLIMAGE_JPG_ENABLED TRUE)
#                 if(NOT SDLIMAGE_JPG_SHARED)
#                     list(APPEND PC_REQUIRES libjpeg)
#                 endif()
#             else()
#                 message(${fatal_error} "libjpeg NOT found")
#             endif()
#         endif()
#         if(SDLIMAGE_JPG_ENABLED)
#             if(SDLIMAGE_JPG_SHARED)
#                 if(NOT DEFINED SDLIMAGE_DYNAMIC_JPEG)
#                     target_include_directories(${sdl3_image_target_name} PRIVATE
#                         $<TARGET_PROPERTY:JPEG::JPEG,INCLUDE_DIRECTORIES>
#                         $<TARGET_PROPERTY:JPEG::JPEG,INTERFACE_INCLUDE_DIRECTORIES>
#                         $<TARGET_PROPERTY:JPEG::JPEG,INTERFACE_SYSTEM_INCLUDE_DIRECTORIES>
#                     )
#                     if(SDLIMAGE_JPG_VENDORED)
#                       add_dependencies(${sdl3_image_target_name} JPEG::JPEG)
#                     endif()
#                 endif()
#                 target_get_dynamic_library(SDLIMAGE_DYNAMIC_JPEG JPEG::JPEG)
#                 message(STATUS "Dynamic libjpeg: ${SDLIMAGE_DYNAMIC_JPEG}")
#                 target_compile_definitions(${sdl3_image_target_name} PRIVATE "LOAD_JPG_DYNAMIC=\"${SDLIMAGE_DYNAMIC_JPEG}\"")
#             else()
#                 target_link_libraries(${sdl3_image_target_name} PRIVATE JPEG::JPEG)
#             endif()
#       endif()
#     endif()
#     if(SDLIMAGE_JPG_ENABLED)
#         target_compile_definitions(${sdl3_image_target_name} PRIVATE
#             LOAD_JPG
#             SAVE_JPG=$<BOOL:${SDLIMAGE_JPG_SAVE}>
#         )
#     else()
#         # Variable is used by test suite
#         set(SDLIMAGE_JPG_SAVE OFF)
#     endif()
# endif()

# list(APPEND SDLIMAGE_BACKENDS JXL)
# set(SDLIMAGE_JXL_ENABLED FALSE)
# if(SDLIMAGE_JXL)
#     if(SDLIMAGE_JXL_VENDORED)
#         set(SDLIMAGE_JXL_ENABLED TRUE)
#         enable_language(CXX)
#         message(STATUS "${PROJECT_NAME}: Using vendored libjxl")
#         # BUILD_TESTING variable is used by libjxl
#         set(BUILD_TESTING OFF CACHE BOOL "build testing")
#         # JPEGXL_ENABLE_BENCHMARK variable is used by libjxl
#         set(JPEGXL_ENABLE_BENCHMARK OFF CACHE BOOL "libjpegxl benchmark" FORCE)
#         # JPEGXL_ENABLE_TOOLS variable is used by libjxl
#         set(JPEGXL_ENABLE_JNI OFF CACHE BOOL "build jpegxl jni" FORCE)
#         # JPEGXL_ENABLE_SJPEG variable is used by libjxl
#         set(JPEGXL_ENABLE_SJPEG OFF CACHE BOOL "build jpegxl sjpeg" FORCE)
#         # JPEGXL_BUNDLE_SKCMS variable is used by libjxl
#         set(JPEGXL_BUNDLE_SKCMS OFF CACHE BOOL "build jpegxl bundle sjpeg" FORCE)
#         # JPEGXL_ENABLE_OPENEXR variable is used by libjxl
#         set(JPEGXL_ENABLE_OPENEXR OFF CACHE BOOL "build jpegxl openxr" FORCE)
#         # JPEGXL_ENABLE_MANPAGES variable is used by libjxl
#         set(JPEGXL_ENABLE_MANPAGES OFF CACHE BOOL "libjxl manpage option" FORCE)
#         # JPEGXL_ENABLE_PLUGINS variable is used by libjxl
#         set(JPEGXL_ENABLE_PLUGINS OFF CACHE BOOL "libjxl manpage option" FORCE)
#         # JPEGXL_ENABLE_SKCMS variable is used by libjxl
#         set(JPEGXL_ENABLE_SKCMS OFF CACHE BOOL "libjxl skcms option" FORCE)
#         # JPEGXL_FORCE_SYSTEM_HWY variable is used by libjxl
#         set(JPEGXL_FORCE_SYSTEM_HWY OFF CACHE BOOL "libjxl highway option" FORCE)
#         sdl_check_project_in_subfolder(external/libjxl libjxl SDLIMAGE_VENDORED)
#         set(BUILD_SHARED_LIBS ${SDLIMAGE_JXL_SHARED})
#         add_subdirectory(external/libjxl external/libjxl-build EXCLUDE_FROM_ALL)
#         register_license(jxl external/libjxl/LICENSE)
#         if(SDLIMAGE_JXL_SHARED)
#             set(jxl_lib jxl)
#             set(jxl_install_libs brotlidec brotlicommon brotlienc jxl)
#         else()
#             set(jxl_lib jxl_dec-static)
#             set(jxl_install_libs brotlidec brotlicommon hwy jxl_dec-static)
#             list(APPEND PC_LIBS
#                 -l$<TARGET_FILE_BASE_NAME:brotlidec> -l$<TARGET_FILE_BASE_NAME:brotlicommon>
#                 -l$<TARGET_FILE_BASE_NAME:brotlienc> -l$<TARGET_FILE_BASE_NAME:jxl>
#             )
#         endif()
#         if(SDLIMAGE_JXL_SHARED OR NOT SDLIMAGE_BUILD_SHARED_LIBS)
#             list(APPEND INSTALL_EXTRA_TARGETS ${jxl_install_libs})
#         endif()
#         set_target_properties(${jxl_lib} PROPERTIES EXPORT_NAME external_libjxl)
#         add_library(SDL3_image::external_libjxl ALIAS ${jxl_lib})
#         if(NOT TARGET libjxl::libjxl)
#             add_library(libjxl::libjxl ALIAS ${jxl_lib})
#         endif()
#     elseif(SDLIMAGE_JXL_SHARED AND DEFINED SDLIMAGE_DYNAMIC_JXL AND EXISTS "${SDLIMAGE_DYNAMIC_JXL}")
#         message(STATUS "${PROJECT_NAME}: Using libjxl from CMake variable")
#         set(SDLIMAGE_JXL_ENABLED TRUE)
#     else()
#         find_package(libjxl ${required})
#         if(libjxl_FOUND)
#             message(STATUS "${PROJECT_NAME}: Using system libjxl")
#             set(SDLIMAGE_JXL_ENABLED TRUE)
#             if(NOT SDLIMAGE_JXL_SHARED)
#                 list(APPEND PC_REQUIRES libjxl)
#                 list(APPEND INSTALL_EXTRA_CMAKE_MODULES cmake/Findlibjxl.cmake)
#             endif()
#         else()
#             message(${fatal_error} "libjxl NOT found")
#         endif()
#     endif()
#     if(SDLIMAGE_JXL_ENABLED)
#         target_compile_definitions(${sdl3_image_target_name} PRIVATE LOAD_JXL)
#         if(SDLIMAGE_JXL_SHARED)
#            if(NOT DEFINED SDLIMAGE_DYNAMIC_JXL)
#                 target_include_directories(${sdl3_image_target_name} PRIVATE
#                     $<TARGET_PROPERTY:libjxl::libjxl,INCLUDE_DIRECTORIES>
#                     $<TARGET_PROPERTY:libjxl::libjxl,INTERFACE_INCLUDE_DIRECTORIES>
#                     $<TARGET_PROPERTY:libjxl::libjxl,INTERFACE_SYSTEM_INCLUDE_DIRECTORIES>
#                 )
#                 if(SDLIMAGE_JXL_VENDORED)
#                     add_dependencies(${sdl3_image_target_name} libjxl::libjxl)
#                 endif()
#             endif()
#             target_get_dynamic_library(SDLIMAGE_DYNAMIC_JXL libjxl::libjxl)
#             message(STATUS "Dynamic libjxl: ${SDLIMAGE_DYNAMIC_JXL}")
#             target_compile_definitions(${sdl3_image_target_name} PRIVATE "LOAD_JXL_DYNAMIC=\"${SDLIMAGE_DYNAMIC_JXL}\"")
#         else()
#             target_link_libraries(${sdl3_image_target_name} PRIVATE libjxl::libjxl)
#         endif()
#     endif()
# endif()

# list(APPEND SDLIMAGE_BACKENDS LBM)
# set(SDLIMAGE_LBM_ENABLED FALSE)
# if(SDLIMAGE_LBM)
#     set(SDLIMAGE_LBM_ENABLED TRUE)
#     target_compile_definitions(${sdl3_image_target_name} PRIVATE LOAD_LBM)
# endif()

# list(APPEND SDLIMAGE_BACKENDS PCX)
# set(SDLIMAGE_PCX_ENABLED FALSE)
# if(SDLIMAGE_PCX)
#     set(SDLIMAGE_PCX_ENABLED TRUE)
#     target_compile_definitions(${sdl3_image_target_name} PRIVATE LOAD_PCX)
# endif()

# list(APPEND SDLIMAGE_BACKENDS PNG)
# list(APPEND SDLIMAGE_BACKENDS APNG)
# set(SDLIMAGE_PNG_ENABLED FALSE)
# if(SDLIMAGE_PNG)
#     set(SDLIMAGE_APNG_ENABLED FALSE)
#     set(SDLIMAGE_PNG_ENABLED TRUE)
#     set(SDLIMAGE_LIBPNG_ENABLED FALSE)

#     if(SDLIMAGE_PNG_LIBPNG)
#         if(SDLIMAGE_PNG_VENDORED)
#             set(PNG_SHARED "${SDLIMAGE_PNG_SHARED}")
#             set(SDLIMAGE_LIBPNG_ENABLED TRUE)
#             message(STATUS "${PROJECT_NAME}: Using vendored libpng")
#             set(PNG_TESTS OFF CACHE BOOL "Build PNG Tests" FORCE)
#             set(SKIP_INSTALL_EXPORT TRUE)
#             sdl_check_project_in_subfolder(external/libpng libpng SDLIMAGE_VENDORED)
#             add_subdirectory(external/libpng external/libpng-build EXCLUDE_FROM_ALL)
#             register_license(libpng external/libpng/LICENSE)
#             if(SDLIMAGE_PNG_SHARED)
#                 set(PNG_LIBRARY png_shared)
#             else()
#                 set(PNG_LIBRARY png_static)
#             endif()
#             add_library(PNG::PNG ALIAS ${PNG_LIBRARY})
#             set_property(TARGET ${PNG_LIBRARY} PROPERTY DEBUG_POSTFIX "")
#             target_include_directories(${sdl3_image_target_name} PRIVATE external/libpng)
#             if(SDLIMAGE_PNG_SHARED OR NOT SDLIMAGE_BUILD_SHARED_LIBS)
#                 list(APPEND INSTALL_EXTRA_TARGETS ${PNG_LIBRARY})
#             endif()
#             set_target_properties(${PNG_LIBRARY} PROPERTIES EXPORT_NAME external_libpng)
#             add_library(SDL3_image::external_libpng ALIAS ${PNG_LIBRARY})
#             if(NOT SDLIMAGE_PNG_SHARED)
#                 list(APPEND PC_LIBS -l$<TARGET_FILE_BASE_NAME:${PNG_LIBRARY}>)
#                 endif()
#             endif()
#         elseif(SDLIMAGE_PNG_SHARED AND DEFINED SDLIMAGE_DYNAMIC_PNG AND EXISTS "${SDLIMAGE_DYNAMIC_PNG}")
#             message(STATUS "${PROJECT_NAME}: Using libpng from CMake variable")
#             set(SDLIMAGE_LIBPNG_ENABLED TRUE)
#         else()
#             find_package(PNG ${required})
#             if(PNG_FOUND)
#                 message(STATUS "${PROJECT_NAME}: Using system libpng")
#                 set(SDLIMAGE_LIBPNG_ENABLED TRUE)
#                 if(NOT SDLIMAGE_PNG_SHARED)
#                     list(APPEND PC_REQUIRES libpng)
#                 endif()
#             else()
#                 message(${FATAL_ERROR} "libpng NOT found")
#             endif()
#         endif()
#     endif()

#     if(SDLIMAGE_LIBPNG_ENABLED)
#         set(SDLIMAGE_APNG_ENABLED TRUE)
#         target_compile_definitions(${sdl3_image_target_name} PRIVATE
#             SDL_IMAGE_LIBPNG
#         )
#         if(SDLIMAGE_PNG_SHARED)
#             if(NOT DEFINED SDLIMAGE_DYNAMIC_PNG)
#                 if(TARGET PNG::png_shared)
#                     set(png_target PNG::png_shared)
#                 else()
#                     set(png_target PNG::PNG)
#                 endif()
#                 target_include_directories(${sdl3_image_target_name} PRIVATE
#                     $<TARGET_PROPERTY:${png_target},INCLUDE_DIRECTORIES>
#                     $<TARGET_PROPERTY:${png_target},INTERFACE_INCLUDE_DIRECTORIES>
#                     $<TARGET_PROPERTY:${png_target},INTERFACE_SYSTEM_INCLUDE_DIRECTORIES>
#                 )
#                 if(SDLIMAGE_PNG_VENDORED)
#                     add_dependencies(${sdl3_image_target_name} ${png_target})
#                 endif()
#             endif()
#             target_get_dynamic_library(SDLIMAGE_DYNAMIC_PNG PNG::PNG)
#             message(STATUS "Dynamic libpng: ${SDLIMAGE_DYNAMIC_PNG}")
#             target_compile_definitions(${sdl3_image_target_name} PRIVATE "LOAD_LIBPNG_DYNAMIC=\"${SDLIMAGE_DYNAMIC_PNG}\"")
#         else()
#             target_link_libraries(${sdl3_image_target_name} PRIVATE PNG::PNG)
#         endif()
#     endif()

#     target_compile_definitions(${sdl3_image_target_name} PRIVATE
#         LOAD_PNG
#         SAVE_PNG=$<BOOL:${SDLIMAGE_PNG_SAVE}>
#     )
# endif()

# list(APPEND SDLIMAGE_BACKENDS PNM)
# set(SDLIMAGE_PNM_ENABLED FALSE)
# if(SDLIMAGE_PNM)
#     set(SDLIMAGE_PNM_ENABLED TRUE)
#     target_compile_definitions(${sdl3_image_target_name} PRIVATE LOAD_PNM)
# endif()

# list(APPEND SDLIMAGE_BACKENDS QOI)
# set(SDLIMAGE_QOI_ENABLED FALSE)
# if(SDLIMAGE_QOI)
#     set(SDLIMAGE_QOI_ENABLED TRUE)
#     target_compile_definitions(${sdl3_image_target_name} PRIVATE LOAD_QOI)
# endif()

# list(APPEND SDLIMAGE_BACKENDS SVG)
# set(SDLIMAGE_SVG_ENABLED FALSE)
# if(SDLIMAGE_SVG)
#     set(SDLIMAGE_SVG_ENABLED TRUE)
#     target_compile_definitions(${sdl3_image_target_name} PRIVATE LOAD_SVG)
# endif()

# list(APPEND SDLIMAGE_BACKENDS TGA)
# set(SDLIMAGE_TGA_ENABLED FALSE)
# if(SDLIMAGE_TGA)
#     set(SDLIMAGE_TGA_ENABLED TRUE)
#     if(SDLIMAGE_TGA_ENABLED)
#       target_compile_definitions(${sdl3_image_target_name} PRIVATE
#           LOAD_TGA
#           SAVE_TGA=$<BOOL:${SDLIMAGE_TGA_SAVE}>
#       )
#     else()
#       # Variable is used by test suite
#       set(SDLIMAGE_TGA_SAVE OFF)
#     endif()
# endif()

# list(APPEND SDLIMAGE_BACKENDS TIF)
# set(SDLIMAGE_TIF_ENABLED FALSE)
# if(SDLIMAGE_TIF)
#     if(SDLIMAGE_BACKEND_IMAGEIO OR SDLIMAGE_BACKEND_WIC)
#         set(SDLIMAGE_TIF_ENABLED TRUE)
#     else()
#         if(SDLIMAGE_TIF_VENDORED)
#             set(SDLIMAGE_TIF_ENABLED TRUE)
#             message(STATUS "${PROJECT_NAME}: Using vendored libtiff")
#             # tiff-cxx variable is used by vendored libtiff
#             set(tiff-cxx OFF CACHE BOOL "libtiff: C++ API" FORCE)
#             # tiff-tests variable is used by vendored libtiff
#             set(tiff-tests OFF CACHE BOOL "libtiff: tests" FORCE)
#             # tiff-opengl variable is used by vendored libtiff
#             set(tiff-opengl OFF CACHE BOOL "libtiff: OpenGL option" FORCE)
#             # jpeg variable is used by vendored libtiff
#             set(jpeg OFF CACHE BOOL "libtiff: jpeg option" FORCE)
#             # libdeflate variable is used by vendored libtiff
#             set(libdeflate OFF CACHE BOOL "libtiff: libdeflate option" FORCE)
#             # DEFLATE_FOUND variable is used by vendored libtiff
#             set(DEFLATE_FOUND OFF CACHE BOOL "libtiff: libdeflate option" FORCE)
#             # lerc variable is used by vendored libtiff
#             set(lerc OFF CACHE BOOL "libtiff: lerc option" FORCE)
#             # lzma variable is used by vendored libtiff
#             set(lzma OFF CACHE BOOL "libtiff: lzma option" FORCE)
#             # webp variable is used by vendored libtiff
#             set(webp OFF CACHE BOOL "libtiff: webp option" FORCE)
#             # zstd variable is used by vendored libtiff
#             set(zstd OFF CACHE BOOL "libtiff: zstd option" FORCE)
#             # ZSTD_FOUND variable is used by vendored libtiff
#             set(ZSTD_FOUND OFF)
#             # WEBP_LIBRARY variable is used by vendored libtiff
#             set(WEBP_LIBRARY "")
#             sdl_check_project_in_subfolder(external/libtiff libtiff SDLIMAGE_VENDORED)
#             set(BUILD_SHARED_LIBS ${SDLIMAGE_TIF_SHARED})
#             add_subdirectory(external/libtiff external/libtiff-build EXCLUDE_FROM_ALL)
#             register_license(tiff external/libtiff/LICENSE.md)
#             add_library(TIFF::TIFF ALIAS tiff)
#             set(SDLIMAGE_TIF_TARGET "TIFF::tiff")
#             if(SDLIMAGE_TIF_SHARED OR NOT SDLIMAGE_BUILD_SHARED_LIBS)
#               list(APPEND INSTALL_EXTRA_TARGETS tiff)
#             endif()
#             set_target_properties(tiff PROPERTIES EXPORT_NAME external_libtiff)
#             add_library(SDL3_image::external_libtiff ALIAS tiff)
#             if(NOT SDLIMAGE_TIF_SHARED)
#                 list(APPEND PC_LIBS -l$<TARGET_FILE_BASE_NAME:tiff>)
#             endif()
#         elseif(SDLIMAGE_TIF_SHARED AND DEFINED SDLIMAGE_DYNAMIC_TIF AND EXISTS "${SDLIMAGE_DYNAMIC_TIF}")
#             message(STATUS "${PROJECT_NAME}: Using libtiff from CMake variable")
#             set(SDLIMAGE_TIF_ENABLED TRUE)
#             set(SDLIMAGE_TIF_TARGET "tiff-non-existing-target")
#         else()
#             find_package(TIFF ${required})
#             if(TIFF_FOUND)
#                 message(STATUS "${PROJECT_NAME}: Using system libtiff")
#                 set(SDLIMAGE_TIF_ENABLED TRUE)
#                 if(NOT SDLIMAGE_TIF_SHARED)
#                     list(APPEND PC_REQUIRES libtiff-4)
#                 endif()
#                 if(TARGET TIFF::tiff)
#                     # introduced in CMake 3.28
#                     # TIFF::TIFF still exists, but it is an INTERFACE library linking to TIFF::tiff (no ALIAS library)
#                     set(SDLIMAGE_TIF_TARGET "TIFF::tiff")
#                 else()
#                     set(SDLIMAGE_TIF_TARGET "TIFF::TIFF")
#                 endif()
#             else()
#                 message(${fatal_error} "libtiff NOT found")
#             endif()
#         endif()
#         if(SDLIMAGE_TIF_ENABLED)
#             target_compile_definitions(${sdl3_image_target_name} PRIVATE LOAD_TIF)
#             if(SDLIMAGE_TIF_SHARED)
#                 if(NOT DEFINED SDLIMAGE_DYNAMIC_TIF)
#                     target_include_directories(${sdl3_image_target_name} PRIVATE
#                         $<TARGET_PROPERTY:${SDLIMAGE_TIF_TARGET},INCLUDE_DIRECTORIES>
#                         $<TARGET_PROPERTY:${SDLIMAGE_TIF_TARGET},INTERFACE_INCLUDE_DIRECTORIES>
#                         $<TARGET_PROPERTY:${SDLIMAGE_TIF_TARGET},INTERFACE_SYSTEM_INCLUDE_DIRECTORIES>
#                     )
#                     if(SDLIMAGE_TIF_VENDORED)
#                       add_dependencies(${sdl3_image_target_name} ${SDLIMAGE_TIF_TARGET})
#                     endif()
#                 endif()
#                 target_get_dynamic_library(SDLIMAGE_DYNAMIC_TIF ${SDLIMAGE_TIF_TARGET})
#                 message(STATUS "Dynamic libtiff: ${SDLIMAGE_DYNAMIC_TIF}")
#                 target_compile_definitions(${sdl3_image_target_name} PRIVATE "LOAD_TIF_DYNAMIC=\"${SDLIMAGE_DYNAMIC_TIF}\"")
#             else()
#                 target_link_libraries(${sdl3_image_target_name} PRIVATE ${SDLIMAGE_TIF_TARGET})
#             endif()
#         endif()
#     endif()
# endif()

# list(APPEND SDLIMAGE_BACKENDS WEBP)
# set(SDLIMAGE_WEBP_ENABLED FALSE)
# if(SDLIMAGE_WEBP)
#     # missing cpufeatures
#     if(SDLIMAGE_WEBP_VENDORED)
#         set(SDLIMAGE_WEBP_ENABLED TRUE)
#         message(STATUS "${PROJECT_NAME}: Using vendored libwebp")
#         sdl_check_project_in_subfolder(external/libwebp libwebp SDLIMAGE_VENDORED)
#         set(BUILD_SHARED_LIBS ${SDLIMAGE_WEBP_SHARED})
#         add_subdirectory(external/libwebp external/libwebp-build EXCLUDE_FROM_ALL)
#         register_license(webp external/libwebp/COPYING)
#         target_include_directories(${sdl3_image_target_name} PRIVATE external/libwebp/src)
#         add_library(WebP::webp ALIAS webp)
#         add_library(WebP::webpdemux ALIAS webpdemux)
#         add_library(WebP::libwebpmux ALIAS libwebpmux)
#         if(SDLIMAGE_WEBP_SHARED OR NOT SDLIMAGE_BUILD_SHARED_LIBS)
#             list(APPEND INSTALL_EXTRA_TARGETS webp webpdemux libwebpmux)
#             if(NOT SDLIMAGE_WEBP_SHARED)
#                 list(APPEND INSTALL_EXTRA_TARGETS sharpyuv)
#             endif()
#         endif()
#         set_target_properties(webp PROPERTIES EXPORT_NAME "external_libwebp")
#         set_target_properties(webpdemux PROPERTIES EXPORT_NAME "external_webpdemux")
#         set_target_properties(libwebpmux PROPERTIES EXPORT_NAME "external_libwebpmux")
#         set_target_properties(sharpyuv PROPERTIES EXPORT_NAME "external_sharpyuv")
#         add_library(SDL3_image::external_libwebp ALIAS webp)
#     elseif(SDLIMAGE_WEBP_SHARED AND DEFINED SDLIMAGE_DYNAMIC_WEBP AND EXISTS "${SDLIMAGE_DYNAMIC_WEBP}" AND DEFINED SDLIMAGE_DYNAMIC_WEBPDEMUX AND EXISTS "${SDLIMAGE_DYNAMIC_WEBPDEMUX}" AND DEFINED SDLIMAGE_DYNAMIC_WEBPMUX AND EXISTS "${SDLIMAGE_DYNAMIC_WEBPMUX}")
#         message(STATUS "${PROJECT_NAME}: Using libwebp from CMake variable")
#         set(SDLIMAGE_WEBP_ENABLED TRUE)
#     else()
#         find_package(webp ${required})
#         if(webp_FOUND)
#             message(STATUS "${PROJECT_NAME}: Using system libwebp")
#             set(SDLIMAGE_WEBP_ENABLED TRUE)
#             if(NOT SDLIMAGE_WEBP_SHARED)
#               list(APPEND PC_REQUIRES libwebp libwebpdemux libwebpmux)
#               list(APPEND INSTALL_EXTRA_CMAKE_MODULES cmake/Findwebp.cmake)
#             endif()
#         else()
#             message(${fatal_error} "libwebp NOT found")
#         endif()
#     endif()
#     if(SDLIMAGE_WEBP_ENABLED)
#         target_compile_definitions(${sdl3_image_target_name} PRIVATE
#             LOAD_WEBP
#             SAVE_WEBP=$<BOOL:${SDLIMAGE_WEBP_SAVE}>
#         )
#         if(SDLIMAGE_WEBP_SHARED)
#            if(NOT DEFINED SDLIMAGE_DYNAMIC_WEBP AND NOT DEFINED SDLIMAGE_DYNAMIC_WEBPDEMUX AND NOT DEFINED SDLIMAGE_DYNAMIC_WEBPMUX)
#                 target_include_directories(${sdl3_image_target_name} PRIVATE
#                     $<TARGET_PROPERTY:WebP::webp,INCLUDE_DIRECTORIES>
#                     $<TARGET_PROPERTY:WebP::webp,INTERFACE_INCLUDE_DIRECTORIES>
#                     $<TARGET_PROPERTY:WebP::webp,INTERFACE_SYSTEM_INCLUDE_DIRECTORIES>
#                     $<TARGET_PROPERTY:WebP::webpdemux,INCLUDE_DIRECTORIES>
#                     $<TARGET_PROPERTY:WebP::webpdemux,INTERFACE_INCLUDE_DIRECTORIES>
#                     $<TARGET_PROPERTY:WebP::webpdemux,INTERFACE_SYSTEM_INCLUDE_DIRECTORIES>
#                     $<TARGET_PROPERTY:WebP::libwebpmux,INCLUDE_DIRECTORIES>
#                     $<TARGET_PROPERTY:WebP::libwebpmux,INTERFACE_INCLUDE_DIRECTORIES>
#                     $<TARGET_PROPERTY:WebP::libwebpmux,INTERFACE_SYSTEM_INCLUDE_DIRECTORIES>
#                 )
#                 if(SDLIMAGE_WEBP_VENDORED)
#                     add_dependencies(${sdl3_image_target_name} WebP::webp WebP::webpdemux WebP::libwebpmux)
#                 endif()
#             endif()
#             target_get_dynamic_library(SDLIMAGE_DYNAMIC_WEBPDEMUX WebP::webpdemux)
#             message(STATUS "Dynamic libwebpdemux: ${SDLIMAGE_DYNAMIC_WEBPDEMUX}")
#             target_compile_definitions(${sdl3_image_target_name} PRIVATE "LOAD_WEBPDEMUX_DYNAMIC=\"${SDLIMAGE_DYNAMIC_WEBPDEMUX}\"")
#             target_get_dynamic_library(SDLIMAGE_DYNAMIC_WEBPMUX WebP::libwebpmux)
#             message(STATUS "Dynamic libwebpmux: ${SDLIMAGE_DYNAMIC_WEBPMUX}")
#             target_compile_definitions(${sdl3_image_target_name} PRIVATE "LOAD_WEBPMUX_DYNAMIC=\"${SDLIMAGE_DYNAMIC_WEBPMUX}\"")
#             target_get_dynamic_library(SDLIMAGE_DYNAMIC_WEBP WebP::webp)
#             message(STATUS "Dynamic libwebp: ${SDLIMAGE_DYNAMIC_WEBP}")
#             target_compile_definitions(${sdl3_image_target_name} PRIVATE "LOAD_WEBP_DYNAMIC=\"${SDLIMAGE_DYNAMIC_WEBP}\"")
#         else()
#             target_link_libraries(${sdl3_image_target_name} PRIVATE WebP::webp WebP::webpdemux WebP::libwebpmux)
#         endif()
#     else()
#       # Variable is used by test suite
#       set(SDLIMAGE_WEBP_SAVE OFF)
#     endif()
# endif()

# list(APPEND SDLIMAGE_BACKENDS XCF)
# set(SDLIMAGE_XCF_ENABLED FALSE)
# if(SDLIMAGE_XCF)
#     set(SDLIMAGE_XCF_ENABLED TRUE)
#     target_compile_definitions(${sdl3_image_target_name} PRIVATE LOAD_XCF)
# endif()

# list(APPEND SDLIMAGE_BACKENDS XPM)
# set(SDLIMAGE_XPM_ENABLED FALSE)
# if(SDLIMAGE_XPM)
#     set(SDLIMAGE_XPM_ENABLED TRUE)
#     target_compile_definitions(${sdl3_image_target_name} PRIVATE LOAD_XPM)
# endif()

# list(APPEND SDLIMAGE_BACKENDS XV)
# set(SDLIMAGE_XV_ENABLED FALSE)
# if(SDLIMAGE_XV)
#     set(SDLIMAGE_XV_ENABLED TRUE)
#     target_compile_definitions(${sdl3_image_target_name} PRIVATE LOAD_XV)
# endif()

# # Restore BUILD_SHARED_LIBS
# set(BUILD_SHARED_LIBS ${SDLIMAGE_BUILD_SHARED_LIBS})

# if(SDLIMAGE_INSTALL)
#     install(
#         TARGETS ${sdl3_image_target_name}
#         EXPORT SDL3ImageExports
#         ARCHIVE DESTINATION "${CMAKE_INSTALL_LIBDIR}" COMPONENT devel
#         LIBRARY DESTINATION "${CMAKE_INSTALL_LIBDIR}" COMPONENT library
#         RUNTIME DESTINATION "${CMAKE_INSTALL_BINDIR}" COMPONENT library
#     )
#     install(
#         FILES "${CMAKE_CURRENT_SOURCE_DIR}/include/SDL3_image/SDL_image.h"
#         DESTINATION "${CMAKE_INSTALL_INCLUDEDIR}/SDL3_image" COMPONENT DEVEL
#     )

#     export(TARGETS ${sdl3_image_target_name} ${INSTALL_EXTRA_TARGETS} NAMESPACE "SDL3_image::" FILE "${sdl3_image_target_name}-targets.cmake")

#     if(BUILD_SHARED_LIBS)
#         set(pdbdir "${CMAKE_INSTALL_BINDIR}")
#     else()
#         set(pdbdir "${CMAKE_INSTALL_LIBDIR}")
#     endif()
#     if(MSVC)
#         SDL_install_pdb("${sdl3_image_target_name}" "${pdbdir}")
#     endif()

#     if(INSTALL_EXTRA_TARGETS)
#         set_property(TARGET ${INSTALL_EXTRA_TARGETS} PROPERTY PUBLIC_HEADER "")
#         set(archive_destination)
#         if(NOT BUILD_SHARED_LIBS)
#             set(archive_destination ARCHIVE DESTINATION "${CMAKE_INSTALL_LIBDIR}" COMPONENT devel)
#         endif()
#         install(
#             TARGETS ${INSTALL_EXTRA_TARGETS}
#             EXPORT SDL3ImageExports
#             ${archive_destination}
#             LIBRARY DESTINATION "${CMAKE_INSTALL_LIBDIR}" COMPONENT library
#             RUNTIME DESTINATION "${CMAKE_INSTALL_BINDIR}" COMPONENT library
#         )
#         if(MSVC)
#             foreach(tgt IN LISTS INSTALL_EXTRA_TARGETS)
#                 SDL_install_pdb("${tgt}" "${pdbdir}")
#             endforeach()
#         endif()
#     endif()

#     if(WIN32 AND NOT MINGW)
#         set(SDLIMAGE_INSTALL_CMAKEDIR_ROOT_DEFAULT "cmake")
#     else()
#         set(SDLIMAGE_INSTALL_CMAKEDIR_ROOT_DEFAULT "${CMAKE_INSTALL_LIBDIR}/cmake")
#     endif()
#     set(SDLIMAGE_INSTALL_CMAKEDIR_ROOT "${SDLIMAGE_INSTALL_CMAKEDIR_ROOT_DEFAULT}" CACHE STRING "Root folder where to install SDL3_imageConfig.cmake related files (SDL3_image subfolder for MSVC projects)")
#     set(SDLIMAGE_PKGCONFIG_INSTALLDIR "${CMAKE_INSTALL_LIBDIR}/pkgconfig")

#     if(WIN32 AND NOT MINGW)
#         set(SDLIMAGE_INSTALL_CMAKEDIR "${SDLIMAGE_INSTALL_CMAKEDIR_ROOT}")
#     else()
#         set(SDLIMAGE_INSTALL_CMAKEDIR "${SDLIMAGE_INSTALL_CMAKEDIR_ROOT}/SDL3_image")
#     endif()

#     configure_package_config_file(cmake/SDL3_imageConfig.cmake.in SDL3_imageConfig.cmake
#         NO_SET_AND_CHECK_MACRO
#         INSTALL_DESTINATION "${SDLIMAGE_INSTALL_CMAKEDIR}"
#     )
#     write_basic_package_version_file("${PROJECT_BINARY_DIR}/SDL3_imageConfigVersion.cmake"
#         COMPATIBILITY AnyNewerVersion
#     )
#     install(
#         FILES
#             "${CMAKE_CURRENT_BINARY_DIR}/SDL3_imageConfig.cmake"
#             "${CMAKE_CURRENT_BINARY_DIR}/SDL3_imageConfigVersion.cmake"
#             ${INSTALL_EXTRA_CMAKE_MODULES}
#         DESTINATION "${SDLIMAGE_INSTALL_CMAKEDIR}"
#         COMPONENT devel
#     )
#     install(EXPORT SDL3ImageExports
#         FILE ${sdl3_image_target_name}-targets.cmake
#         NAMESPACE SDL3_image::
#         DESTINATION "${SDLIMAGE_INSTALL_CMAKEDIR}"
#         COMPONENT devel
#     )

#     if(SDLIMAGE_RELOCATABLE)
#       file(RELATIVE_PATH SDL_PATH_PREFIX_RELATIVE_TO_PKGCONFIG "${CMAKE_INSTALL_PREFIX}/${SDLIMAGE_PKGCONFIG_INSTALLDIR}" "${CMAKE_INSTALL_PREFIX}")
#       string(REGEX REPLACE "[/]+$" "" SDL_PATH_PREFIX_RELATIVE_TO_PKGCONFIG "${SDL_PATH_PREFIX_RELATIVE_TO_PKGCONFIG}")
#       set(SDL_PKGCONFIG_PREFIX "\${pcfiledir}/${SDL_PATH_PREFIX_RELATIVE_TO_PKGCONFIG}")
#     else()
#       set(SDL_PKGCONFIG_PREFIX "${CMAKE_INSTALL_PREFIX}")
#     endif()

#     if(IS_ABSOLUTE "${CMAKE_INSTALL_INCLUDEDIR}")
#       set(INCLUDEDIR_FOR_PKG_CONFIG "${CMAKE_INSTALL_INCLUDEDIR}")
#     else()
#       set(INCLUDEDIR_FOR_PKG_CONFIG "\${prefix}/${CMAKE_INSTALL_INCLUDEDIR}")
#     endif()
#     if(IS_ABSOLUTE "${CMAKE_INSTALL_LIBDIR}")
#       set(LIBDIR_FOR_PKG_CONFIG "${CMAKE_INSTALL_LIBDIR}")
#     else()
#       set(LIBDIR_FOR_PKG_CONFIG "\${prefix}/${CMAKE_INSTALL_LIBDIR}")
#     endif()

#     string(JOIN " " PC_REQUIRES ${PC_REQUIRES})
#     string(JOIN " " PC_LIBS ${PC_LIBS})
#     configure_file(cmake/sdl3-image.pc.in sdl3-image.pc @ONLY)

#     # Always install sdl3-image.pc file: libraries might be different between config modes
#     install(FILES "${CMAKE_CURRENT_BINARY_DIR}/sdl3-image.pc"
#         DESTINATION "${SDLIMAGE_PKGCONFIG_INSTALLDIR}" COMPONENT devel)

#     install(FILES "LICENSE.txt"
#         DESTINATION "${CMAKE_INSTALL_DATAROOTDIR}/licenses/${PROJECT_NAME}"
#         COMPONENT library
#     )

#     foreach(license_name IN LISTS install_license_names)
#         install(FILES "${install_license_${license_name}}" DESTINATION "${CMAKE_INSTALL_DATAROOTDIR}/licenses/${PROJECT_NAME}/optional" RENAME "LICENSE.${license_name}.txt")
#     endforeach()

#     if(SDLIMAGE_INSTALL_MAN)
#         sdl_get_git_revision_hash(SDLIMAGE_REVISION)
#         SDL_generate_manpages(
#             HEADERS_DIR "${PROJECT_SOURCE_DIR}/include/SDL3_image"
#             SYMBOL "IMG_Init"
#             WIKIHEADERS_PL_PATH "${CMAKE_CURRENT_SOURCE_DIR}/build-scripts/wikiheaders.pl"
#             REVISION "${SDLIMAGE_REVISION}"
#         )
#     endif()

#     if(SDLIMAGE_ROOTPROJECT)
#         configure_file(cmake/cmake_uninstall.cmake.in cmake_uninstall.cmake IMMEDIATE @ONLY)

#         add_custom_target(uninstall
#             COMMAND ${CMAKE_COMMAND} -P "${CMAKE_CURRENT_BINARY_DIR}/cmake_uninstall.cmake")
#     endif()
# endif()

# if(SDLIMAGE_SAMPLES)
#     function(add_sdl_image_example_executable TARGET)
#         if(ANDROID)
#             add_library(${TARGET} SHARED ${ARGN})
#         else()
#             add_executable(${TARGET} ${ARGN})
#         endif()
#         sdl_add_warning_options(${TARGET} WARNING_AS_ERROR ${SDLIMAGE_WERROR})
#         sdl_target_link_options_no_undefined(${TARGET})
#         target_link_libraries(${TARGET} PRIVATE SDL3_image::${sdl3_image_target_name})
#         target_link_libraries(${TARGET} PRIVATE ${sdl3_target_name})

#         if(SDLIMAGE_SAMPLES_INSTALL)
#             install(TARGETS ${TARGET}
#                 RUNTIME DESTINATION "${CMAKE_INSTALL_LIBEXECDIR}/installed-tests/SDL3_image"
#             )
#             if(MSVC)
#                 SDL_install_pdb("${TARGET}" "${CMAKE_INSTALL_LIBEXECDIR}/installed-tests/SDL3_image")
#             endif()
#         endif()
#     endfunction()
#     add_sdl_image_example_executable(showanim examples/showanim.c)
#     add_sdl_image_example_executable(showimage examples/showimage.c)
#     add_sdl_image_example_executable(showclipboard examples/showclipboard.c)
#     add_sdl_image_example_executable(showgpuimage examples/showgpuimage.c)
# endif()

# if(SDLIMAGE_TESTS)
#     enable_testing()
#     add_subdirectory(test)
# endif()


# set(available_deps)
# set(unavailable_deps)
# foreach(dep IN LISTS SDLIMAGE_BACKENDS)
#   set(var SDLIMAGE_${dep}_ENABLED)
#   if(NOT DEFINED ${var})
#     message(AUTHOR_WARNING "${var} not defined")
#   endif()
#   if(${var})
#     list(APPEND available_deps ${dep})
#   else()
#     list(APPEND unavailable_deps ${dep})
#   endif()
# endforeach()
# string(JOIN " " avail_str ${available_deps})
# string(TOLOWER "${avail_str}" avail_str)
# string(JOIN " " unavail_str ${unavailable_deps})
# string(TOLOWER "${unavail_str}" unavail_str)
# message(STATUS "SDL3_image backends:")
# message(STATUS "- enabled:  ${avail_str}")
# message(STATUS "- disabled: ${unavail_str}")

sdl3_image_lib = library('sdl3_image',
  sdl3_image_src,
  include_directories: 'include',
  dependencies: deps)

sdl3_image_dep = declare_dependency(include_directories: 'include',
  link_with: sdl3_image_lib)