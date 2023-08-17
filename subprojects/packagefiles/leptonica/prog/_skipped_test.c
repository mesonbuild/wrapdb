#include <stdio.h>

int main(void) {
    fprintf(stderr, "skipping: %s\n", SKIP_REASON);
    return 77;
}
