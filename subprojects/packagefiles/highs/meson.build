project('HiGHS', ['c', 'cpp'],
  version : '1.2.0',
  default_options : ['warning_level=3', 'cpp_std=c++11'])

compiler = meson.get_compiler('cpp')

have_mm_pause = compiler.compiles('''
  #include <immintrin.h>
  int main () {
    _mm_pause();
    return 0;
  }''',
  name : '_mm_pause')

have_builtin_clz = compiler.compiles('''
  #include <cstdint>
  int main () {
    unsigned int x = 5;
    unsigned long long y = __builtin_clz(x);
    x = __builtin_clzll(y);
    return 0;
  }''',
  name : '__builtin_clzll')

have_bitscan_reverse = compiler.compiles('''
  #include <intrin.h>
  #pragma intrinsic(_BitScanReverse)
  #pragma intrinsic(_BitScanReverse64)
  int main () {
    unsigned long x = 5;
    unsigned long y;
    _BitScanReverse(&y, x);
    _BitScanReverse64(&x, y);
    return 0;
  }''',
  name : '_BitScanReverse')
  
highs_include_directories = include_directories([
  '.',
  'app',
  'extern',
  'src',
  'src/io',
  'src/ipm/ipx',
  'src/ipm/ipx/include/',
  'src/ipm/basiclu',
  'src/lp_data',
  'src/mip',
  'src/model',
  'src/presolve',
  'src/qpsolver',
  'src/simplex',
  'src/test',
  'src/util',
])

ipx_on = get_option('ipx')
if not get_option('fast_build')
  ipx_on = true
endif

version_split = meson.project_version().split('.')
conf_data = configuration_data()
conf_data.set('FAST_BUILD', get_option('fast_build'))
#conf_data.set('SCIP_DEV', scip_dev)
#conf_data.set('HiGHSDEV', highs_dev)
conf_data.set('IPX_ON', ipx_on)
conf_data.set('HIGHSINT64', get_option('highsint64'))
conf_data.set('CMAKE_SOURCE_DIR', meson.project_source_root())
conf_data.set('HIGHS_VERSION_MAJOR', version_split[0])
conf_data.set('HIGHS_VERSION_MINOR', version_split[1])
conf_data.set('HIGHS_VERSION_PATCH', version_split[2])
conf_data.set('HIGHS_HAVE_MM_PAUSE', have_mm_pause)
conf_data.set('HIGHS_HAVE_BUILTIN_CLZ', have_builtin_clz)
conf_data.set('HIGHS_HAVE_BITSCAN_REVERSE', have_bitscan_reverse)

hconfig = configure_file(
  input : 'src/HConfig.h.in',
  output : 'HConfig.h',
  configuration : conf_data,
  format : 'cmake@') 
               
hconfig_include_dir = include_directories('.')

subdir('src')
highs_deps = [dependency('threads')]
if ipx_on
  highs_deps += ipx_dep
endif

libhighs = library(
  'highs', highs_sources,
  dependencies : highs_deps,
  include_directories : highs_include_directories) 

highs_dep = declare_dependency(
  dependencies : highs_deps,
  link_with : libhighs,
  include_directories : highs_public_include_directories)

subdir('check')

