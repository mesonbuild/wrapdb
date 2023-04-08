// Modified manually for Meson wrap

#ifndef GLBINDING_TEMPLATE_API_H
#define GLBINDING_TEMPLATE_API_H

#include <glbinding/glbinding_export.h>

#ifdef GLBINDING_STATIC_DEFINE
#  define GLBINDING_TEMPLATE_API
#else
#  ifndef GLBINDING_TEMPLATE_API
#    ifdef _MSC_VER
#      define GLBINDING_TEMPLATE_API
#    else
#      define GLBINDING_TEMPLATE_API __attribute__((visibility("default")))
#    endif
#  endif

#endif

#endif
