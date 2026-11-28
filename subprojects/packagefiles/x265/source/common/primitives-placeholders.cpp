#include "cpu.h"

#if !defined(ENABLE_ASSEMBLY) && defined(X265_ARCH_ARM)
extern "C" {
void PFX(cpu_neon_test)(void) {}
int PFX(cpu_fast_neon_mrc_test)(void) { return 0; }
} // extern "C"
#endif // X265_ARCH_ARM
