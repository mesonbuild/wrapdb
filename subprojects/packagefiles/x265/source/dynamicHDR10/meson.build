dynamicHDR10_srcs = files(
  'BasicStructures.h',
  # 'json11/json11.cpp',
  'JsonHelper.cpp',
  'JsonHelper.h',
  'SeiMetadataDictionary.cpp',
  'SeiMetadataDictionary.h',
  'api.cpp',
  'hdr10plus.h',
  'json11/json11.h',
  'metadataFromJson.cpp',
  'metadataFromJson.h',
)

# FIXME UPSTREAM: <cstdint> is now required for building with new GCC --Amy
# https://gitlab.archlinux.org/archlinux/packaging/packages/x265/-/commit/9d27978355453de977f7ac88144857525a2fb5cc
needs_cstdint_workaround = not cpp.has_type(
  'uint8_t',
  prefix: '''
#include <string>
#include <vector>
#include <map>
#include <memory>
#include <initializer_list>
#include <cassert>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <limits>
''',
)
if needs_cstdint_workaround
  dynamicHDR10_srcs += files('json11/gcc15-workaround.cpp')
else
  dynamicHDR10_srcs += files('json11/json11.cpp')
endif

install_headers('hdr10plus.h')
