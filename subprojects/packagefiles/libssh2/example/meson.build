examples = [
  'direct_tcpip',
  'scp',
  'scp_nonblock',
  'scp_write',
  'scp_write_nonblock',
  'sftp',
  'sftp_RW_nonblock',
  'sftp_append',
  'sftp_mkdir',
  'sftp_mkdir_nonblock',
  'sftp_nonblock',
  'sftp_write',
  'sftp_write_nonblock',
  'sftp_write_sliding',
  'sftpdir',
  'sftpdir_nonblock',
  'ssh2',
  'ssh2_agent',
  'ssh2_echo',
  'ssh2_exec',
  'subsystem_netconf',
  'tcpip-forward',
]

x11_dep = dependency(
  'x11',
  required: false,
)
if x11_dep.found()
  examples += 'x11'
endif

foreach example : examples
  executable(
    example,
    '@0@.c'.format(example),
    include_directories: include_directories('../src'),
    dependencies: [libssh2_dep, ws_dep],
  )
endforeach
