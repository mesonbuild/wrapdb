// Modified manually for Meson wrap

#ifndef GLBINDING_AUX_TEMPLATE_API_H
#define GLBINDING_AUX_TEMPLATE_API_H

#include <glbinding-aux/glbinding-aux_export.h>

#ifdef GLBINDING_AUX_STATIC_DEFINE
#  define GLBINDING_AUX_TEMPLATE_API
#else
#  ifndef GLBINDING_AUX_TEMPLATE_API
#    ifdef _MSC_VER
#      define GLBINDING_AUX_TEMPLATE_API
#    else
#      define GLBINDING_AUX_TEMPLATE_API __attribute__((visibility("default")))
#    endif
#  endif

#endif

#endif
