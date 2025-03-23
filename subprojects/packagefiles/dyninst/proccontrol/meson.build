srcs = files(
  'src/arm_process.C',
  'src/event.C',
  'src/generator.C',
  'src/handler.C',
  'src/irpc.C',
  'src/loadLibrary/codegen-aarch64.C',
  'src/loadLibrary/codegen-ppc.C',
  'src/loadLibrary/codegen-x86.C',
  'src/loadLibrary/codegen.C',
  'src/loadLibrary/injector.C',
  'src/mailbox.C',
  'src/memcache.C',
  'src/pcerrors.C',
  'src/pcmachsyscall.C',
  'src/ppc_process.C',
  'src/process.C',
  'src/processplat.C',
  'src/procpool.C',
  'src/procset.C',
  'src/resp.C',
  'src/response.C',
  'src/x86_process.C',
)

if host_machine.system() in ['linux', 'freebsd']
  srcs += files('src/int_thread_db.C', 'src/mmapalloc.C', 'src/sysv.C')
elif host_machine.system() == 'windows'
  srcs += files(
    '../common/src/dthread-win.C',
    '../common/src/dthread.C',
    'src/DecoderWindows.C',
    'src/GeneratorWindows.C',
    'src/loadLibrary/codegen-win.C',
    'src/windows_handler.C',
    'src/windows_process.C',
    'src/windows_thread.C',
  )
endif

if host_machine.system() == 'freebsd'
  srcs += files(
    '../common/src/dthread-unix.C',
    '../common/src/dthread.C',
    'src/freebsd.C',
    'src/loadLibrary/codegen-freebsd.C',
    'src/notify_pipe.C',
    'src/unix.C',
  )
elif host_machine.system() == 'linux'
  srcs += files(
    '../common/src/dthread-unix.C',
    '../common/src/dthread.C',
    'src/linux.C',
    'src/loadLibrary/codegen-linux.C',
    'src/notify_pipe.C',
    'src/unix.C',
  )
endif

args = ['-DPROCCONTROL_EXPORTS']

iface_deps = [common_dep, boost_dep]
if get_option('lightweight_symtab')
  iface_deps += [symlite_dep]
else
  iface_deps += [symtabapi_dep]
endif

install_headers(
  'h/Decoder.h',
  'h/Event.h',
  'h/EventType.h',
  'h/Handler.h',
  'h/Mailbox.h',
  'h/PCErrors.h',
  'h/PCProcess.h',
  'h/PlatFeatures.h',
  'h/ProcessSet.h',
)

pcontrol_lib = library(
  'pcontrol',
  srcs,
  gnu_symbol_visibility: 'inlineshidden',
  override_options: ['b_ndebug=false'],
  include_directories: include_directories(
    '..',
    'src',
    'h',
    (get_option('lightweight_symtab') ? ['../symtabAPI/h'] : []),
    # Comes through hack CMake target trickery
    '../common/src',
    (get_option('lightweight_symtab') ? ['../symlite/src'] : [
      '../symtabAPI/src',
    ]),
  ),
  c_args: args,
  cpp_args: args,
  dependencies: [iface_deps, dl_dep, threads_dep],
  version: meson.project_version(),
  soversion: dyninst_soversion,
  install: true,
)
pcontrol_dep = declare_dependency(
  link_with: pcontrol_lib,
  include_directories: include_directories('h'),
  dependencies: iface_deps,
)
all_deps += pcontrol_dep
