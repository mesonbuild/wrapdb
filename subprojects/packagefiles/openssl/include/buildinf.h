#define PLATFORM "platform: (see uname)"
#define DATE "built on: the date it was built on, see https://reproducible-builds.org for why this doesn't matter"

/*
 * Generate compiler_flags as an array of individual characters. This is a
 * workaround for the situation where CFLAGS gets too long for a C90 string
 * literal
 */
static const char compiler_flags[] = {
    'c','o','m','p','i','l','e','r',':',' ','a','n','o','n','y','m',
    'o','u','s','\0'
};
