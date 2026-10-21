/*
 * Upstream's cmake/msvc/sys/time.h does #include < time.h >, which clang-cl
 * rejects. qa_utils.cc only includes <sys/time.h> for CLOCKS_PER_SEC.
 */
#ifndef VOLK_WRAP_SYS_TIME_H
#define VOLK_WRAP_SYS_TIME_H

#include <time.h>

#endif
