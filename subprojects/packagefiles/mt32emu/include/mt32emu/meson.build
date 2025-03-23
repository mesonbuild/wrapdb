configure_file(
  input: mt32emu_config_h_in,
  output: 'config.h',
  configuration: conf_data,
)

foreach src_dest : mt32emu_header_map
  configure_file(
    input: src_dest[0],
    output: src_dest[1],
    copy: true,
  )
endforeach

subdir('c_interface')
